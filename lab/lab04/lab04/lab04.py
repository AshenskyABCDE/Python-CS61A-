LAB_SOURCE_FILE = __file__


def add_chars(w1, w2):
    s=''
    j=0
    for ch in w2:
        if j==len(w1):
            s+=ch
        elif ch != w1[j]:
            s+=ch
        else:
            j=1
    return s

