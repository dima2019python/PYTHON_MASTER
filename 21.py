words = ['мадам', 'самолет', 'madam', 'oko']
palidromes = []

for word in words:
    if word == word[::-1]:
        palidromes.append(word)

print(palidromes)

