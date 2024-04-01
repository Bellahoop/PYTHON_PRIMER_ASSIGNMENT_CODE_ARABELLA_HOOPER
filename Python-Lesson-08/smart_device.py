class SmartDevice:

    def __init__(self, model_number, product_type, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.product_type = product_type
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print(f"This is {self.model_number} {self.product_type} from {self.brand} with a screen size of {self.screen_size} inches.")

    def install_app(self, app_name=None):
        if app_name is None:
            print("Please provide an app name.")
            return

        if app_name not in self.app_list:
            print(f"Installing {app_name}...")
            self.app_list.append(app_name)
            return self.app_list
        else:
            print(f"{app_name} is already installed on your {self.product_type}.")

    def delete_app(self, app_name):
        if app_name in self.app_list:
            print(f"Deleting {app_name}...")
            self.app_list.remove(app_name)
            return self.app_list
        else:
            print(f"{app_name} is not installed on your {self.product_type}.")