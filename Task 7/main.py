class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public variable
        self._salary = salary    # Protected variable
        self.__ssn = ssn        # Private variable

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")


emp = Employee("John", 50000, "123-45-6789")
emp.display()

print("")
print("Accessing all three variables from an object:")
# Accessing public and protected variables
print(emp.name)     
print(emp._salary)  

# we cant access private variable directly
# print(emp.__ssn)  
