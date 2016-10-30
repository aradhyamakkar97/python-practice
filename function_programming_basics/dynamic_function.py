def get_func_mult_by_num(num):

    def mult_by(value):
        return num * value

    return mult_by

generated_func = get_func_mult_by_num(5)

print("10 times 5 is ",generated_func(10))
