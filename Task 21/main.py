import time

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            time.sleep(1)  #  1-second delay
            return value

try:
    num = int(input("Enter a number to count down from: "))
    print("Countdown:")
    for i in Countdown(num):
        print(i)
except ValueError:
    print("Please enter a valid number.")
