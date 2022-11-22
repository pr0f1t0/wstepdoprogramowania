sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
l = ["name", "age", "fff"]
d1 = {}

for i in l:
 if i in sample_dict:
  d1[i] = sample_dict[i]
  #print(d1)
 else:
  print("Nie ma takiego klucza!")

"""for i in d1.values():
 if i in sample_dict:
  del d1[i]"""

for i in l:
 x = sample_dict.pop(i, "error")
 print(x)

"""for i in sample_dict.values():
 if i == "Jones":
  print("yes")
  break
 else:
  print("no")"""

if "Jones" in sample_dict.values():
 print("yes")
else:
 print('no')











#for k,v in sample_dict.items():
 #print(f"{k:<10} = {v:>10}")



#for key in sample_dict.keys():
 #print(f"{key:<10} = {sample_dict[key]:>10}")

