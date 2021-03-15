import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32MultiArray


class Turtlebot:
    def __init__(self):
        rospy.init_node('commander', anonymous=True)
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber("/cmd_vel", Twist, self.vel_callback)
        
        self.sensor_msg = None
        rospy.Subscriber("/infrared_topic", Int32MultiArray, self.sensor_callback)
        self.current_vel = Twist()

        rospy.sleep(1)  # set some delay for node settling

    def vel_callback(self, msg):
        self.current_vel = msg

    def sensor_callback(self, msg):
        self.sensor_msg = msg

    def bat_callback(self):
        pass

    def get_vel(self):
        return self.current_vel

    def get_sensor(self, number_sensors=0):
        if self.sensor_msg != None :
            return self.sensor_msg.data[number_sensors]
        else:
            return 0

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

    def move_robot(self, left, right):
        data = Twist()
        distance = 15.0 # distance of wheels
        linear_x = ( (left + right) / 2 ) / 100.0 *0.26 # percent of speed x max speed
        angular_z = -(left - right) / float(distance) #make sure distance is float
        data.linear.x = linear_x
        data.linear.y = 0.0
        data.linear.z = 0.0
        data.angular.x = 0.0
        data.angular.y = 0.0
        data.angular.z = angular_z
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
