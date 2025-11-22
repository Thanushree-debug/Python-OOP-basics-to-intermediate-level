class calculator:
    def add(self,a,b):
        print(a+b)

    def add(self,a,b,c=0):#here c is a optional parameter
        print(a+b+c)

c=calculator()
c.add(1,2)