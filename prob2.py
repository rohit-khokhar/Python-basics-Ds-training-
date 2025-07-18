n = int(input("enter n : "))

if n%2 == 0:
    print("Even")
    revstr = str(n)[::-1]
    print(revstr)

else:
    print("No even digits")


