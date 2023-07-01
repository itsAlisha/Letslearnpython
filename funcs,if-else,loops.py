
a=34
b=33
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")

print("a is greater than b") if a>b else print("b is greater than a")

a=32
b=33
if a>b or a%2==0:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")
def trialfunc(x,y="World"):
    print(x+" "+y)

trialfunc("Hello","Girl")

numbers=[1,2,3,4,77,88,99,100]
for x in numbers :
    print(x)
    if x==4:
        break

print("\n")

L = [1, 2, 3, 4, 77, 88, 99, 100]
for y in L:
    if y==77:
        continue
    print(y)     #correct indentation would lead to correct answer

z="Fruits"
for t in z:
    if t=='i':
        continue;
    print(t)

for m in range(50,100):
    print((m+1)%2)

print("\n")
i=1
while i<6:
    print(i)
    i += 1
    if i==3:
        break
print("\n")
j=1
while j<6:
    print(j)
    j += 1
    if j==3:
        continue
