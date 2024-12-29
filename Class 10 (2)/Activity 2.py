#Reversing a string/number using loops
word = input('Enter a word : ')
word2 = ('')
for i in word:
    word2 = i + word2
    print(word2)

print('The correct word is' ,word)
print('The reversed word is' ,word2)