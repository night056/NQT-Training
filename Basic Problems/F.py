'''Ezio can manipulate at most X number of guards with the apple of eden.
Given that there are Y number of guards, predict if he can safely manipulate all of them.'''

n=int(input())
while n>0:
    x, y=map(int, input().split())
    if x>=y:
        print("YES")
    else:
        print("NO")
    n=n-1
