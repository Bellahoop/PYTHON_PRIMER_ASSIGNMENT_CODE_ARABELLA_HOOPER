class KitchenAppliance:
    def __init__(self, brand, model_number):
        self.model_number = model_number
        self.brand = brand
    
    def report(self):
        print(f"This is the Smart Coffee Machine {self.model_number} from {self.brand}")


class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        super().__init__(brand, model_number)
        self.coffee_menu = coffee_menu
    
    def update_menu(self, new_coffee):
        new_coffee_lower = new_coffee.lower()
        if new_coffee_lower not in [item.lower() for item in self.coffee_menu]:
            self.coffee_menu.append(new_coffee_lower)
            print(f"{new_coffee} has been added to the menu.")
        else:
            print(f"{new_coffee} is already on the menu.")
    
    def make_coffee(self, coffee_type):
        coffee_type = coffee_type.lower()
        if coffee_type in [item.lower() for item in self.coffee_menu]:
            print(f"Making {coffee_type}...")
        else:
            print(f"Sorry, {coffee_type} is not available on the menu.")
            choice = input(f"Do you want to add {coffee_type} to the menu? (yes/no): ")
            if choice.lower() == 'yes':
                self.update_menu(coffee_type)
            else:
                print("Please choose an item from the menu:")
                self.list_menu()

    def list_menu(self):
        print("Menu items:")
        for coffee in self.coffee_menu:
            print("-", coffee)