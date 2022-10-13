
# Product of consecutive fibonacci numbers
# return if two consecutive fib numbers can be multiplied to equal product, including the consecutive fib numbers
# f(n) * f(n+1) = prod
# return [f(n), f(n+1), true/false]
def productFib(prod):
    print(prod)
    fibs = [0,1,1]
    if prod > 2:
        for i in range(3, prod+3):
            fibs.append(fibs[i-2]+fibs[i-1])
            new = fibs[len(fibs)-1]
            current = fibs[i-2]*fibs[i-1]
            if current == prod:
                return [fibs[i-2], fibs[i-1], True]
            elif current > prod:
                return [fibs[i-2], fibs[i-1], False]
    elif prod == 2:
        fibs.append(2)
        return [fibs[2], fibs[3], True]
    elif prod == 1:
        return [fibs[1], fibs[2], True]
    elif prod == 0:
        return [fibs[0], fibs[1], True]

