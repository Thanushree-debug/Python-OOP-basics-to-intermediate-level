class user:
    def __init__(self,username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in")

        

'''class admin:
    def __init__(self):
        self.username = username
        self.__password = password'''
#if i wirte code like above without using administrator
#i have to write a long code repeating many steps
#soo instead try using inheritance like below code
class admin(user):
    def delete_user(self):
        print("admin deleted the user")

a = admin("karnataka hudugi")
print(a.username)
a.login()
a.delete_user()