class Sum:

    @staticmethod
    def getSum(*args):
        sum = 0
        for i in args:
            sum+= i
        return sum

def main():
    print("Sum :",Sum.getSum(1,2,3,45,5))

main()
