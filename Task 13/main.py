class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  

    def start_car(self):
        print("Starting the car...")
        self.engine.start()


engine1 = Engine()
car1 = Car(engine1)
car1.start_car()
