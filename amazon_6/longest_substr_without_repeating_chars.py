# Time: O(N)
# Space: O(1) - as just the dic of 26 letters

# Catch: index and start

# We maintain a dic of prev envountered letter index, we avoid by +1 start if the usedchar index is less than start we anyways
# avoided and keep the updated max

def lenlognonrept(s):
    start = Maxlen=0
    usedchar={}

    for index, char in enumerate(s):

        if char in usedchar and  usedchar[char] >= start: # and the only time we update is, once the elemnt is found after the start
                                                          # as start only has all unique elements
            start = usedchar[char]+1                      # only way to avoid the specific variable is to move right if not
                                                          # in left it will be there
        else:
            Maxlen = max(Maxlen, index - start + 1)

        usedchar[char] = index
        print(index, start)

    return Maxlen

print(lenlognonrept('tmmzuxt'))