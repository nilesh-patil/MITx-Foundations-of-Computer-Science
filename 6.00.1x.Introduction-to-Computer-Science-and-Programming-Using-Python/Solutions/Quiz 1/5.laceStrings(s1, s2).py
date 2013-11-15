def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    if len(s1) > len(s2):
        (s1, remainder) = (s1[0:len(s2)], s1[len(s2):])
    
    elif len(s1) < len(s2):
        (s2, remainder) = (s2[0:len(s1)], s2[len(s1):])
    else:
        remainder = ""
    
    chars = []
    for i in range(len(s1)):
        chars.append(s1[i])
        chars.append(s2[i])
    result = "".join(chars) + remainder
    return result