# we can try going through loops but if the length of the input change then its not proper to go for loops as
# loops are not dynamically written

# so, back tracking is like dynamic looping

# catch: we are coming from last so its curr + prev, is what given to the recursion

# Time: O(3^N) as for each element we get 3 power of combo
# Space: O(1) - recursion



def lettercombo(digits):

    map= {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    if len(digits)==0:
        return []
    if len(digits)==1:
        return list(map[digits[0]]) # as we receive in form of array

    prev = lettercombo(digits[:-1])

    current = map[digits[-1]]

    return [p+c for p in prev for c in current] # irrespective of the inner or outer loops ans is correct