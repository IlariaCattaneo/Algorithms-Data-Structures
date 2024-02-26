def shortest_least_common_word(text):
    list_of_words = []
    word = ''
    for letter in text:
        if letter.isalpha():
            word += letter
        else:
            if not word == '':
                list_of_words.append(word)
                word = ''
    if not word == '':
            list_of_words.append(word)
    D = {}
    for word in list_of_words:
        if word in D:
            D[word] += 1
        else:
             D[word] = 1
    min = None
    least_common = None
    for k,v in D.items():
        if min == None:
            min = v
            least_common = k
        elif v < min:
            min = v
            least_common = k
        elif v == min and len(k) < len(least_common):
            least_common = k
    print(least_common)

shortest_least_common_word("""What is free software?

"Free software" is a matter of liberty, not price. To understand the
concept, you should think of "free" as in "free speech", not as in
"free beer".

Free software is a matter of the users' freedom to run, copy,
distribute, study, change and improve the software.""")