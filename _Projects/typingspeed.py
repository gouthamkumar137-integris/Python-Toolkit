import time

text = "Python makes automation easy"

print("Type this:")
print(text)

input("Press Enter to start...")

start = time.time()

typed = input("\nType here: ")

end = time.time()

time_taken = end - start
wpm = len(typed.split()) / time_taken * 60

print(f"\nTime: {time_taken:.2f} sec")
print(f"WPM: {wpm:.2f}")

if typed == text:
    print("Perfect typing!")
else:
    print("Some mistakes made.")