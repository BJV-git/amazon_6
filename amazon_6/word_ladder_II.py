# Logic: the same process extra is that at each step we will get the new words formed  and their path to that word

import collections
def printladders(begin, end, wordlist):
    wordlist = set(wordlist)
    res=[]
    layer={}
    layer[begin] = [[begin]]

    while layer:
        newlayer = collections.defaultdict(list)
        for w in layer:
            if w==end:
                res.extend(k for k in layer[w])
                return res
            else:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newer = w[:i] + c + w[i+1:]
                        if newer in wordlist:
                            newlayer[newer] += [j + [newer] for j in layer[w]]

        wordlist -= set(newlayer.keys())
        layer  =  newlayer
    return []

print(printladders("hit","cog",["hot","dot","dog","lot","log","cog"]))

