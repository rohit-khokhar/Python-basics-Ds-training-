
marks = int(input("Enter marks in range (0,100): "))

if marks >= 90:
    print("A+")

elif 80 <= marks <= 89:
    if marks % 5 == 0:
        print("A with bonus")
    else:
        print("A")

elif 60 <= marks <= 79:
    if marks % 2 == 0:
        print("B")
    else:
        print("C")

else:
    print("Fail")
