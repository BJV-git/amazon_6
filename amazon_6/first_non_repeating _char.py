# isntead of maintaingin a dict lets mainatain a row of all alphabets

# Time: O(N)
# Space: O(1)

def firtsUnique(s):
    count={}
    for i in s:
        count[i] = count.get(i,0)+1
    for i in s:
        if count[i]==1:
            return i
    return -1