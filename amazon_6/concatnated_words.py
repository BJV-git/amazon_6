
def concatwords(words):
    res=[]
    words = set(words)
    for w in words:
        words.remove(w)
        if check(w,  words):
            res.append(w)
        words.add(w)
    return res

def check(word, d):
    if word in d:
        return  True
    for i in range(len(word), 0, -1):
        if word[:i] in d and check(word[i:], d): # this helps in finding if a word  is formed in multiple combos
            return True
    return False