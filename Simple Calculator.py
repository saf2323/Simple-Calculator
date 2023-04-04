#Calculator

print('Calculator')

num1 = int(input('ENTER FIRST NUMBER:'))
num2 = int(input('ENTER SECOND NUMBER:'))

print('Choices:')
print('1. +')
print('2. -')
print('3. *')
print('4. /')
print('5. %')

choice = input('ENTER STATEMENT:')

if choice=='+':
    print('ANSWER:',num1 + num2)

if choice=='-':
    print('ANSWER:',num1 - num2)

if choice=='*':
    print('ANSWER:',num1 * num2)

if choice=='/':
    print('ANSWER:',num1 / num2)

if choice=='%':
    print('ANSWER:',num1 % num2)


