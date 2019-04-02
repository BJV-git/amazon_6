# Catch: use the re to grab and dic to count

# Time: O(N), for k words, maintain a heap and get it in klogk times
# Space: O(N)

import re
import collections

def mostCommonWord( para, ban):
    ban = [i.lower() for i in ban]
    pattern = r'(\w+)'
    l = [i for i in re.findall(pattern, para) if i.lower() not in ban]
    dic = {}
    for i in l:
        dic[i.lower()] = dic.get(i.lower(), 0) + 1

    maxi = 0
    c = collections.Counter(dic)
    a = c.most_common(1)[0][0]
    return (a)

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))