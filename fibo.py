# Fibonacci numbers module
def fib(n, test=None):     # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b
    print('\n',test)

def fib2(n):    # return Fibonaci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# executing modules as scripts
if __name__ == '__main__':
    import sys
    # fib(int(sys.argv[1]))
    # fib(int(sys.argv[1]), int(sys.argv[2]))
    fib(int(sys.argv[1]), sys.argv[2])
    # python fibo.py 10 69
