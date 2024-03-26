#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Node(Node):
    
    def __init__(self):
        super().__init__("node_gsoc")
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        timer_period = 5.0  
        self.timer = self.create_timer(timer_period, self.timer_callback)
       
        
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello! ROS2 is fun'
        self.publisher_.publish(msg)
        self.get_logger().info('"%s"' % msg.data)
        
        
def main(args=None):
    rclpy.init(args=args)
    node = Node()
    rclpy.spin(node)
    rclpy.shutdown()
    
if  __name__ == '__main__':
    main()    