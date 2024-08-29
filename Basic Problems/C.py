'''Write a program which reads two integers x and y, and prints them in ascending order.'''
while True:
    k=[]
    n,m=input().split()
    n=int(n)
    m=int(m)
    if n==0 and m==0:
        break
    else:
        print(min(n, m), max(n, m))
