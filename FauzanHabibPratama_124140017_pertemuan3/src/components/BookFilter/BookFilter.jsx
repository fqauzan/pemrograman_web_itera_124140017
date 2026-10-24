
import PropTypes from "prop-types";

function BookFilter({
  search,
  onSearchChange,
  status,
  onStatusChange,
}) {
  return (
    <section className="book-filter">
      <h2>Cari dan Filter Buku</h2>

      <label htmlFor="search">
        Cari judul atau penulis
      </label>

      <input
        id="search"
        type="search"
        placeholder="Ketik judul atau nama penulis..."
        value={search}
        onChange={(event) => onSearchChange(event.target.value)}
      />

      <label htmlFor="filter-status">Filter status</label>

      <select
        id="filter-status"
        value={status}
        onChange={(event) => onStatusChange(event.target.value)}
      >
        <option value="semua">Semua Buku</option>
        <option value="milik">Buku Milik Saya</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>
    </section>
  );
}

BookFilter.propTypes = {
  search: PropTypes.string.isRequired,
  onSearchChange: PropTypes.func.isRequired,
  status: PropTypes.string.isRequired,
  onStatusChange: PropTypes.func.isRequired,
};

export default BookFilter;
