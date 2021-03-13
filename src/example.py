import time
from api import Turtlebot

robot = Turtlebot()
print "bringup finished"

robot.forward(50)  # 50% speed
time.sleep(3)
print "forward finished"

robot.backward(50)
time.sleep(3)
print "backward finished"

robot.turn_left(50)
time.sleep(3)
print "turn left finished"

robot.turn_right(50)
time.sleep(3)
print "turn right finished"

robot.stop()
print "stop"

time.sleep(1)
print "current velocity is "
print robot.get_vel()
