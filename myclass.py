class MyClass:
    number = 0
    name = "noname"

def Main():
    me = MyClass()
    me.number = 1337
    me.name = "Aradhya"

    friend = MyClass()
    friend.number = 3
    friend.name = "Steve"

    empty = MyClass()

    print("Name :"+me.name + ",  fav no. : "+str(me.number))
    print("Name :"+friend.name + ",  fav no. : "+str(friend.number))
    print("Name :"+empty.name + ",  fav no. : "+str(empty.number))

if __name__ == '__main__':
    Main()
