# lis=[1,2,3]
# lis.append(5)
# print(lis)
# lis.append(6)
# print(lis)

dictt={}
print(type(dictt))
dictt.update({"Shreejan":"Shrestha"})

dictt.update({"Sajana":"MUM"})
dictt.update({"Shreejan":"Daddy","Shristi":"Buri","puntu":"laley"})
print(dictt)

user=input(":")

# if user == dictt.keys():
#     print("xa")
# else:
#     print("xaina")



for keys in dictt.keys():
    if user==keys:
        print("xa")
        print(dictt.get(user))
        break
else:
    print("Xaina")

