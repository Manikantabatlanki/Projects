num=int(input('enter a number:'))
d=2
while d<=num//2:
    if num%d==0:
        print('not prime')
        break
    d=d+1
else:
    print('prime')
    

