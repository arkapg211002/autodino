import pyautogui
from PIL import Image,ImageGrab
import time
#from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)
    return

#def draw():
def iscollide(data):
    # bird
    for i in range(260,350):
        for j in range(400, 590):
            if data[i, j] ==0:
                hit('down')
                return True

    for i in range(270, 420):
        for j in range(600, 700):
            if data[i, j]==0:
                hit('up')
                return True
    return


if __name__ == '__main__':
    print("Dino game about to start...")
    time.sleep(2)
    #hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data=image.load()
        iscollide(data)

        #cactus
        '''for i in range(270,420):
            for j in range(580, 700):
                 data[i, j]=0


        #bird
        for i in range(260,350):
            for j in range(400, 570):
                 data[i, j]=171

        #image.show()
        #break



        image.show()
        break'''
