import argparse

def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b= b,a+b
    return a

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num",help="The Fibonachhhhhi num u wich to calculate ",type=int)

    args = parser.parse_args()

    result = fib(args.num)

    print ('the '+str(args.num)+"th fib number is "+str(result))

if __name__ == '__main__':
    Main()
