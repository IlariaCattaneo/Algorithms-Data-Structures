def character_frequencies(text):
    D = {}
    for character in text.lower():
        if character in D:
            D[character] += 1
        else:
            D[character] = 1
    
    for key, value in D.items():
        print(key, value)

character_frequencies('This program reads a text file')