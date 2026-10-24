
import { describe, it, expect } from "vitest";
import { filterBooks, getBookStats } from "./bookUtils.js";

const books = [
  {
    id: "1",
    title: "Belajar React",
    author: "Andi",
    status: "baca",
  },
  {
    id: "2",
    title: "Dasar Python",
    author: "Budi",
    status: "milik",
  },
  {
    id: "3",
    title: "Pemrograman Web",
    author: "Andi",
    status: "beli",
  },
];

describe("Pengujian Manajemen Buku", () => {
  it("1. Menghitung total buku", () => {
    expect(getBookStats(books).totalBooks).toBe(3);
  });

  it("2. Menghitung buku yang sedang dibaca", () => {
    expect(getBookStats(books).readingBooks).toBe(1);
  });

  it("3. Menghitung buku yang ingin dibeli", () => {
    expect(getBookStats(books).wantedBooks).toBe(1);
  });

  it("4. Mencari buku berdasarkan judul", () => {
    const result = filterBooks(books, "react", "semua");

    expect(result).toHaveLength(1);
    expect(result[0].title).toBe("Belajar React");
  });

  it("5. Memfilter buku berdasarkan status", () => {
    const result = filterBooks(books, "", "baca");

    expect(result).toHaveLength(1);
    expect(result[0].status).toBe("baca");
  });
});
