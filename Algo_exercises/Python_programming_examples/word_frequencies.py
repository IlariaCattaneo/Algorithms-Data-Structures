def word_frequencies(text):
    list_of_words = []
    word = ''
    for letter in text:
        if letter.isalpha():
            word += letter
        else:
            if not word == '':
                list_of_words.append(word.lower())
                word = ''
    if not word == '':
        list_of_words.append(word.lower())    
    # print(list_of_words)
    D = {}
    for word in list_of_words:
        if word in D:
            D[word] += 1
        else:
            D[word] = 1
    # print(D)
    for key, value in D.items():
        print(key, value)

word_frequencies('This program reads a text file')