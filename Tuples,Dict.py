#TUPLES : ordered, non-changeable, can store duplicates
t=("Alisha","Meghaa",45,27.3)
print(t)
print(len(t))
print(t[:])
print(t[2:])
z=("Car")
print(type(z))
z=("Car",)
print(type(z))
s=("Car","Alisha","Meghaa",45,27.3)
#s.append("Oranges")          #gives an error as you can't append tuple
y=list(s)
y.append("Oranges")
y[1]="Scooter"
x=tuple(y)
print(x)

#-----DICT-----#
dictt={
    "name":"Alisha",
    "age":21,
    "vehicle":"Ford Endeavour",
    "fruits":["Litchi","Mango","Oranges"]
}
y=dictt.get("name")
print(y)
x=dictt["vehicle"]
print(x)
print(len(dictt))
print(type(dictt))
dictt["vehicle"]="Activa"
print(dictt)
dictt.update({"name":"Alisha Bhagat"})
dictt["color"]="Blue"
print(dictt)
dictt.pop("fruits")
print(dictt)
dictt.update({"surname":"Bhagat"})
print(dictt)