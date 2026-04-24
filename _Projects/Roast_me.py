import random
print("Hi, I’m RoastBot 😈… type something")

study_keywords=['study','read','learn','exam','revision']
reels_keywords=['reel','video','instagram','youtube','scroll',"waste"]
gym_keywords=['gym','workout','exercise','run']

study_roasts = [
"Oh studying? Miracle happening today?",
"Books opened, brain still closed?",
"Let me guess… 5 mins study, 2 hours break?"
]

reels_roasts=['Scrolling again? Your future is crying.',
'Instagram knows you better than your parents.',
'Thumb workout > real workout huh?']


while True:
    text=input("\nYou:").lower()

    if text =="exit":
        print("RoasBot: Running away already? 😏")
        break

    words=text.split()
    category=None

    for word in words:
        if word in study_keywords:
            category='study'
            break
        elif word in reels_keywords:
            category='reels'
            break
        elif word in gym_keywords:
            category="gym"
            break
    if category is None:
        category="general"

    if category=='study':
    study=['huu']



        


        