def add(a,b):  
    return a+b
def sub(a,b):
    return a-b
def product(a,b):
    return a*b

def display_menu():
    print("simple calculator")
    print("1.add\n2.substract\n3.product\n4.quit")
    #print("1.add")
    #print("2.sub")
    #print("3.product")
    #print("4.quit")
    #instead of this long format code just try the above short code
while(True):
    display_menu()
    choice = int(input("enter ur choice: "))

    if choice in {1,2,3}: 
        a=int(input("enter a: "))
        b=int(input("enter b: "))

        print(f"you entered {choice}")

    if choice==1:
        print("result: ", add(a,b))

    elif choice==2:
        print("result: ", sub(a,b))

    elif choice==3:
        print("result: ", product(a,b))

    elif choice==4:
        print("exit from calculator")
        break;

    else:
        print("invalid choice plz try again!!")