y=0
while True: 
    x=input('enter a number :')
    try: z=float(x)
    except: 
        if x=='done': break
    y=z+y
print('y=',y)