def print_info(about_me):
    for key, value in about_me.items():
        print(f"My {key.replace('_', ' ')} is {value}.")

about_me = {
    "name": "Arabella",
    "age": "28",
    "occupation": "Project management",
    "location": "Berlin",
    "hobby": "Swimming",
    "language": "German"
}

print_info(about_me)
