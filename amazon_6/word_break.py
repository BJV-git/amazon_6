# POINT: DP, verifies if its a valid start and then sees if there is any valid split word in the given map
# its a greedy too, but storing all the possibles starts so we cna know what split is optimal

# so when we divide a word we set the [] index to be true so that from that point we will check that if any

# time: O(N2) -- ?
# space: O(N)

# imporvement - ??????
# Catch: just go through till iterations in every, and see if its a start and if there is one in given dict

def word_break(s, map):
    map = set(map)
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in map for j in range(i)), # rather than checking from every point to last lets do the opposite
                                                              # if every linear possible word is a possible start and in map
                                                              # which sees if any element fits before that so that curr can be a start
                                                              # which lays foundation for the next
    print((ok))
    return ok[-1]

    # f[0] = True
    # for i in range(ls):
    #     if f[i]:
    #         for j in map:
    #             l = len(j)
    #             if l+i <= ls and s[i:i+l] == j:
    #                 f[i+l] = True
    # print(f)
    # return f[ls]

def wordbreak(s, words):
    sl = len(s)
    d=[False]*sl
    for i in range(sl):
        for w in words:
            if w==s[i-len(w)+1:i+1] and (d[i-len(w)] or i - len(w)==-1): # the resaon for +1 on btoh side is understood if thoiught
                d[i] = True
                break
    return d[-1]


print(word_break('bnbananaapples',['apples', 'bn', 'banana'] ))