from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='v2x_cohdatoros',
            executable='DSRC_publisher',
            parameters=[
                {'port': 37008}
            ]
        ),
        Node(
            package='v2x_cohdatoros',
            executable='GPS_publisher',
            parameters=[
                {'port': 37010}
            ]
        ),
        Node(
            package='can_bridge',
            executable='can_bridge_node',
            ),
        Node(
            package='v2x_frontend',
            executable='v2x_frontend_server',
        ),
        Node(
            package='v2x_trafficlightassist',
            executable='redlightassist',
        )
    ])
