from art import logo
import os
clear =lambda: os.system('cls')
clear()

def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations ={'+':add,
             '-':substract,
             '*':multiply,
             '/':divide}
def calculator():
    print(logo)
    
    num1 = float(input('What\'s the first number? : '))
    for symbols in operations:
        print(symbols)
        
    continue_calc = True

    while continue_calc:
        operation_symbol =input('Pick an operartion from above: ')
        num2 =float(input('What\'s the next number? :'))
        calcul_fun = operations[operation_symbol]
        result = calcul_fun(num1,num2)
        print(f'{num1}{operation_symbol}{num2} ={result}')
        if input(f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation: ').lower() == 'y':
            num1 =result
        else:
            continue_calc = False
            calculator()
calculator()