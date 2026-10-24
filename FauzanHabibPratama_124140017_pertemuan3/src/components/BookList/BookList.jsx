
import { useBooks } from "../../context/BookContext.jsx";
import "./BookList.css";

export default function BookList({ books: displayedBooks, onEdit }) {
  const { books: allBooks, deleteBook } = useBooks();

  const books = displayedBooks ?? allBooks;

  function handleDelete(id) {
    const confirmed = window.confirm("Yakin ingin menghapus buku ini?");

    if (confirmed) {
      deleteBook(id);
    }
  }

  function getStatusLabel(status) {
    const labels = {
      milik: "Buku Milik Saya",
      baca: "Sedang Dibaca",
      beli: "Ingin Dibeli",
    };

    return labels[status] || status;
  }

  return (
    <section className="book-list">
      <h2>Daftar Buku ({books.length})</h2>

      {books.length === 0 ? (
        <p className="empty-message">
          Belum ada buku yang sesuai.
        </p>
      ) : (
        <div className="book-grid">
          {books.map((book) => (
            <article className="book-card" key={book.id}>
              <h3>{book.title}</h3>

              <p>
                <strong>Penulis:</strong> {book.author}
              </p>

              <p>
                <strong>Status:</strong>{" "}
                {getStatusLabel(book.status)}
              </p>

              <div className="book-actions">
                <button
                  type="button"
                  className="edit-button"
                  onClick={() => onEdit?.(book)}
                >
                  Edit
                </button>

                <button
                  type="button"
                  className="delete-button"
                  onClick={() => handleDelete(book.id)}
                >
                  Hapus
                </button>
              </div>
            </article>
          ))}
        </div>
      )}
    </section>
  );
}
