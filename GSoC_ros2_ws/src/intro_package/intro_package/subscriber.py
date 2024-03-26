#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):

    def __init__(self):
        super().__init__('node_GSoC_subs')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            20)
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info('Great! Nice to hear that')
        
def main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()