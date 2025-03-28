import random

jokes=[
    "***Why did the astronaut break up with his girlfriend? Because he needed space.***",
    "***Why did the banana go to the doctor? Because he was not peeling well.***",
    "***What do you call a group of cows playing instruments? A moo-sical band.***",
    "***Why did the computer go to the doctor? Because it had a virus.***",
    "***Why did the mushroom go to the party? Beacuse he was a fun-gi.***",
    "***What do you call an opener that does not work? A can't opener.***",
    "***Why did the bicycle could not stand by itself? Beacuse it was two-tired.***",
    "***What do you call a fake noodle? An impasta.***",
    "***Why did the scarecrow win an award? Because he was outstanding in his field.***"
    ]

print("************************************************")
print("This is A Random Joke Generator")
print("************************************************")
input("Press enter to get a joke: ")
play=True
while play:
    print(random.choice(jokes))
    play=input("Press enter to get one more joke or press 'q' and enter to quit: ").lower()!='q'
print("Thanks for playing! I hope we made you smile")

