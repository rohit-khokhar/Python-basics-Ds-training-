    #  1
s1 = "Hello WORLD"
print(s1.lower())  


s = "ENGLISH LETTER"
result = ""

for char in s:
    if 'A' <= char <= 'Z': 
        result += chr(ord(char) + 32)
    else:
        result += char

print(result)   

       
#   2
print(s1.upper()) 

s = "english letter"
result = ""

for char in s:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    else:
        result += char

print(result) 

#   3

s1 = "Hello133"
s2 = "Hello12"
print(s1.isalnum())  
print(s2.isalnum())  

s = "Rohit123"
result = True

for char in s:
    if not (
        ('a' <= char <= 'z') or 
        ('A' <= char <= 'Z') or 
        ('0' <= char <= '9')
    ):
        result = False
        break

print(result)  


# 4. 
S = "I love Java"
print(S.replace("Java", "Python"))  

s = "Hello World"
new_string = ""

for char in s:
    if char == 'l':
        new_string += 'x'  
    else:
        new_string += char  

print(new_string)  




# 5. 
Fruit = "apple,banana,grapes"
print(Fruit.split(","))  

s = "hello world"
words = []
word = ""

for char in s:
    if char == " ":
        if word != "":
            words.append(word)
            word = ""
    else:
        word += char

if word:
    words.append(word)

print(words)  


# 6. 
str = "###Python###"
print(str.strip('#'))  

s = "   Hello World   "

start = 0
end = len(s) - 1


while start < len(s) and s[start] == ' ':
    start += 1

while end >= 0 and s[end] == ' ':
    end -= 1

if start <= end:
    result = s[start:end+1]
else:
    result = ""  

print(f"'{result}'")  


# 7. 
c = "Python programming is fun. Programming is creative."
print(c.count("programming"))  
print(c.lower().count("programming")) 


s = "python"
target = "a"
counter = 0

for char in s:
    if char == target:
        counter += 1

print(counter)  


# 8. 
text = "open the door"
print(text.startswith("open")) 

s = "hello world"
prefix = "hello"
is_start = True

if len(prefix) > len(s):
    is_start = False
else:
    for i in range(len(prefix)):
        if s[i] != prefix[i]:
            is_start = False
            break

print(is_start)  





# 9. 
text2 = "report.pdf"
print(text2.endswith(".pdf"))  

s = "hello world"
suffix = "world"
is_end = True

if len(suffix) > len(s):
    is_end = False
else:
    for i in range(1, len(suffix) + 1):
        if s[-i] != suffix[-i]:
            is_end = False
            break

print(is_end)  



# 10. 
stat1 = "HelloWorld"
stat2 = "Hello123"


print(stat1.isalpha())  
print(stat2.isalpha())    


s = "Rohit"
result = True

for char in s:
    if not (
        ('a' <= char <= 'z') or 
        ('A' <= char <= 'Z') 
    ):
        result = False
        break

print(result)  # Output: True

