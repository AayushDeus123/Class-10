#Sum of whole numbers consecutively
num = int(input('Enter a whole number : '))
sum = 0
for i in range(1, num+1):
    sum = sum + i
    print(sum)
print('The final sum is : ',sum)