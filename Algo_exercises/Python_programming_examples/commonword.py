def commonword(text):
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
    max = 0
    most_common = None
    for word in D:
        if D[word] > max:
            max = D[word]
            most_common = word
    print(most_common)

# ex 1
commonword("""What is free software?

"Free software" is a matter of liberty, not price. To understand the
concept, you should think of "free" as in "free speech", not as in
"free beer".

Free software is a matter of the users' freedom to run, copy,
distribute, study, change and improve the software.""")