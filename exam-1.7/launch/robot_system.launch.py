import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_file = os.path.join(
        get_package_share_directory('exam_robot'),
        'urdf',
        'exam_robot.urdf'
    )
    
    with open(urdf_file, 'r') as f:
        robot_desc = f.read()
    
    return LaunchDescription([
        Node(package='exam_robot', executable='battery_node'),
        Node(package='exam_robot', executable='distance_sensor'),
        Node(package='exam_robot', executable='robot_status'),
        Node(package='exam_robot', executable='motor_simulator'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}]
        ),
        # Добавляем joint_state_publisher для публикации состояний суставов
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            parameters=[{'source_list': ['']}]
        ),
    ])