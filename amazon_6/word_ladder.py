# POINT: pre-process, while queue, for the begin word we need to see all possible routes so for all i, _ , i+1

# Point: pre process - so that we have all possibilities for all the blanks
# write down the base cases and if not visited just add to the visited

# TIME:  O()
# SPACE: O()


def word_ladder(begin, end, wordict):
    l = 2
    front, back = set([begin]), set([end])

    wordict.discard(begin)

    while front:
        front = wordict & (set(word[:index] + ch + word[index+1:] for word in front
                               for index in range(len(begin))for ch in 'abcdefghijklmnopqrstuvwxyz'))

        if front & back:
            return l

        l+=1

        if len(front) > len(back):
            front, back = back, front

        wordict -= front

    return 0












































from collections import deque

def word_ladder(beginWord, endWord, wordList):

    def construct(word_List):
        d={}
        for word in word_List:
            for i in range(len(word)):
                s=word[:i]+"_"+word[i+1:]
                d[s] = d.get(s,[])+[word]
        print(d)
        return d


    def bfs(begin, end, dict_words):
        queue, visited = deque([(begin,1)]), set()
        while queue:
            word, steps = queue.popleft()
            if word not in visited:
                visited.add(word)

                if word==end:
                    return steps

                for i in range(len(word)):
                    s=word[:i]+"_"+word[i+1:]
                    neighbours = dict_words.get(s,[])
                    for n in neighbours:
                        if n not in visited:
                            queue.append((n,steps+1))
        return 0


    d = construct( set(wordList )| set([beginWord])) # we might need the end word as it might not exist in the dictionary provided to make a path
    return bfs(beginWord, endWord, d)

print(word_ladder('hit','hot', ["hot","dot","dog","lot","log","cog"]))


































    # queue = [(beginWord,1)]
    # visited = set()
    #
    # while queue:
    #     word,dist = queue.pop(0)
    #     if word == endWord:
    #         return dist
    #
    #     for  i in range(len(word)):
    #         for j in 'abcdefghijklmnopqrstuvwxyz':
    #             temp = word[:i]+j+word[i+1:]
    #             if temp not in visited and temp in wordList:
    #                 queue.append((temp,dist+1))
    #                 visited.add(temp)
    #
    #     return 0