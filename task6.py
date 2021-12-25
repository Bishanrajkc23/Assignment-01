#Write a Python program to select an item randomly from a list.
import random
alpha = ["11", "12", "a1", "a2", "33", "bb", "cc"]
a = random.randint(0,len(alpha))
print(f"The Randomly selected item  is: {alpha[a]}")