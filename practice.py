class User:
    def __init__(self, first_name, last_name, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}, the user's height is {self.height}, the user's weight is {self.weight}.")
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}.")