'''Chef is watching TV. The current volume of the TV is X. Pressing the volume up button of the TV remote increases the volume by 1 while pressing the volume down button decreases the volume by 1. Chef wants to change the volume from X to Y. Find the minimum number of 
button presses required to do so.'''
n=int(input())
while n>0:
    x, y=map(int, input().split())
    print(abs(x-y))
    n=n-1
