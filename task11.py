#Write a Python program to remove an item from a set if it is present in the set.
inte = {1, 2, 3, 4, 5}
q = int(input("Enter a number to remove from set if it is present: "))
w = 0
for item in inte:
    if item == q:
        inte.remove(q)
        print(f"The Modified set after removing {q} is : {inte}")
        break
    else:
        w = w+1
if w == len(inte):
    print(f"{q} is Not found in Set : {inte}")