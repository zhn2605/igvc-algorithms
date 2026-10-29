import math

from igvc_types import Pose2D, Twist2D, wrap_angle


def odometry_step(pose, prev, curr, dt_s, m_per_tick, track_width):
    distLeft, distRight = (
        m_per_tick * (curr.left - prev.left),
        m_per_tick * (curr.right - prev.right),
    )
    centerDist = (distRight + distLeft) / 2
    angle = (distRight - distLeft) / track_width
    d_x, d_y = (
        math.cos(pose.yaw + angle / 2) * centerDist,
        math.sin(pose.yaw + angle / 2) * centerDist,
    )
    return (
        Pose2D(pose.x + d_x, pose.y + d_y, wrap_angle(pose.yaw + angle)),
        Twist2D(centerDist / dt_s, angle / dt_s),
    )
