def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    # FILL IN YOUR CODE HERE...
    if start >= stop - step:
        return f(stop-step) * step
    return (f(start) * step) + radiationExposure(start + step, stop, step)