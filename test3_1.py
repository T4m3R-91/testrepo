print('Instructions: Enter a number followed by Enter to sum. enter reset to reset calculator \n')
y=0
while True: 
    x=input('enter a number :')
    if x=='reset':
        y=0.0
        print('\naccumulative sum=',y,'\n')
        continue
    try: z=float(x)
    except: 
        print('enter a numerical value')
        continue
    y=z+y
    print('accumulative sum =',y)
print('inout over \ntotal =',y)