#Write a Python script to check if a given key already exists in a dictionary.
a = input("Enter a key to remove from Dictionary if it is present: ")
inte = {"first": 1, "second": 2, "third": 3, "fourth": 4, "eighty": 80}
b = 0
for key,value in inte.items():
    if key == a:
        print(f"{a} already exist as key in dictionary {inte}")
        break
    else:
        b = b+1
if b == len(inte):
    print(f"{a} is Not found in Dictionary : {inte}")