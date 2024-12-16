import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"
        
        def __str__(self):
            return f"name : {self.name}\nprice : {self.price}\ndescription : {self.description()}"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        self.counter = 0 

    def repair(self):
        self.counter = 0
        return "This coffee machine has been repaired."

    def serve(self, drink: HotBeverage) -> HotBeverage:
        if self.counter >= 10:
            raise CoffeeMachine.BrokenMachineException()
        self.counter += 1
        if random.randint(0, 5) == 1:
            return CoffeeMachine.EmptyCup()
        return drink

def machine():
    coffee_machine = CoffeeMachine()
    beverages = [Coffee(), Tea(), Chocolate(), Cappuccino()]
    print("Welcome to the Coffee Machine!")
    
    for index in range(12):
        try:
            beverage = random.choice(beverages)
            print(index + 1)
            print("Trying to Serve", str(beverage))
            served_beverage = coffee_machine.serve(beverage)
            print("Served", str(served_beverage))
        except CoffeeMachine.BrokenMachineException as e:
            print()
            print("Error", str(e), "Repairing...")
            repair_message = coffee_machine.repair()
            print("", repair_message)
            print("Coffee Machine is ready to serve!")
        print()

if __name__ == "__main__":
    machine()