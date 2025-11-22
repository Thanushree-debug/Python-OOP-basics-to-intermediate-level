class book:
    def __init__ (self,title,author):
        self.title=title
        self.author=author

    def info(self):
        print(f"TITLE={self.title} , AUTHOR={self.author}")

book1=book("pyt prgm" , "thanu")
book2=book("machine learning" , "chandan")

book1.info()
book2.info()

#if any value we dont know 
#it means i know only pyt prg book name and i dont know the author name so in that case follow the below code

class book:
    def __init__ (self,title,author="unknown"):
        self.title=title
        self.author=author

    def info(self):
        print(f"TITLE={self.title} , AUTHOR={self.author}")

book1=book("pyt prgm")
book2=book("machine learning" , "chandan")

book1.info()
book2.info()