'''Write a program which reads three integers a, b and c, and prints the number of divisors of c between a and b.'''
a, b, c=map(int, input().split())
count=0
for i in range(a, b+1):
    if c%i==0:
        count+=1 

print(count)
