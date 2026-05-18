a=float(input("Enter the First number:"))
b=float(input("Enter the Second number:"))
while True:
    print("\n---Operation Menu---")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter your choice(1-5):"))
    if choice==5:
        print("exiting...")
        break
    elif choice==1:
        print(f"Addition of two numbers:\n{a}+{b}=",a+b)
    elif choice==2:
        print(f"Substraction of two numbers:\n{a}-{b}=",a-b)
    elif choice==3:
        print(f"Multiplication of two numbers:\n{a}*{b}=",a*b)
    elif choice==4:
        if b!=0:
            print(f"Division of two numbers:\n{a}/{b}=",a/b)
        else:
            print("Error: value of 'b' must be greater than zero")
    else:
        print("Invalid Input!!!")
    