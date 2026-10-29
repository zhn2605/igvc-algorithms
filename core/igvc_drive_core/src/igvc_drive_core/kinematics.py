from igvc_types import Twist2D, WheelSpeeds


def twist_to_wheels(twist, track_width):
    right_wheel = (twist.w * track_width + 2 * twist.v) / 2
    left_wheel = (-twist.w * track_width + 2 * twist.v) / 2
    return WheelSpeeds(left_wheel, right_wheel)


def wheels_to_twist(wheels, track_width):
    b_v = (wheels.left + wheels.right) / 2
    w_v = (wheels.right - wheels.left) / track_width
    return Twist2D(b_v, w_v)
