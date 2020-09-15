# To find 2^n without performing multiplication
def f(n):
    if n == 0:
        return 1

    ans = 0
    for i in range(n):
        ans = ans + f(i)
    return ans+1 

# Drawback: The above solution is very slow for large numbers
#def f(n):
#    if n == 0:
#        return 1
#    return 2 * f(n-1)