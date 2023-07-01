'''
Hi, i am not a string
'''

x="""
Hi 
i
am
multi-line
string
"""
print(x)
print(type(x))
print(len(x))
print("am" in x)
print("song" in x)
print(x[3:])

print(x.upper())
print(x.lower())
print(x.swapcase())
print(x.title())
print(x.capitalize())
y="   alisha   "
print(y.capitalize())
print(y[1:5])
print(y[-5:-2])
print(y.rstrip())
print(x[1])
print(y.replace("a","k"))
print(y.split("h"))
x='hello'
y='world'
z=x+y
print(z)
print("Today is an awesome \bday")
print("Today is an awesome \nday")
print("Today is an awesome \rday")
print("Today is an awesome \tday")
print("Today is an \"awesome\" day")
print("Today\'s an awesome day")
print("Today is an awesome \fday")
txt="\110\145\154\154\157"
print(txt)
_txt2="\\\\"
print(_txt2)
_txt="\x48\x65\x6c\x6c\x6f"
print(_txt)
