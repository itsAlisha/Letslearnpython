print("Enter a number : ")
n=int(input())

def fib(n):
    if n==0 :
        return 0
    if n==1:
        return 1
    a=0
    b=1
    print(a)
    print(b)

    for i in range(2,n):
        fib=a+b
        a=b
        b=fib
        print(fib)

fib(n)