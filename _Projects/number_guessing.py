import random

while True:
    key=random.randint(1,10)
    try:
        number=int(input("Enter number (1-10): "))
        if number==key:
            print("Good guessing")
        else:
            print("Correct number is: ",key)
    except ValueError:
        print("Invalid value!!!")