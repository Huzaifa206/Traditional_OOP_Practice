class Counter:
    count = 0  # Class variable

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.display_count()
