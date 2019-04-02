# Point: make the sorted order of the words as the key to identify
# space: O(N), time: O(N)

# just use the letters in each word

def groupanagrams(strs):
    map={}
    for w in (strs):
        key = set(w)
        map[key]=map.get(key,[])+[w]
    return map.values()