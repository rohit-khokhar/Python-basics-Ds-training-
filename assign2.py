
dict_like = [("name", "Alice"), ("age", 25), ("city", "Delhi")]

def get_value(key):
    for k, v in dict_like:
        if k == key:
            return v
    return None  

def set_value(key, value):
    for i in range(len(dict_like)):
        if dict_like[i][0] == key:
            dict_like[i] = (key, value)
            return
    dict_like.append((key, value)) 

print(get_value("name"))   
set_value("age", 30)
set_value("country", "India")
print(dict_like)
  