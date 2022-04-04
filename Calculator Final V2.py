while True: 
    operation=input('Pick an operation: [+] [-] [x] [/] [quit] ').lower()
    
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
        try:
            print(number1 / number2)
        except:
            print('Undefined')
        
   
        
print('Quitting')
