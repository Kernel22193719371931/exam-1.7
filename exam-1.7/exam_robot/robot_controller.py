#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.last_status = ""
        
        self.status_sub = self.create_subscription(
            String, '/robot_status', self.status_callback, 10)
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_cmd)
        
        self.current_twist = Twist()
        
    def status_callback(self, msg):
        status = msg.data
        
        if status != self.last_status:
            self.last_status = status
            self.get_logger().info(f'Status: {status}')
            
            if status == "ALL OK":
                self.current_twist.linear.x = 0.3
                self.current_twist.angular.z = 0.0
            elif status == "WARNING: Low battery":
                self.current_twist.linear.x = 0.1
                self.current_twist.angular.z = 0.0
            elif status == "WARNING: Obstacle close":
                self.current_twist.linear.x = 0.0
                self.current_twist.angular.z = 0.5
            elif status == "CRITICAL":
                self.current_twist.linear.x = 0.0
                self.current_twist.angular.z = 0.0
    
    def publish_cmd(self):
        self.cmd_pub.publish(self.current_twist)

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()