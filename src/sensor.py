import time
import rospy
from api import Turtlebot


def tester():

    robot = Turtlebot()
    
    print "bringup finished"
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        ir_right, ir_left = robot.get_sensor()
        
        print "Infrared sensor left:" + str(ir_left) + " Infrared sensor right:" + str(ir_right)

        rate.sleep()



    robot.stop()
    print "stop"
    print "current velocity is "
    print robot.get_vel()

if __name__ == '__main__':
    try:
        tester()
    except rospy.ROSInterruptException:
        pass
