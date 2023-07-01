
list=["apple","mango","cherry"]
def loop(x):
    for x in list:
        print(3*x)

loop(list)
#----------------------------------------#
list2=["car","bike","scooter","plane"]
def func1(y):
    print(4*y)

def func2(p1,p2):
    for items in p2:
        p1(items)                 #list 2 ke items pe func1 run krde

func2(func1,list2)                #func1 passed as parameter

#----------------------------------------#
#LIST : ordered, changeable, can store duplicates
list=["Alisha",21,"Scooter",True,5]
print(list)
print(len(list))
print(type(list))
print(list[4])
print(list[2:4])   #excludes last in range
list[2]="Car"
print(list)
list[3:5]=[False,10]
list.append("Oranges")
print(list)
list.remove("Oranges")
print(list)
list.insert(1,"Bhagat")
print(list)
