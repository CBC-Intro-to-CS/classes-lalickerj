"""
The assignment:

Make a class called User.

Create two attributes called first_name and last_name, and then create several other attributes (at least 2 more) that are typically stored in a user profile.

Make a method called describe_user() that prints a summary of the user’s information.

Make another method called greet_user() that prints a personalized greeting to the user.

Create 3 instances representing different users, and call both methods for each user.
"""
class User:
    def __init__(self, first_name, last_name, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
    def describe_User(self):
        #Prints out the user's first name, last name, height and their weight
        print(f"The user's first name is {self.first_name}, the last name is {self.last_name}, the user's height is {self.height} and the user's weight is {self.weight}.")

    def greet_User(self):
        #Prints out a personalized greeting to the user.
        print(f"Hello, {self.first_name} {self.last_name}.")

User = User("John", "Laboiski", "6ft", "190lbs")
User.describe_User()
User.greet_User()

