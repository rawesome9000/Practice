while True: 
    operation=input('Pick an operation: [+] [-] [x] [/] ')        #part of the code where you choose the operation
    if operation == 'quit':                                       #does what it says, if 'quit' is typed, it breaks the loop, and goes to the next code outside the loop
        break                                                     #I could make this simpler, such as not 
    elif operation not in ('+','-','x','/'):                      #code for error control, restarts the loop if the input is not in any of the specified
        print('Invalid input')
        continue                                                  
    
    try:                                                          #error control in case a user inputs a string
        number1=int(input('Enter first number: '))
        number2=int(input('Enter second number: '))
    except:
        print('Invalid input')
        continue

    if operation == '+':                                          #the main "equation" for the script. Could be scalable, maybe I can add other operations...
        print(number1 + number2)
    elif operation == '-':
        print(number1 - number2)
    elif operation == 'x':
        print(number1 * number2)
    elif operation == '/':
        print(number1 / number2)
   
        
print('Quitting')
