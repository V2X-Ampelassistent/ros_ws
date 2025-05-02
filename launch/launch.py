from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='v2x_cohdatoros',
            executable='DSRC_publisher',
            parameters=[
                {'port': 38008}
            ]
        ),
        Node(
            package='v2x_cohdatoros',
            executable='GPS_publisher',
            parameters=[
                {'port': 38010}
            ]
        )
    ])