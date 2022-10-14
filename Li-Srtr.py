thelist= []
        
while True:
    a = input('Enter the number you want to add to the list: \n')
    if a == 'exit':
       break
    else:   
        thelist.append(int(a))
        print(thelist)

j=int(input('For Asending order press 1 and for Desending order press 2: \n'))
if j==1:
    print(sorted(thelist, reverse=False))
        
else: 
    print(sorted(thelist, reverse=True))
