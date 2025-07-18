st = input("enter a string : ")
pr = set()

for i in st:
    if i not in pr:
      print(i, st.count(i))
      pr.add(i)



   


