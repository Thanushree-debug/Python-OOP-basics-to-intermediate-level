class database:
    def __init__(self):
        self.storage={} #opening a kaali dictionary

    def write(self,key,value):
        self.storage[key]=value

    def read(self,key):
        if key in self.storage:
            print(self.storage[key])
        else:
            print("db not avlble")

db=database()
#db.read("chandan")  #i can put this also but i wont get any output
db.write("subscribers","100k")
print(db.storage)

#only db.storage means it will show the info to everyone
#but if i give db.__storage it wont give info to everyone only writer of code can see the info but only inside the code
print(db.__storage)

