def is_it_odd(num):
    if num%2 ==0:
        return False
    return True

def change_list(list,func):
    oddlist = []

    for i in list:
        if func(i):
            oddlist.append(i)

    return oddlist

aList = range(1,20)

print(change_list(aList,is_it_odd))
