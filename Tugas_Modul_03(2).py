class Employee: ## Kelas induk Employee yang mendefinisikan atribut dan metode dasar untuk semua karyawan
    def __init__(self, name, role, hours_worked, task_completed): # Inisialisasi atribut karyawan
        self.name = name # Nama karyawan
        self.role = role  # Peran karyawan
        self.hours_worked = hours_worked  # Jam kerja karyawan
        self.task_completed = task_completed # Jumlah tugas yang diselesaikan

    # Metode ini diimplementasikan oleh kelas turunan
    def work(self):
        raise NotImplementedError("Subclasses should implement this method.")

    # Metode untuk mengevaluasi performa karyawan berdasarkan jam kerja dan tugas yang diselesaikan
    def evaluate_performance(self):
        if self.hours_worked == 0:
            return "No Performance" # Jika tidak ada jam kerja, tidak ada performa
        
         # Menghitung rasio antara tugas yang diselesaikan dan jam kerja
        performance_ratio = self.task_completed / self.hours_worked
        
        # Menentukan rating performa berdasarkan rasio
        if performance_ratio > 2:
            return "High Performance" # Performa tinggi jika rasio lebih dari 2
        elif performance_ratio > 1:
            return "Medium Performance" # Performa sedang jika rasio lebih dari 1
        else:
            return "Low Performance" # Performa rendah jika rasio 1 atau kurang


# Kelas turunan untuk Software Engineer
class SoftwareEngineer(Employee):
    def work(self):
        return f"{self.name} (Software Engineer) is coding." # Mengembalikan string yang menjelaskan pekerjaan Software Engineer


class DataScientist(Employee): # Kelas turunan untuk Data Scientist
    def work(self):
        return f"{self.name} (Data Scientist) is analyzing data."  # Mengembalikan string yang menjelaskan pekerjaan Data Scientist


class ProductManager(Employee): # Kelas turunan untuk Product Manager
    def work(self):
        return f"{self.name} (Product Manager) is managing the product roadmap."  # Mengembalikan string yang menjelaskan pekerjaan Product Manager


# Contoh penggunaan membuat daftar karyawan dengan berbagai jam kerja dan tugas yang diselesaikan
employees = [
    SoftwareEngineer("Alice", "Software Engineer", 5, 12), #karyawan1
    DataScientist("Bob", "Data Scientist", 8, 5), #karyawan2
    ProductManager("Charlie", "Product Manager", 6, 4), #karyawan3
    SoftwareEngineer("David", "Software Engineer", 10, 5) #karyawan4
]

for employee in employees:
    print(employee.work()) # Memanggil metode work() untuk mencetak deskripsi pekerjaan
    print(f"Performance Rating: {employee.evaluate_performance()}\n") #mencetak performa