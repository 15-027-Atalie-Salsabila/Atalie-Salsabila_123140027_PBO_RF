# Mengimpor modul ABC (Abstract Base Class) dan abstractmethod untuk membuat kelas abstrak
from abc import ABC, abstractmethod

# Kelas abstrak Plant sebagai dasar untuk semua jenis tanaman
class Plant(ABC):
    # Konstruktor untuk inisialisasi atribut dasar tanaman
    def __init__(self, name, water_needs, fertilizer_needs):
        self.name = name  # Nama tanaman
        self.water_needs = water_needs  # Kebutuhan air standar (liter)
        self.fertilizer_needs = fertilizer_needs  # Kebutuhan pupuk standar (kg)
        self.adjusted_water_needs = water_needs  # Kebutuhan air yang disesuaikan (dapat berubah berdasarkan kondisi cuaca)
        self.adjusted_fertilizer_needs = fertilizer_needs  # Kebutuhan pupuk yang disesuaikan (default sama dengan standar)

    # Metode abstrak yang harus diimplementasikan oleh subclass
    @abstractmethod
    def grow(self):
        pass

    # Metode untuk menghitung kebutuhan air dan pupuk berdasarkan curah hujan dan kelembaban tanah
    def calculate_needs(self, rainfall, soil_moisture):
        # Mengurangi kebutuhan air jika curah hujan cukup
        if rainfall > 5:  # Jika curah hujan lebih dari 5 mm, kurangi kebutuhan air
            self.adjusted_water_needs = max(0, self.water_needs - (rainfall / 2))
            print(f"Adjusted Water Needs: {self.adjusted_water_needs:.2f} liters (reduced due to rain)")
        else:  # Jika curah hujan rendah, kebutuhan air tetap
            self.adjusted_water_needs = self.water_needs
            print(f"Adjusted Water Needs: {self.adjusted_water_needs:.2f} liters")

        # Kebutuhan pupuk tidak berubah, tetap menggunakan nilai standar
        self.adjusted_fertilizer_needs = self.fertilizer_needs

    # Metode untuk menampilkan kebutuhan pupuk setelah penyesuaian
    def show_needs(self):
        print(f"Adjusted Fertilizer Needs: {self.adjusted_fertilizer_needs:.2f} kg")


# Kelas turunan RicePlant (Tanaman Padi) dari kelas Plant
class RicePlant(Plant):
    # Konstruktor yang menginisialisasi RicePlant dengan kebutuhan air dan pupuk tertentu
    def __init__(self):
        super().__init__(name="Rice", water_needs=20, fertilizer_needs=4)  # Padi butuh 20 liter air dan 4 kg pupuk

    # Implementasi metode grow untuk tanaman padi
    def grow(self):
        print("Rice is growing in the paddy field")


# Kelas turunan CornPlant (Tanaman Jagung) dari kelas Plant
class CornPlant(Plant):
    # Konstruktor yang menginisialisasi CornPlant dengan kebutuhan air dan pupuk tertentu
    def __init__(self):
        super().__init__(name="Corn", water_needs=18, fertilizer_needs=7)  # Jagung butuh 18 liter air dan 7 kg pupuk

    # Implementasi metode grow untuk tanaman jagung
    def grow(self):
        print("Corn is growing in the farm")


# Fungsi untuk mensimulasikan kondisi cuaca dan dampaknya pada tanaman
def simulate_weather(plant, rainfall, soil_moisture):
    plant.grow()  # Memanggil metode grow dari tanaman yang diberikan
    print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")  # Menampilkan laporan cuaca
    plant.calculate_needs(rainfall, soil_moisture)  # Menghitung kebutuhan air dan pupuk berdasarkan cuaca
    plant.show_needs()  # Menampilkan kebutuhan pupuk yang telah disesuaikan


# Bagian utama program yang dijalankan saat file ini dieksekusi langsung
if __name__ == "__main__":
    # Membuat objek RicePlant dan CornPlant
    rice = RicePlant()
    corn = CornPlant()

    # Simulasi cuaca untuk tanaman padi dengan curah hujan 10 mm dan kelembaban tanah 75%
    simulate_weather(rice, rainfall=10, soil_moisture=75)

    print()  # Untuk pemisah output

    # Simulasi cuaca untuk tanaman jagung dengan curah hujan 2 mm dan kelembaban tanah 40%
    simulate_weather(corn, rainfall=2, soil_moisture=40)

