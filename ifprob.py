
num = int(input("Enter a number between 1 and 999: "))

if 10 <= num <= 99 and num % 2 == 0:
    print("Even double digit number")

elif 100 <= num <= 999 and num % 2 != 0:
    print("Odd triple-digit number")

elif num in [2, 3, 5, 7]:
    print("Single digit prime number")

else:
    print("Doesn't match any category")
