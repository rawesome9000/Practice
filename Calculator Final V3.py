def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

while True:
    operations=('+','-','*','/')
    choice=input('Please pick an operation: [+] [-] [*] [/] ').lower()
    if choice == 'quit':
        print('Quitting')
        break
    elif choice not in operations:
        print('Invalid input')
        continue

    try:
        num1=int(input('1st number: '))
        num2=int(input('2nd number: '))
    except:
        print('You must enter a number')
        continue
    
    if choice == '+':
        print(add(num1,num2))
    elif choice == '-':
        print(subtract(num1,num2))
    elif choice == '*':
        print(multiply(num1,num2))
    elif choice == '/':
        try:
            print(divide(num1,num2))
        except:
            print('Undefined')
            continue
    
    
