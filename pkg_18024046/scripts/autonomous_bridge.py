#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class AutonomousBridge(Node):
    def __init__(self):
        super().__init__('autonomous_bridge')
        self.subscriber = self.create_subscription(Twist, 'autonomous_vel', self.twist_callback, 10)
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.cmd_type_pub = self.create_publisher(String, 'cmd_type', 10)

    def twist_callback(self, msg):
        self.cmd_vel_pub.publish(msg)
        cmd_type_msg = String()
        cmd_type_msg.data = 'autonomous'
        self.cmd_type_pub.publish(cmd_type_msg)

def main(args=None):
    rclpy.init(args=args)
    node = AutonomousBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
