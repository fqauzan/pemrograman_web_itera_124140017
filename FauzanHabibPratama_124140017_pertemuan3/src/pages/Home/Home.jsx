
import { useState } from "react";
import { Link } from "react-router-dom";
import { useBooks } from "../../context/BookContext.jsx";
import useBookStats from "../../hooks/useBookStats.js";
import { filterBooks } from "../../hooks/bookUtils.js";
import BookForm from "../../components/BookForm/BookForm.jsx";
import BookList from "../../components/BookList/BookList.jsx";
import BookFilter from "../../components/BookFilter/BookFilter.jsx";
import "./Home.css";

export default function Home() {
  const { books } = useBooks();
  const { totalBooks, readingBooks, wantedBooks } = useBookStats();

  const [search, setSearch] = useState("");
  const [status, setStatus] = useState("semua");
  const [editingBook, setEditingBook] = useState(null);

  const filteredBooks = filterBooks(books, search, status);

  return (
    <main className="app">
      <header className="app-header">
        <p className="eyebrow">PERSONAL LIBRARY</p>
        <h1>Manajemen Buku Pribadi</h1>
        <p>Catat, cari, dan kelola koleksi buku pribadimu.</p>

        <Link to="/stats" className="stats-link">
          Lihat Statistik Lengkap
        </Link>
      </header>

      <section className="dashboard-stats">
        <div className="stat-card">
          <span>Total Buku</span>
          <strong>{totalBooks}</strong>
        </div>

        <div className="stat-card">
          <span>Sedang Dibaca</span>
          <strong>{readingBooks}</strong>
        </div>

        <div className="stat-card">
          <span>Ingin Dibeli</span>
          <strong>{wantedBooks}</strong>
        </div>
      </section>

      <section className="panel">
        <BookForm
          key={editingBook?.id || "new-book"}
          editingBook={editingBook}
          onFinishEdit={() => setEditingBook(null)}
        />
      </section>

      <section className="panel">
        <BookFilter
          search={search}
          onSearchChange={setSearch}
          status={status}
          onStatusChange={setStatus}
        />

        <BookList
          books={filteredBooks}
          onEdit={setEditingBook}
        />
      </section>

      <footer>
        <p>Manajemen Buku Pribadi · Praktikum React</p>
      </footer>
    </main>
  );
}
