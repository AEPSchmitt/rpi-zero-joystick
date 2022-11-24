from gpiozero import Button
from time import sleep

NULL_CHAR = chr(0)

DOWN = Button(23)
UP = Button(24)
RIGHT = Button(25)
LEFT = Button(27)
tickrate = 60


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        try:
            fd.write(report.encode())
        except Exception as e:
            fd.write((NULL_CHAR*8).encode())
            print(e)

def run():
    while True:
        u = 82 if UP.is_pressed else 0
        d = 81 if DOWN.is_pressed else 0
        l = 80 if LEFT.is_pressed else 0
        r = 79 if RIGHT.is_pressed else 0
        
        report = (NULL_CHAR*2+chr(u)+chr(d)+chr(l)+chr(r)+NULL_CHAR*2)
        #print(report.encode())
        write_report(report)
        sleep(1.0/tickrate)
                
run()
