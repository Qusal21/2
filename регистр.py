print('Введите слово')
word = input()
Big=0
Small=0
for i in word:
    if 'a' <= i <= 'z':
        Small +=1
    elif 'A' <= i <= 'Z':
         Big += 1
if Big <= Small:
    print(str.lower(word))
else:
    print(str.upper(word))