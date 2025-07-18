num = int(input("enter the elements of list: "))
   

if num%2 == 0:
     print(num**2)

elif num%2 != 0:
     print(num+num)

elif  num%3==0 and num%5==0:
     num = str(num)
     s = num.replace(num,"fizzBuzz")

else:
    print("bye")