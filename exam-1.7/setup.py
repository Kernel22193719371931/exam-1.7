from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'exam_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'battery_node = exam_robot.battery_node:main',
            'distance_sensor = exam_robot.distance_sensor:main',
            'robot_status = exam_robot.robot_status:main',
            'motor_simulator = exam_robot.motor_simulator:main',
        ],
    },
)