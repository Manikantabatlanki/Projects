num=int(input('enter a number:'))
bkp=num
d_cnt=0
while num>0:
    num=num//10
    d_cnt=d_cnt+1
num=bkp
s=0
while num>0:
    m=num%10
    s=s+m**d_cnt
    num=num//10
if s==bkp:
    print('it is armstrong')
else:
    print('it is not a armstrong')
