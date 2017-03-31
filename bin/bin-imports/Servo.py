
import RPi.GPIO as GPIO
import time




def pwm(frequency):

    GPIO.setmode(GPIO.BOARD)
    
    # pin 13

    GPIO.setup(13, GPIO.OUT)

    # 12 is the pin number of PI
    # 50 is the frequency
    p = GPIO.PWM(12, 50)

    p.start(7.5)


    #Duty Cycle = length / period

    #length is the iwsth of the puulse, which in this case is .5 or 2.5 ms
    # period is you know 1/ frequency
    try:
        t = 10, 000
        while (t != 0):
            t = t -1
            p.ChangeDutyCycle(12.5)  # turn towards 180 degree
            time.sleep(1)
        t = 10, 000
        while (t != 0):
            t = t - 1
            p.ChangeDutyCycle(2.5)  # turn towards 0 degree
            time.sleep(1)  # sleep 1 second

#root = Tk()
#root.wm_title('Servo Control')
#app = App(root)
#root.geometry("200x50+0+0")
#root.mainloop()

