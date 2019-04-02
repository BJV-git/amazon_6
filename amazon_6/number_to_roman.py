# Point: we can maintain the track of all possible 100 and 90 and so on and their respective romans and just divide and subtract and go on

# Catch: first we want to repsent th ehigher to low, so order the dic as wise but with 900 adn all too
# add to results
# decreasr to n

# time: O(1) - O(10)
# Space: O(1)

def num_to_roman(n):

    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    res=''
    romans=["", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    i=0
    while n:
        res+= (n//values[i])*romans[i]
        n %= values[i]
        i+=1
    return res


print(num_to_roman(45))