from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="igvc_hello",
                executable="hello",
            ),
            Node(
                package="foxglove_bridge",
                executable="foxglove_bridge",
            ),
        ]
    )
