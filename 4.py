import string

translation = {}
with open("Traslation.txt", encoding='utf8') as file:
    for line in file:
        key, *value = line.split()
        translation[key] = value[1]
v = translation.items()

with open('input.txt', encoding='utf8') as text:
    #symbols = ['!', '@', '#', '?', '%', '.', ',']
    #for symbol in symbols:
    #    if symbol in text:
    #        text.replace(symbol, ' ')
    for line in text:
        line = line.lower()
        for word in line.split():
            if word in translation.keys():
                list(map(lambda x: translation[x] if x in translation else x, line))
                print(word, translation.get(word))
            else:
                print(word)
