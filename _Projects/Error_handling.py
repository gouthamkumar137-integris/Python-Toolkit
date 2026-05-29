def DivExp(a,b):
    assert a>0, "Error: 'a' must be greater than 0"
    if b==0:
        raise ZeroDivisionError("Error: Divide by Zero!!!")
    return a/b

try:
    a=float(input("Enter the First no. (Numerator):"))
    b=float(input("Enter the Second no. (Dinominator):"))
    result=DivExp(a,b)
    print(f"Result:\t{a}/{b}={result}")

except AssertionError as ae:
    print(ae)
except ZeroDivisionError as zde:
    print(zde)
except ValueError:
    print("Error: Invalid input please recheck.")
except Exception as e:
    print("Unexpected Error Occured:",e)


