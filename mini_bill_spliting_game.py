import random

print(f"Welcome to the Game!\nwho pay the bill?")
friends=[]
friends=input("Write your names, separated by spaces:").split()

random_names=random.choice(friends)
chiceing_name=friends.index(random_names)
print(f"{friends[chiceing_name]} you are paying off !")






