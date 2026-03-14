#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class BatteryNode(Node):
    def __init__(self):
        super().__init__('battery_node')
        self.publisher = self.create_publisher(Float32, '/battery_level', 10)
        self.timer = self.create_timer(1.0, self.publish_battery)
        self.battery = 100.0
    
    def publish_battery(self):
        if self.battery > 0:
            self.battery -= 1.0
            if self.battery < 0:
                self.battery = 0.0
            
            if self.battery % 10 == 0:
                self.get_logger().info(f'Battery: {self.battery}%')
        
        msg = Float32()
        msg.data = self.battery
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()