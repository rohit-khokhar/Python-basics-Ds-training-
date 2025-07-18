
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))

if type(a) == int and type(b) == int:
    mul = a * b
    print("Multiplication:", mul)
    if mul % a == 0 and mul % b == 0:
        print("Result is divisible by both inputs")

elif type(a) == str and type(b) == str:
    add = a + b
    print("Concatenation:", add)
    
    # Check if first characters are same
    if a[0] == b[0]:
        print("First letter is the same")

elif type(a) == int and type(b) == str:
    repeat = a * b
    print("Repeated string:", repeat)

elif type(a) == str and type(b) == int:
    repeat = b * a
    print("Repeated string:", repeat)



