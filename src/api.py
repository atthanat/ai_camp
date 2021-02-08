import rospy
from geometry_msgs.msg import Twist


class Turtlebot:
    def __init__(self):
        rospy.init_node('commander', anonymous=True)
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber("/cmd_vel", Twist, self.vel_callback)

        self.current_vel = Twist()

        rospy.sleep(1)  # set some delay for node settling

    def vel_callback(self, msg):
        self.current_vel = msg

    def bat_callback(self):
        pass

    def get_vel(self):
        return self.current_vel

    def get_battery(self):
        pass

    def forward(self, speed):
        data = Twist()
        data.linear.x = 1.0 * (speed / 100.0)
        data.linear.y = 0.0
        data.linear.z = 0.0
        data.angular.x = 0.0
        data.angular.y = 0.0
        data.angular.z = 0.0
        self.vel_pub.publish(data)

    def backward(self, speed):
        data = Twist()
        data.linear.x = -1.0 * (speed / 100.0)
        data.linear.y = 0.0
        data.linear.z = 0.0
        data.angular.x = 0.0
        data.angular.y = 0.0
        data.angular.z = 0.0
        self.vel_pub.publish(data)

    def turn_left(self, speed):
        data = Twist()
        data.linear.x = 0.0
        data.linear.y = 0.0
        data.linear.z = 0.0
        data.angular.x = 0.0
        data.angular.y = 0.0
        data.angular.z = 1.0 * (speed / 100.0)
        self.vel_pub.publish(data)

    def turn_right(self, speed):
        data = Twist()
        data.linear.x = 0.0
        data.linear.y = 0.0
        data.linear.z = 0.0
        data.angular.x = 0.0
        data.angular.y = 0.0
        data.angular.z = -1.0 * (speed / 100.0)
        self.vel_pub.publish(data)

    def stop(self):
        data = Twist()
        data.linear.x = 0.0
        data.linear.y = 0.0
        data.linear.z = 0.0
        data.angular.x = 0.0
        data.angular.y = 0.0
        data.angular.z = 0.0
        self.vel_pub.publish(data)
