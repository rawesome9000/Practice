
#I'm pretty new to this github thing, and pretty new in adding comments...
#but anyway, here is a simple Looping Calculator that I made
#My first ever python script, and the project that made me fell in love with programming in general
#Who knows what future has in store for me... 

while True: 
    operation=input('Pick an operation: [+] [-] [x] [/] ')
    if operation == 'quit':
        break
    elif operation not in ('+','-','x','/'):
        print('Invalid input')
        continue
    
    try:
        number1=int(input('Enter first number: '))
        number2=int(input('Enter second number: '))
    except:
        print('Invalid input')
        continue

    if operation == '+':
        print(number1 + number2)
    elif operation == '-':
        print(number1 - number2)
    elif operation == 'x':
        print(number1 * number2)
    elif operation == '/':
        print(number1 / number2)
    elif operation == 'Quit':
        break
    
print('Quitting')
    
