from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound

from ..models import Matakuliah


def _is_positive_int(value):
    """True jika value bilangan bulat > 0 (boolean ditolak)."""
    return (isinstance(value, int) and not isinstance(value, bool)
            and value > 0)


def _validate_numeric(data):
    """Validasi sks & semester jika ada. Return pesan error atau None."""
    for field in ('sks', 'semester'):
        if field in data and not _is_positive_int(data[field]):
            return f'Field {field} harus berupa bilangan bulat lebih dari 0'
    return None


def _not_found(mk_id):
    return HTTPNotFound(
        json_body={'error': f'Matakuliah dengan ID {mk_id} tidak ditemukan'})


def _get_json(request):
    """Ambil body JSON. Return None jika tidak valid."""
    try:
        data = request.json_body
    except ValueError:
        return None
    return data if isinstance(data, dict) else None


# 1. READ ALL
@view_config(route_name='matakuliah_list', renderer='json')
def matakuliah_list(request):
    items = request.dbsession.query(Matakuliah).order_by(
        Matakuliah.id.asc()).all()
    return {'matakuliahs': [m.to_dict() for m in items]}


# 2. READ ONE
@view_config(route_name='matakuliah_detail', renderer='json')
def matakuliah_detail(request):
    mk_id = request.matchdict['id']
    mk = request.dbsession.query(Matakuliah).filter_by(id=mk_id).first()
    if mk is None:
        return _not_found(mk_id)
    return {'matakuliah': mk.to_dict()}


# 3. CREATE
@view_config(route_name='matakuliah_add', renderer='json')
def matakuliah_add(request):
    data = _get_json(request)
    if data is None:
        return HTTPBadRequest(
            json_body={'error': 'Body harus berupa JSON object yang valid'})

    for field in ('kode_mk', 'nama_mk', 'sks', 'semester'):
        if field not in data or data[field] in (None, ''):
            return HTTPBadRequest(
                json_body={'error': f'Field {field} wajib diisi!'})

    error = _validate_numeric(data)
    if error:
        return HTTPBadRequest(json_body={'error': error})

    dbsession = request.dbsession
    if dbsession.query(Matakuliah).filter_by(kode_mk=data['kode_mk']).first():
        return HTTPBadRequest(json_body={
            'error': f"Kode MK {data['kode_mk']} sudah digunakan"})

    mk = Matakuliah(
        kode_mk=data['kode_mk'],
        nama_mk=data['nama_mk'],
        sks=data['sks'],
        semester=data['semester'],
    )
    dbsession.add(mk)
    dbsession.flush()  # agar id terisi

    return {'success': True, 'matakuliah': mk.to_dict()}


# 4. UPDATE
@view_config(route_name='matakuliah_update', renderer='json')
def matakuliah_update(request):
    dbsession = request.dbsession
    mk_id = request.matchdict['id']

    mk = dbsession.query(Matakuliah).filter_by(id=mk_id).first()
    if mk is None:
        return _not_found(mk_id)

    data = _get_json(request)
    if data is None:
        return HTTPBadRequest(
            json_body={'error': 'Body harus berupa JSON object yang valid'})

    error = _validate_numeric(data)
    if error:
        return HTTPBadRequest(json_body={'error': error})

    for field in ('kode_mk', 'nama_mk'):
        if field in data and not data[field]:
            return HTTPBadRequest(
                json_body={'error': f'Field {field} tidak boleh kosong'})

    if 'kode_mk' in data:
        duplikat = (
            dbsession.query(Matakuliah)
            .filter(Matakuliah.kode_mk == data['kode_mk'],
                    Matakuliah.id != mk.id)
            .first()
        )
        if duplikat:
            return HTTPBadRequest(json_body={
                'error': f"Kode MK {data['kode_mk']} sudah digunakan"})
        mk.kode_mk = data['kode_mk']

    if 'nama_mk' in data:
        mk.nama_mk = data['nama_mk']
    if 'sks' in data:
        mk.sks = data['sks']
    if 'semester' in data:
        mk.semester = data['semester']

    return {'success': True, 'matakuliah': mk.to_dict()}


# 5. DELETE
@view_config(route_name='matakuliah_delete', renderer='json')
def matakuliah_delete(request):
    dbsession = request.dbsession
    mk_id = request.matchdict['id']

    mk = dbsession.query(Matakuliah).filter_by(id=mk_id).first()
    if mk is None:
        return _not_found(mk_id)

    dbsession.delete(mk)
    return {'success': True,
            'message': f'Matakuliah dengan ID {mk_id} berhasil dihapus'}