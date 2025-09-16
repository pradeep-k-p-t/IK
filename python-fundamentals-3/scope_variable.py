def modifier(a,b,c,d): 
    a.append(3)
    b +=4 
    c['a'] = 3 
    d += "world"
    return a,b,c,d

a = [-1]
b = 0 
c ={"test": 1}
d = "hello "
print(f" a = {a},b= {b}, c= {c},d = {d}")
a,b,c,d = modifier(a,b,c,d)
a = [-1]
b = 0 
c ={"test": 1}
d = "hello "
modifier(a,b,c,d)
print(f" a = {a},b= {b}, c= {c},d = {d}")