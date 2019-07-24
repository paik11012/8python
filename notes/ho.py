# List comprehension을 활용하여 만들어주세요.
# words = 'Life is too short, you need python!'
# vowels = 'aeiou'
# result = [char for char in words if char not in vowels]
# print(''.join(result))

words = 'Life is too short, you need python!'
vowels = 'aeiou'
result = []
for char in words:
    if char not in vowels:
        result.append(char)
print(''.join(result))

