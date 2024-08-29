'''A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).'''
n=int(input())
L=[]
count=0
for _ in range(n):
    a=int(input())
    if a==0:
        count+=1
    else:
        L.append(a)
for _ in range(count):
    L.append(0)
print(L)
        
