class BankAccount:
    # Kurs tetap untuk konversi mata uang
    exchange_rates = {
        'USD': 1.0,  # USD ke USD
        'EUR': 1.1,  # EUR ke USD
        'IDR': 0.000067  # IDR ke USD
    }

    def __init__(self, account_holder, balance, currency):
        # Inisialisasi atribut akun
        self.account_holder = account_holder  # Pemegang akun
        self.balance = balance  # Saldo akun
        self.currency = currency  # Mata uang akun

    def __add__(self, amount):
        # Menambahkan saldo dengan jumlah yang diberikan (dalam mata uang yang sesuai)
        if isinstance(amount, tuple):
            amount_value, amount_currency = amount
            converted_amount = amount_value * self.exchange_rates[amount_currency] / self.exchange_rates[self.currency]
            self.balance += converted_amount
        else:
            self.balance += amount
        return self.balance

    def __sub__(self, amount):
        # Mengurangi saldo dengan jumlah yang diberikan (dalam mata uang yang sesuai)
        if isinstance(amount, tuple):
            amount_value, amount_currency = amount
            converted_amount = amount_value * self.exchange_rates[amount_currency] / self.exchange_rates[self.currency]
            if self.balance >= converted_amount:
                self.balance -= converted_amount
            else:
                print("Insufficient balance for withdrawal!")
        else:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient balance for withdrawal!")
        return self.balance

    def apply_interest(self):
        # Menghitung dan menerapkan bunga tahunan berdasarkan saldo
        if self.balance < 5000:
            interest_rate = 0.01  # 1% untuk saldo di bawah $5000
        else:
            interest_rate = 0.02  # 2% untuk saldo di atas $5000
        
        interest = self.balance * interest_rate
        self.balance += interest
        print(f"Applying interest... New Balance = {self.balance}")

    def check_balance(self):
        # Memeriksa saldo dan memberikan peringatan jika saldo rendah
        if self.balance < 1000:
            print("Low Balance Warning")
        print(f"{self.account_holder}'s Account: Balance = {self.balance} {self.currency}")


# Contoh penggunaan
# Akun John
john_account = BankAccount("John", 5000, "USD")
print(f"John's Account: Initial Balance = {john_account.balance} {john_account.currency}")
john_account.apply_interest()  # Menerapkan bunga

# Akun Emily
emily_account = BankAccount("Emily", 1000, "EUR")
print(f"\nEmily's Account: Initial Balance = {emily_account.balance} {emily_account.currency}")

# Mengonversi saldo Emily ke USD dan mencoba menarik $1200
converted_amount = emily_account.balance * BankAccount.exchange_rates['EUR']  # Mengonversi €1000 ke USD
print(f"Converted to USD: ${converted_amount}")

withdrawal_amount = (1200, 'USD')  # Menarik $1200
emily_account - withdrawal_amount  # Mencoba menarik uang

# Memeriksa saldo akhir
emily_account.check_balance()  # Memeriksa saldo akhir