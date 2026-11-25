# CLI PASSWORD STRENGTH AUDITOR

# gmail=input("Enter Email:").strip().lower()

# if len(gmail)<8:
#     print("too short: must be at least 8 characters.");

# elif '@' in gmail and gmail.endswith((".com",".in")):
#     print("Valid Email.")
# else:
#     print("Invalid Email.");

# password=input("Enter password:")
# has_digit=False
# has_upper=False

# if len(password)>=8:
#     for char in password:
#         if char.isdigit():
#             has_digit=True
#         elif char.isupper():
#             has_upper=True
#         if has_digit and has_upper:
#             break

# if has_digit and has_upper:
#     print("Strong Password")
# else:
#     print("Week Password")


def check_password(password):
    issues=[]
    if len(password)<8:
        issues.append("at least 8 characters")
    
    has_digit=any(char.isdigit() for char in password)
    has_upper=any(char.isupper() for char in password)
    has_symbol=any(not char.isalnum() for char in password)
    
    if not has_digit:
        issues.append("a number")
    if not has_upper:
        issues.append("an uppercase letter")
    if not has_symbol:
        issues.append("a special symbol")

    return "Strong Password." if not issues else "Week Password.\n Missing:"+",".join(issues)

attempt=0
for attempt in range(3):
    pwd=input("Enter The Password: ")
    status=check_password(pwd)
    print(status)
    if status=="Strong Password.":
        print("Account Created Successfully!")
        break
else:
    print("Too Many failed Attempts. LOKED.")

    