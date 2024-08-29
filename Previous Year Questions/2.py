'''Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment problems before the lecture. Today he got one tricky question. The problem statement is “A positive integer has been given as an input. 
Convert decimal value to binary representation. Toggle all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits”.'''

n=int(input())
a=1
bin_num=0
while n>0:
    d=n%2
    bin_num+=(d*a)
    a=a*10
    n=n/2
print(bin_num)
'''to edit'''
