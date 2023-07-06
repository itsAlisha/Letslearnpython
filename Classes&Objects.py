#PYTHON is an object oriented programming Language
''' Simplest example of Class and Object
class Human:
    x=5

h1=Human()
print(h1.x)
'''
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def methods(self):
        print("Hi, my name is "+self.name)
        print("I am "+str(self.age)+" years old")

h1=Human("Sherlock",6)
h1.methods()
h2=Human("Alisha",21)
h2.methods()
print(h1.name)
print(h2.age)

del h1
print("h1 deleted successfully")
#h1.methods()              #Gives error because it is deleted
h2.name="Rahul"            #re-write values
h2.age=50
h2.methods()

class hermoine:
    pass               #Empty class

#class harrypotter:
     #gives an error
