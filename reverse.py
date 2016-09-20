def Reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

def Main():
    rev = Reverse('Aradhya')
    for char in rev:
        print(char)

    data = 'Aradhya'
    print(list(data[i] for i in range(len(data)-1,-1,-1)))

if __name__ =='__main__':
    Main()
