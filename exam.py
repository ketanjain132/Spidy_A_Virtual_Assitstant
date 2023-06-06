def fun(n): 
    if (n > 100):
        return n - 5
    return fun(fun(n+11));
print(fun(45))