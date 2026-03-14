#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class DistanceSensor(Node):
    def __init__(self):
        super().__init__('distance_sensor')
        
        self.min_range = 0.5
        self.max_range = 3.0
        self.distance = 3.0
        self.linear_vel = 0.0
        
        self.publisher = self.create_publisher(Float32, '/distance', 10)
        self.subscriber = self.create_subscription(Twist, '/cmd_vel', self.cmd_callback, 10)
        self.timer = self.create_timer(0.2, self.publish_ranges)
    
    def cmd_callback(self, msg):
        self.linear_vel = msg.linear.x
    
    def publish_ranges(self):
        if self.linear_vel > 0:
            self.distance = max(self.distance - 0.2, self.min_range)
        elif self.linear_vel < 0:
            self.distance = min(self.distance + 0.2, self.max_range)
        else:
            self.distance = 3.0
        
        msg = Float32()
        msg.data = self.distance
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()