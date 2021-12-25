#Write a Python script to concatenate following dictionaries to create a new one.
dic= {10:20, 20:30}
dic1= {30:40, 40:50}
dic2= {50:60,60:70}
dic3 = {}
for i in (dic,dic1,dic2):
    dic3.update(i)
print(f"The New Dictionary after concatenate {dic} , {dic1} & {dic2} is: {dic3}")