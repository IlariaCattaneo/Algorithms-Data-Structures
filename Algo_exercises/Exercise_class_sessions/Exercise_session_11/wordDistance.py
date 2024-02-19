class Node:
    def __init__(self, word):
        self.nexts = []
        self.word = word


def distance(word1, word2):
    count = 0
    dim = len(word1) if len(word1) < len(word2) else len(word2)
    for i in range(dim):
        if word1[i] != word2[i]:
            count += 1
    return count
   

def wordDistance(beginWord, endWord, wordList):
    count = 0
    if endWord not in wordList:
        return 0
    else:
        n = Node(beginWord)

        for i in wordList:
            if distance(n.word, i) == 1:
                n.nexts.append(i)
                


wordDistance('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
# print(distance('hit', 'cog'))