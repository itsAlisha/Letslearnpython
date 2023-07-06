#For tasks like these :
'''
fruits=['apple','mango','banana','kiwi','litchi','pineapple']
newfruits=[]
for x in fruits:
    if "i" in x:
        newfruits.append(x)
print(newfruits)
'''

fruits=['apple','mango','banana','kiwi','litchi','pineapple']
newfruits=[x for x in fruits if "a" in x]
print(newfruits)
newfruits=[x for x in range(0,4)]
print(newfruits)
newfruits=[x for x in fruits if x!='kiwi']
print(newfruits)
newfruits=[x for x in range(10) if x<6]
print(newfruits)
newfruits=[x.upper() for x in fruits]
print(newfruits)
newfruits=[x.upper() if x!='banana' else 'orange' for x in fruits]
print(newfruits)
newfruits=[x if x!='litchi' else 'Papaya' for x in fruits]
print(newfruits)
