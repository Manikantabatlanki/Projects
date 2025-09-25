m='python full stack develpoer'
s=m.replace(" ","")
output=''
max=0
for ch in m:
    if ch not in output:
        cnt=0
        for other in m:
            if ch==other:
                cnt=cnt+1
        if cnt>max:
            max=cnt
            output=ch
        elif cnt>=max:
            output=output+ch
print(output)
