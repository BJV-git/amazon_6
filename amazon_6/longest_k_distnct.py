# Point: checking if a window is valid takes constant if used constant space map, i.e. to see if uniq are more than k, by that move the window
# can make it more efficient if we maintain a count of uniques

# Catch: use the window
# so we need to have a map to keep track of k distinct count, same as longest window substring
# we move on and if exceeds we delete
# we update teh max
# good as we have to move till all duplicates are removed

# Time:  O(N)
# Space: O(1)

def longest_k(s,k):
    ls = len(s)

    if len(set(s)) < k:
        print('wrong input')
        return None

    curr_start=0
    curr_end = 0

    max_win = 1
    max_start = 0

    map = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}

    map[s[0]] +=1
    ls=len(s)

    for i in range(1,ls):
        map[s[i]] +=1
        curr_end+=1

        while k >= len((i for i in map if map[i]>0)): # all it does is just move and remove one
            map[s[curr_start]]-=1
            curr_start+=1
        if curr_end-curr_start+1 > max_win and k == len((i for i in map if map[i]>0)):
            max_win = curr_end-curr_start+1
            max_start = curr_start

    return max_win

# https://www.programcreek.com/2013/02/longest-substring-which-contains-2-unique-characters/

def longest_k_char(s,k):
    result=0
    i=0
    map={}
    ls =len(s)
    for j in range(ls):
        ch = s[j]
        map[ch] = map.get(ch,0)+1
        if len(map) <= k:
            result = max(result, j-i+1)
        else:
            while len(map) > k:
                c = s[i]
                map[c]-=1
                if not map[c]:
                    del map[c]
                i+=1
    return result