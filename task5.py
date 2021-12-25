#Write a Python program to print a specified list after removing the 4th elements.
data1 = ["11", "12", "a1", "a2", "33", "bb", "cc"]
data2 = []
for i in range(len(data1)):
    if i == 4:
        continue
    else:
        data2.append(data1[i])
print(data2)