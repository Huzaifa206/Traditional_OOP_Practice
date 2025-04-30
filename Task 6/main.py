class Logger:
    def __init__(self):
        print("Logger object has been created.")
    
    def __del__(self):
        print("Logger object has been destroyed.")


log1 = Logger()
del log1  