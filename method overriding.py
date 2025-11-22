class animal:#parent
    def make_sound(self):
        print("animal is making sound")

class dog(animal):#child
    def make_sound(self):
        super().make_sound()#if i use this line then it is super function and without this line it is method over_riding
        print("bark")

d=dog()
d.make_sound()
