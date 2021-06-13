translation = {}
with open("Traslation.txt", encoding='utf8') as file:
    for line in file:
        key, *value = line.split()
        translation[key] = value[1]
v = translation.values()

text = open('input.txt', encoding='utf8')
for line in text:
    for word in line:
        print(translation[key])