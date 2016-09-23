import threading
import time

class AsyncWrite(threading.Thread):

    def __init__(self,text,out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out,"a")
        f.write(self.text+'\n')
        f.close()
        time.sleep(2)
        print("finished background file Write to "+self.out)

def Main():
    message = input("Enter a string to store: ")
    background = AsyncWrite(message,'out.txt')
    background.start()
    print("the program can continue while it writes in another thread")

    print("life is a bitch, and death is her sister\n sleep is her cousing, what a fucking family picture")
    background.join()
    print('waited until thread was complete')

if __name__ == '__main__':
    Main()
