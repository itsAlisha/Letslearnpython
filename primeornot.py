print("Enter a number : ")
n=int(input())
def checkprime(n):
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            return

    print("Prime")
    return

checkprime(n)