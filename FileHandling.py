#4 Modes : Read, Write, Create, Append
f=open("trial.txt","r")
f.close()
#print(f.read())
# print(f.read(1))
# print(f.read(2))
# print(f.read(30))
# print(f.readline())       #prints single line
# print(f.readline())
# print(f.readline())
# print(f.readline())
# for x in f:               #prints all lines with spaces
#     print(x)
# f.close()
# print("File closed successfully")

#To write in File :
# f2=open("trial.txt","a")
# f2.write(" A new line ")
# f2.close()
# f2=open("trial.txt","r")
# print(f2.read())
# f2.close()

#To re-write in File :
# f3=open("trial.txt","w")
# f3.write("Completely new now")
# f3.close()
# f3=open("trial.txt","r")
# print(f3.read())

#create new file
# f4=open("newfileee.txt","x")       #Steps : Create->Write->Close->Open->Read->Close
# f4=open("newfileee.txt","w")
# f4.write("Abra ca dabra")
# f4.close()
# f4=open("newfileee.txt","r")
# print(f4.read())
# f4.close()

#Remove using OS
# import os
# os.remove("newfileee.txt")

# import os
# if os.path.exists("newfileee.txt"):
#     os.remove("newfileee.txt")
# else:
#     print("File not present")

