import datetime

class Perpustakaan:
    def __init__(self):
        self.buku = {
            '001': {'Title': "A Game of Thrones", 'Author': 'George R. R. Martin', 'Release date': '1996', 'Price': 20000},
            '002': {'Title': "Harry Potter and the Chamber of Secrets", 'Author': 'J.K. Rowling', 'Release date': '1998', 'Price': 15000},
            '003': {'Title': "Harry Potter and the Philosopher's Stone", 'Author': 'J.K. Rowling', 'Release date': '1999', 'Price': 25000},
            '004': {'Title': "Harry Potter and the Prisoner of Azkaban", 'Author': 'J.K. Rowling', 'Release date': '1997', 'Price': 15000},
            '005': {'Title': "A Storm of Swords", 'Author': 'George R. R. Martin', 'Release date': '2000', 'Price': 15000},
            '006': {'Title': "Dune", 'Author': 'Frank Herbert', 'Release date': '1965', 'Price': 30000},
            '007': {'Title': "The Lord of the Rings", 'Author': 'J.R.R. Tolkien', 'Release date': '1954', 'Price': 40000},
            '008': {'Title': "Fight Club", 'Author': 'Chuck Palahniuk', 'Release date': '1996', 'Price': 15000},
            '009': {'Title': "Battle Royale", 'Author': 'Koushun Takami', 'Release date': '1999', 'Price': 15000},
            '010': {'Title': "The Green Mile", 'Author': 'Stephen King', 'Release date': '1996', 'Price': 20000},
        }
        self.next_book_id = int(max(self.buku, key=lambda x: int(x))) + 1 if self.buku else 1
        self.membership_discount = 0.2

    def generate_book_id(self):
        return '{:03}'.format(self.next_book_id)

    def tambah_buku(self, title, author, release_date, price):
        existing_book = next((key for key, value in self.buku.items() if value['Title'] == title), None)

        if existing_book:
            # Buku sudah ada, tambahkan stok
            print(f"Buku dengan judul {title} sudah ada di perpustakaan.")
            return existing_book
        else:
            # Buku belum ada, tampilkan konfirmasi
            print("\nDetail Buku yang Akan Ditambahkan:")
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Release Date: {release_date}")
            print(f"Price: {price}")

            confirm = input("Apakah Anda yakin ingin menambahkan buku ini? (Y/N): ").upper()

            if confirm == 'Y':
                # Tambahkan buku baru
                book_id = self.generate_book_id()
                self.next_book_id += 1

                self.buku[book_id] = {
                    'Title': title,
                    'Author': author,
                    'Release date': release_date,
                    'Price': price
                }
                print(f"Buku dengan ID {book_id} berhasil ditambahkan.")
                return book_id
            else:
                print("Penambahan buku dibatalkan.")
                return None

    def tampilkan_semua_buku(self, sort_by=None):
        if not self.buku:
            print("Perpustakaan kosong.")
        else:
            if sort_by:
                sorted_buku = sorted(self.buku.items(), key=lambda x: x[1][sort_by] if sort_by in x[1] else x[1]['Title'])
                buku_to_display = dict(sorted_buku)
            else:
                buku_to_display = self.buku

            print("{:<5}||{:<40}||{:<20}||{:<15}||{}".format("ID", "Title", "Author", "Release Date", "Price"))
            print("=" * 90)
            for book_id, info in buku_to_display.items():
                print("{:<5}||{:<40}||{:<20}||{:<15}||{}".format(
                    book_id, info['Title'], info['Author'], info['Release date'], info['Price']
                ))

            # Opsi sorting
            print("\nOpsi Sorting:")
            print("1. Author")
            print("2. Title")
            print("3. Release Date")
            print("4. Price")
            print("0. Kembali")

            sort_option = input("Masukkan pilihan sorting (0-4): ")
            if sort_option == "1":
                self.tampilkan_semua_buku('Author')
            elif sort_option == "2":
                self.tampilkan_semua_buku('Title')
            elif sort_option == "3":
                self.tampilkan_semua_buku('Release date')
            elif sort_option == "4":
                self.tampilkan_semua_buku('Price')
            elif sort_option == "0":
                return
            else:
                print("Pilihan sorting tidak valid. Masukkan angka 0-4.")

    def tampilkan_buku_spesifik(self, book_id):
        if book_id in self.buku:
            info = self.buku[book_id]
            print("{:<5}||{:<40}||{:<20}||{:<15}||{}".format("ID", "Title", "Author", "Release Date", "Price"))
            print("=" * 90)
            print("{:<5}||{:<40}||{:<20}||{:<15}||{}".format(
                book_id, info['Title'], info['Author'], info['Release date'], info['Price']
            ))
        else:
            print(f"Buku dengan ID {book_id} tidak ditemukan.")

    def update_buku(self, book_id, key, value):
        if book_id in self.buku:
            confirm = input(f"Apakah Anda yakin ingin mengupdate data buku dengan ID {book_id}? (Y/N): ").upper()

            if confirm == 'Y':
                if key in self.buku[book_id]:
                    self.buku[book_id][key] = value
                    print(f"Informasi buku dengan ID {book_id} diperbarui.")
                else:
                    print(f"Key '{key}' tidak valid.")
            else:
                print(f"Update data buku dengan ID {book_id} dibatalkan.")
        else:
            print(f"Buku dengan ID {book_id} tidak ditemukan. Kembali ke submenu.")

    def hapus_buku(self, book_id):
        if book_id in self.buku:
            confirm = input(f"Apakah Anda yakin ingin menghapus data buku dengan ID {book_id}? (Y/N): ").upper()

            if confirm == 'Y':
                del self.buku[book_id]
                print(f"Buku dengan ID {book_id} dihapus dari perpustakaan.")
            else:
                print(f"Hapus data buku dengan ID {book_id} dibatalkan.")
        else:
            print(f"Buku dengan ID {book_id} tidak ditemukan.")

    def sewa_buku(self, book_id, weeks, is_member):
        if book_id in self.buku:
            info = self.buku[book_id]
            rental_fee = int(info['Price']) * int(weeks)

            if is_member:
                rental_fee *= (1 - self.membership_discount)

            print("\nDetail Penyewaan:")
            print(f"Title: {info['Title']}")
            print(f"Author: {info['Author']}")
            print(f"Release Date: {info['Release date']}")
            print(f"Rental Fee for {weeks} weeks: {rental_fee}")

            confirm_rent = input("Apakah Anda yakin ingin menyewa buku ini? (Y/N): ").upper()

            if confirm_rent == 'Y':
                print("Penyewaan berhasil. Mohon kembalikan buku tepat waktu.")
                return rental_fee
            else:
                print("Penyewaan dibatalkan.")
                return 0
        else:
            print(f"Buku dengan ID {book_id} tidak ditemukan.")

    def read_menu(self):
        while True:
            print("\nMenu Data Buku:")
            print("1. Tampilkan Semua Buku")
            print("2. Tampilkan Buku Spesifik")
            print("3. Update Buku")
            print("4. Hapus Buku")
            print("5. Sewa Buku")
            print("0. Kembali ke Menu Utama")

            pilihan = input("Masukkan pilihan (0-5): ")

            if pilihan == "1":
                print("\nMenu Sorting:")
                print("1. Tampilkan Semua Buku")
                print("2. Sort by Author")
                print("3. Sort by Title")
                print("4. Sort by Release Date")
                print("5. Sort by Price")
                print("0. Kembali")

                sort_pilihan = input("Masukkan pilihan (0-5): ")
                if sort_pilihan == "1":
                    self.tampilkan_semua_buku()
                elif sort_pilihan == "2":
                    self.tampilkan_semua_buku('Author')
                elif sort_pilihan == "3":
                    self.tampilkan_semua_buku('Title')
                elif sort_pilihan == "4":
                    self.tampilkan_semua_buku('Release date')
                elif sort_pilihan == "5":
                    self.tampilkan_semua_buku('Price')
                elif sort_pilihan == "0":
                    break
                else:
                    print("Pilihan tidak valid. Masukkan angka 0-5.")

            elif pilihan == "2":
                book_id = input("Masukkan ID buku yang ingin ditampilkan: ")
                self.tampilkan_buku_spesifik(book_id)

            elif pilihan == "3":
                book_id = input("Masukkan ID buku yang ingin diperbarui: ")
                key = input("Masukkan key yang ingin diperbarui: ")
                value = input("Masukkan nilai baru: ")
                self.update_buku(book_id, key, value)

            elif pilihan == "4":
                book_id = input("Masukkan ID buku yang ingin dihapus: ")
                self.hapus_buku(book_id)

            elif pilihan == "5":
                book_id = input("Masukkan ID buku yang ingin disewa: ")
                weeks = input("Masukkan berapa minggu Anda ingin menyewa: ")
                is_member = input("Apakah Anda memiliki membership perpustakaan? (Y/N): ").upper() == 'Y'
                rental_fee = self.sewa_buku(book_id, weeks, is_member)
                print(f"Total Payment: {rental_fee}")

            elif pilihan == "0":
                break

            else:
                print("Pilihan tidak valid. Masukkan angka 0-5.")


def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\nMenu Utama:")
        print("1. Data Buku")
        print("2. Tambah Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Sewa Buku")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan (0-5): ")

        if pilihan == "1":
            perpustakaan.read_menu()

        elif pilihan == "2":
            title = input("Masukkan judul buku: ")
            author = input("Masukkan nama pengarang: ")
            release_date = input("Masukkan tahun rilis: ")
            price = input("Masukkan harga buku: ")
            perpustakaan.tambah_buku(title, author, release_date, price)

        elif pilihan == "3":
            book_id = input("Masukkan ID buku yang ingin diperbarui: ")
            key = input("Masukkan key yang ingin diperbarui: ")
            value = input("Masukkan nilai baru: ")
            perpustakaan.update_buku(book_id, key, value)

        elif pilihan == "4":
            book_id = input("Masukkan ID buku yang ingin dihapus: ")
            perpustakaan.hapus_buku(book_id)

        elif pilihan == "5":
            book_id = input("Masukkan ID buku yang ingin disewa: ")
            weeks = input("Masukkan berapa minggu Anda ingin menyewa: ")
            is_member = input("Apakah Anda memiliki membership perpustakaan? (Y/N): ").upper() == 'Y'
            rental_fee = perpustakaan.sewa_buku(book_id, weeks, is_member)
            print(f"Total Payment: {rental_fee}")

        elif pilihan == "0":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 0-5.")


if __name__ == "__main__":
    main()
