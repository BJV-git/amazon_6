# add till we find the greater and when we find teh less, just subtract the previous from temp and set to 0
# so to have the last decreasing can add the 'I'

# Catch: if happen to find a greater then we have to minus, else just add up
# time: O(N)
# space: O(1)


def roman_to_integer(s):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    summ=0
    for i in range(len(s)-1):
        if dic[s[i]] < dic[s[i+1]]:
            summ -= dic[s[i]] # i.e. we are setting the minus
        else:
            summ+=dic[s[i]] # add up

    return summ+dic[s[i]]