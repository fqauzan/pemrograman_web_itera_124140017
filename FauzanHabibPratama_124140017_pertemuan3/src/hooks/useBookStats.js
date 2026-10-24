
import { useBooks } from "../context/BookContext.jsx";

export default function useBookStats() {
  const { books } = useBooks();

  return {
    totalBooks: books.length,
    readingBooks: books.filter((book) => book.status === "baca").length,
    wantedBooks: books.filter((book) => book.status === "beli").length,
  };
}
