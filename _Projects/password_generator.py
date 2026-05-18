import random
import string

length=int(input("Enter the number:"))

chars=string.ascii_letters+string.digits+string.punctuation
password="".join(random.choice(chars) for _ in range(length))
print("Generated Password:",password)