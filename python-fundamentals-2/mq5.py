
set1={2,5,3}
set2={3,1}
set3={}

print(set1 & set2)
print(set1 | set2)
#everythign that is unqiue to set 1 wrt set2 
print(set1 - set2)
set_xor = (set1 | set2) - (set1 & set2) 
print(set_xor)
set_xor = set1 ^ set2 
print(set_xor)

listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']

listOne.extend(listTwo)
print(listOne)