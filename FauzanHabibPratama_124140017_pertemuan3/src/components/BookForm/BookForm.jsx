
import { useState } from "react";
import PropTypes from "prop-types";
import { useBooks } from "../../context/BookContext";

function BookForm({ editingBook, onFinishEdit }) {
  const { addBook, updateBook } = useBooks();

  const [title, setTitle] = useState(editingBook?.title || "");
  const [author, setAuthor] = useState(editingBook?.author || "");
  const [status, setStatus] = useState(editingBook?.status || "milik");
  const [error, setError] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    if (!title.trim() || !author.trim()) {
      setError("Judul dan nama penulis wajib diisi.");
      return;
    }

    const bookData = {
      title: title.trim(),
      author: author.trim(),
      status,
    };

    if (editingBook) {
      updateBook(editingBook.id, bookData);
      onFinishEdit();
    } else {
      addBook(bookData);
    }

    setTitle("");
    setAuthor("");
    setStatus("milik");
    setError("");
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>{editingBook ? "Edit Buku" : "Tambah Buku Baru"}</h2>

      <label htmlFor="title">Judul Buku</label>
      <input
        id="title"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
        placeholder="Masukkan judul buku"
      />

      <label htmlFor="author">Nama Penulis</label>
      <input
        id="author"
        value={author}
        onChange={(event) => setAuthor(event.target.value)}
        placeholder="Masukkan nama penulis"
      />

      <label htmlFor="status">Status Buku</label>
      <select
        id="status"
        value={status}
        onChange={(event) => setStatus(event.target.value)}
      >
        <option value="milik">Buku Milik Saya</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>

      {error && <p role="alert">{error}</p>}

      <button type="submit">
        {editingBook ? "Simpan Perubahan" : "Tambah Buku"}
      </button>

      {editingBook && (
        <button type="button" onClick={onFinishEdit}>
          Batal
        </button>
      )}
    </form>
  );
}

BookForm.propTypes = {
  editingBook: PropTypes.object,
  onFinishEdit: PropTypes.func,
};

BookForm.defaultProps = {
  editingBook: null,
  onFinishEdit: () => {},
};

export default BookForm;

