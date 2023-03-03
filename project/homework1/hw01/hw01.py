def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    cnt=1
    print(int(x))
    while x !=1:
        if x%2==0:
            x/=2
            cnt+=1
            print(int(x))
        else :
            x=x*3+1
            cnt+=1
            print(int(x))
    return cnt