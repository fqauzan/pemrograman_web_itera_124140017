
export function filterBooks(books, search, status) {
  const keyword = search.toLowerCase();

  return books.filter((book) => {
    const matchesSearch =
      book.title.toLowerCase().includes(keyword) ||
      book.author.toLowerCase().includes(keyword);

    const matchesStatus =
      status === "semua" || book.status === status;

    return matchesSearch && matchesStatus;
  });
}

export function getBookStats(books) {
  return {
    totalBooks: books.length,
    readingBooks: books.filter(
      (book) => book.status === "baca"
    ).length,
    wantedBooks: books.filter(
      (book) => book.status === "beli"
    ).length,
  };
}
