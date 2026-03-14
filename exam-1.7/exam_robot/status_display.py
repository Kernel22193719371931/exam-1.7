#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32

class RobotStatus(Node):
    def __init__(self):
        super().__init__('robot_status')
        self.battery = 100.0
        self.distance = 3.0
        self.status = ""
        
        self.battery_sub = self.create_subscription(
            Float32, '/battery_level', self.battery_callback, 10)
        self.distance_sub = self.create_subscription(
            Float32, '/distance', self.distance_callback, 10)
        self.status_pub = self.create_publisher(String, '/robot_status', 10)
        self.timer = self.create_timer(0.5, self.publish_status)
        
    def battery_callback(self, msg):
        self.battery = msg.data
    
    def distance_callback(self, msg):
        self.distance = msg.data
    
    def publish_status(self):
        status1 = ""
        
        if self.battery < 10.0 or self.distance < 0.7:
            status1 = "CRITICAL"
        elif self.battery < 20.0:
            status1 = "WARNING: Low battery"
        elif self.distance < 1.0:
            status1 = "WARNING: Obstacle close"
        else:
            status1 = "ALL OK"
        
        if status1 != self.status:
            self.status = status1
            self.get_logger().info(f'Status: {status1}')
        
        msg = String()
        msg.data = status1
        self.status_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotStatus()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()