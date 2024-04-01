from smart_device import SmartDevice

device_a = SmartDevice("Series 9", "Apple Watch", 'Apple', 1.6)

device_a.report()

print("\nDevice Information:")
print("Model:", device_a.model_number)
print("Product Type:", device_a.product_type)
print("Brand:", device_a.brand)
print("Screen Size:", device_a.screen_size)

apps_for_device_a = ["Activity", "Blood Oxygen", "Handwashing", "Walkie-Talkie"]

print("\nTesting the install app method:")
print()

for app_name in apps_for_device_a:
    print(f"Attempting to install {app_name}...")
    device_a.install_app(app_name)
    print(f"Current app list: {device_a.app_list}")
    print()

print("\nTesting the delete app method:")
print()

for app_name in ["Activity", "Blood Oxygen", "Clock"][:3]:  
    print(f"Attempting to delete {app_name}...")
    device_a.delete_app(app_name)
    print(f"Current app list: {device_a.app_list}")
    print()

print("\nFinal app list:", device_a.app_list)