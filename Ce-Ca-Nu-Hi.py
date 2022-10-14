a=list(input('enter your credit card number please'))
b=[]
for t in a:
    if t in a[:5]:
        print(t)
        t="*"
        b.append(t)
    elif t in a[5:9]:
        b.append(t)
    else:
        pass
print(b)
j = ''.join(b)
print(j)