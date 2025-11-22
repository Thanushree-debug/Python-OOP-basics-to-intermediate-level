class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private attribute

    def get_username(self):
        return self.username

    def check_password(self, password):
        return password == self.__password

user = User("dev_karnataka", "pass1234")
print(user.get_username())  # Access allowed
print(user.check_password("wrong_pass"))  # Returns False
print(user.check_password("pass1234"))  # Returns True