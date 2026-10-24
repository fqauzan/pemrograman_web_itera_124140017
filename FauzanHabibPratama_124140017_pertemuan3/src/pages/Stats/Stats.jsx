
import useBookStats from "../../hooks/useBookStats.js";
import "./Stats.css";

export default function Stats() {
  const { totalBooks, readingBooks, wantedBooks } = useBookStats();

  return (
    <main className="stats-page">
      <h1>Statistik Buku</h1>

      <div className="stats-grid">
        <section className="stats-card">
          <h2>Total Buku</h2>
          <p>{totalBooks}</p>
        </section>

        <section className="stats-card">
          <h2>Sedang Dibaca</h2>
          <p>{readingBooks}</p>
        </section>

        <section className="stats-card">
          <h2>Ingin Dibeli</h2>
          <p>{wantedBooks}</p>
        </section>
      </div>
    </main>
  );
}
