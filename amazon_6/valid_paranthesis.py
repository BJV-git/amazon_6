# Point: as we append open, when we get close, to get we have to hav dict of key close and pop stack not
# time: O(n), space:O(n) for O(1) index can be used to track opens

# Catch: u push the open so when u get close have dic so can see the match

def valid_paranthesis(s):
    stack=[]
    open=set(['{','(','['])
    close = set(['}',']',')'])

    dic = {'}': '{', ')': '(', ']': '['}

    for brac in s:
        if brac in open:
            stack.append(brac)
        elif brac in close:
            if not stack or stack.pop() != dic[brac]:
                return False

    return not stack  # extra braces i.e. just the closed ones