
import { createContext, useContext } from "react";
import useLocalStorage from "../hooks/useLocalStorage.js";

const BookContext = createContext();

export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage("my-personal-books", []);

  function addBook(book) {
    const newBook = {
      ...book,
      id: crypto.randomUUID(),
    };

    setBooks((currentBooks) => [...currentBooks, newBook]);
  }

  function updateBook(id, updatedBook) {
    setBooks((currentBooks) =>
      currentBooks.map((book) =>
        book.id === id ? { ...book, ...updatedBook } : book
      )
    );
  }

  function deleteBook(id) {
    setBooks((currentBooks) =>
      currentBooks.filter((book) => book.id !== id)
    );
  }

  return (
    <BookContext.Provider value={{ books, addBook, updateBook, deleteBook }}>
      {children}
    </BookContext.Provider>
  );
}

export function useBooks() {
  return useContext(BookContext);
}
