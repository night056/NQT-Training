n=int(input())
while n>0:
    m=int(input())
    l=list(map(int, input().split()))
    count=0
    for i in l:
        if i>=1000:
            count+=1
    print(count)
    n-=1
