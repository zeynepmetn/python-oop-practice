class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.__account_number = account_number
        self.__balance = balance
        self.__customer_name = customer_name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_customer_name(self, new_name):
        self.__customer_name = new_name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} TL yatırıldı. Güncel bakiye: {self.__balance}")
        else:
            print("Yatırılacak para miktarı geçersiz.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} TL çekildi. Güncel bakiye: {self.__balance}")
        else:
            print("Çekilecek para miktarı geçersiz.")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, customer_name,
                 withdraw_limit=2000, deposit_limit=5000):
        super().__init__(account_number, balance, customer_name)
        self.withdraw_limit = withdraw_limit
        self.deposit_limit = deposit_limit

    def deposit(self, amount):
        if 0 < amount <= self.deposit_limit:
            super().deposit(amount)
        else:
            print(f"Yatırılacak miktar {self.deposit_limit} TL limitini aşıyor.")

    def withdraw(self, amount):
        if 0 < amount <= self.withdraw_limit:
            super().withdraw(amount)
        else:
            print(f"Çekilecek miktar {self.withdraw_limit} TL limitini aşıyor.")


class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, customer_name, interest_rate=0.02):
        super().__init__(account_number, balance, customer_name)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            super().deposit(amount)
            print(f"Faiz oranı: %{self.interest_rate * 100}")
        else:
            print("Yatırılacak para miktarı geçersiz.")

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"{interest} TL faiz eklendi.")

acc1 = CheckingAccount("123", 3000, "Zeynep")
acc1.deposit(1000)
acc1.withdraw(500)

acc2 = SavingAccount("456", 5000, "Elif")
acc2.apply_interest()

