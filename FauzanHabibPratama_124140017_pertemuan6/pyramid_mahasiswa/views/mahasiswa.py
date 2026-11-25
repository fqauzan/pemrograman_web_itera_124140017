import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest

from ..models import Mahasiswa


@view_config(route_name='mahasiswa_list', renderer='json')
def mahasiswa_list(request):
    items = request.dbsession.query(Mahasiswa).order_by(Mahasiswa.id.asc()).all()
    return {'mahasiswas': [m.to_dict() for m in items]}


@view_config(route_name='mahasiswa_detail', renderer='json')
def mahasiswa_detail(request):
    mid = request.matchdict['id']
    m = request.dbsession.query(Mahasiswa).filter_by(id=mid).first()
    if m is None:
        return HTTPNotFound(
            json_body={'error': f'Mahasiswa dengan ID {mid} tidak ditemukan'})
    return {'mahasiswa': m.to_dict()}


@view_config(route_name='mahasiswa_add', renderer='json')
def mahasiswa_add(request):
    try:
        data = request.json_body
        for field in ['nim', 'nama', 'jurusan']:
            if field not in data or not data[field]:
                return HTTPBadRequest(
                    json_body={'error': f'Field {field} wajib diisi!'})

        tgl = None
        if data.get('tanggal_lahir'):
            try:
                tgl = datetime.datetime.fromisoformat(
                    data['tanggal_lahir']).date()
            except ValueError:
                return HTTPBadRequest(json_body={
                    'error': 'Format tanggal lahir tidak valid. Gunakan YYYY-MM-DD'})

        m = Mahasiswa(nim=data['nim'], nama=data['nama'],
                      jurusan=data['jurusan'], tanggal_lahir=tgl,
                      alamat=data.get('alamat'))
        request.dbsession.add(m)
        request.dbsession.flush()
        return {'success': True, 'mahasiswa': m.to_dict()}
    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})


@view_config(route_name='mahasiswa_update', renderer='json')
def mahasiswa_update(request):
    mid = request.matchdict['id']
    m = request.dbsession.query(Mahasiswa).filter_by(id=mid).first()
    if m is None:
        return HTTPNotFound(
            json_body={'error': f'Mahasiswa dengan ID {mid} tidak ditemukan'})
    try:
        data = request.json_body
        for f in ('nim', 'nama', 'jurusan', 'alamat'):
            if f in data:
                setattr(m, f, data[f])
        if 'tanggal_lahir' in data:
            if data['tanggal_lahir']:
                try:
                    m.tanggal_lahir = datetime.datetime.fromisoformat(
                        data['tanggal_lahir']).date()
                except ValueError:
                    return HTTPBadRequest(json_body={
                        'error': 'Format tanggal lahir tidak valid. Gunakan YYYY-MM-DD'})
            else:
                m.tanggal_lahir = None
        return {'success': True, 'mahasiswa': m.to_dict()}
    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})


@view_config(route_name='mahasiswa_delete', renderer='json')
def mahasiswa_delete(request):
    mid = request.matchdict['id']
    m = request.dbsession.query(Mahasiswa).filter_by(id=mid).first()
    if m is None:
        return HTTPNotFound(
            json_body={'error': f'Mahasiswa dengan ID {mid} tidak ditemukan'})
    request.dbsession.delete(m)
    return {'success': True,
            'message': f'Mahasiswa dengan ID {mid} berhasil dihapus'}