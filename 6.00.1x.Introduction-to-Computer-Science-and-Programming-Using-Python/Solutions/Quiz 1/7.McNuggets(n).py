def McNuggets(n):
   
    if n == 0:
        return True
    for i in (6, 9, 20):
        if n >= i and McNuggets(n - i):
            return True
    return False