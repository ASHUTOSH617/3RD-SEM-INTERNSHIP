text ='This text contains lots of vowels'
vowels = 'AEIOUaeiou'
count =0
for i in text:
    for j in vowels:
        if i==j:
            count += 1
print('Total vowels = ',count)
            