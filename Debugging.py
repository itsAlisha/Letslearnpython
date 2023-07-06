import random
def GenerateRandom(upper):
    r=random.randint(1,upper)
    return r

def main():
    program=True
    num1=GenerateRandom(10)
    num2=GenerateRandom(10)
    result=num1*num2
    while program:
        ans=input("What is"+str(num1)+"*"+str(num2)+"=")
        if(ans.isdigit()):
            if int(ans)==result:
                print("Correct")
                program=False
            else:
                print("Inaccurate")
        else:
            print("Answer must be positive")

x=10
for x in range(10):
    main()

# Console is where i add my input and check its answer by debugging
#Step Over : it doesn't step n function and stays on line of code
#Step into : Runs debugging in other codes involved too
#tep into my code : Runs debugging in only my code
#Step Out  : Get back to console