s = input("enter password : ")


if len(s) == 6:
     print("weak")

elif (6<len(s)<10 and s.isalpha() == True):
     print("Moderate")


elif (len(s)>10 and s.isalnum() == True) :
     print("strong")

else:
    if any(char in s for char in ('@', '#', '$', '%', '&', '!')):
     print("very strong")

