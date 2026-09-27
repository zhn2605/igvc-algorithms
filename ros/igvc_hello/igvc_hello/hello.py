import sys

import igvc_types
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class Hello(Node):
    """Publishes which Python runs ROS and where igvc_types came from."""

    def __init__(self):
        super().__init__("hello")
        self.publisher = self.create_publisher(String, "hello", 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.text = f"python={sys.executable} igvc_types={igvc_types.__file__}"

    def timer_callback(self):
        self.publisher.publish(String(data=self.text))


def main(args=None):
    rclpy.init(args=args)
    node = Hello()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
