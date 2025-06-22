class Employee:
    def __init__(self):
        pass

    def work(self):
        print(f'Working.......')
        
        
class Developer(Employee):
    def __init__(self):
        super().__init__()

    def work(self):
        print(f"Writing Code....")
        
Dev1 = Developer()
Dev1.work()