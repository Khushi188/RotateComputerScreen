#an app that rotates a screen by 360*
#just for fun app to play around with your friends

#pip install rotate-screen
import rotatescreen
import time
screen = rotatescreen.get_primary_display()
for i in range(5):
    time.sleep(1)
    screen.rotate_to(i*90 % 360)

