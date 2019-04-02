# Point: we count if happen to see all needed update and remove the seen one first and let remaining characetrs be there
# so for count missing, counter are maintained

# the reason why it would stop at last seen is the extra faced meanwhile are <-1 so can be skipped and the one with 0 is taken over

# Catch: need = counter, missing is the one we seen first and want to see next
# make the i move to the one we have seen .... as above

# Time: O(N)
# Space: O(1)

import collections

def minWindow( s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1 # will reduce beyond zero if seen
        print(j, c, ', missing:',missing, need, i)
        if not missing:
            while need[s[i]] < 0: need[s[i]] += 1; i += 1 # this stops actually when the expected is met
            # actually placing i at exactly one of the first seen among 'ABC' or the one we expect next
            if not J or j - i <= J - I: I, J = i, j

            # lets restart
            need[s[i]] += 1 # we are saying edithe min required lo first chusamo, expect to see again soon
            i += 1
            missing += 1
            print('\n', 'need at after inner upafte', need, i)
    return s[I: J]

print(minWindow("ADOBECODEBANC", "ABC"))