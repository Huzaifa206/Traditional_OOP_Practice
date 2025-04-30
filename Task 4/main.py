class Bank:
    bank_name = "Name of Bank"  

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")


b1 = Bank("Huzaifa")
b2 = Bank("Ali    ")

b1.display()
b2.display()

Bank.change_bank_name("Changed Name of Bank")

b1.display()
b2.display()
