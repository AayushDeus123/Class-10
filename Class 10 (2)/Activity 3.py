#Reverse order for numbers
num = int(input('Enter a number : '))
for i in range(num, -1, -1):
    print(i)
print('The reverse order till 0 is' ,i, '\n')
#Correct order for numbers
for i in range(0, num, 2):
    print(i)    
print('The correct order till given number is' ,i)