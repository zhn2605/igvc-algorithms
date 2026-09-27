"""Fails if colcon runs without the venv bridge (see setup.sh)."""


def test_core_and_ros_share_one_interpreter():
    import igvc_types
    import rclpy

    assert igvc_types.__name__ == "evil-igvc_types"
    assert rclpy.__name__ == "rclpy"
