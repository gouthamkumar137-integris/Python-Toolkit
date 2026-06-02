import random
def play_game():
    
    count=0
    print("Guess number between 1 to 100\n")
    key=random.randint(1,100)
    while True:
        try:
            number=int(input("Enter your guess (1-100): "))
            if number<1 or number>100:
                raise ValueError("Please enter a numbeer between 1 and 100.")
            count+=1
            if number==key:
                print("Correct!\n")
                break
            elif key>number:
                print("hint: key is greater than what you guessed.\n")
            elif key<number:
                print("hint: key is lower than what you guessed.\n")
        except ValueError as ve:
            print(ve)
        
        except Exception as e:
            print("Unexpected Error Occured: ",e)
        
    print("You guessed in ",count ,"attempts.")
while True:
    play_game()
    choice=input("Play again? (y/n) ").lower()
    if choice=='n':
        break
    