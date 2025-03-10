import os
import json

# Nama file untuk menyimpan data mahasiswa
FILENAME = 'mahasiswa.txt'

# Fungsi untuk memuat data dari file
def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return {}

# Fungsi untuk menyimpan data ke file
def save_data(students):
    with open(FILENAME, 'w') as file:
        json.dump(students, file)

# Fungsi untuk menampilkan menu
def display_menu():
    print("\n==== SISTEM PENGELOLAAN DATA MAHASISWA ====")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa Berdasarkan NIM")
    print("4. Edit Data Mahasiswa")
    print("5. Hapus Data Mahasiswa")
    print("6. Simpan ke File")
    print("7. Keluar")
    print("===========================================")

# Fungsi untuk menambah mahasiswa
def add_student(students):
    nim = input("Masukkan NIM: ")
    if nim in students:
        print("NIM sudah ada. Silakan gunakan NIM yang berbeda.")
        return
    name = input("Masukkan Nama: ")
    nilai = input("Masukkan Nilai: ")
    students[nim] = {"nama": name, "nilai": nilai}
    print("Mahasiswa berhasil ditambahkan!")

# Fungsi untuk menampilkan semua mahasiswa
def display_students(students):
    if not students:
        print("Tidak ada data mahasiswa.")
        return
    print("\n==== DATA MAHASISWA ====")
    print("NIM      | Nama  | Nilai")
    print("-------------------------")
    for nim, data in students.items():
        print(f"{nim}  | {data['nama']} | {data['nilai']}")

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def search_student(students):
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in students:
        data = students[nim]
        print(f"Data Mahasiswa:\nNIM: {nim}\nNama: {data['nama']}\nNilai: {data['nilai']}")
    else:
        print("Mahasiswa tidak ditemukan.")

# Fungsi untuk mengedit data mahasiswa
def edit_student(students):
    nim = input("Masukkan NIM yang ingin diedit: ")
    if nim in students:
        name = input("Nama baru (kosongkan jika tidak ingin mengubah): ")
        nilai = input("Nilai baru (kosongkan jika tidak ingin mengubah): ")
        if name:
            students[nim]['nama'] = name
        if nilai:
            students[nim]['nilai'] = nilai
        print("Data berhasil diperbarui!")
    else:
        print("Mahasiswa tidak ditemukan.")

# Fungsi untuk menghapus data mahasiswa
def delete_student(students):
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in students:
        del students[nim]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Mahasiswa tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def main():
    students = load_data()
    
    while True:
        display_menu()
        choice = input("Pilihan: ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            edit_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            save_data(students)
            print(f"Data mahasiswa telah disimpan dalam file '{FILENAME}'")
        elif choice == '7':
            save_data(students)
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()