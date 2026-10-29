import math

import pytest
from igvc_drive_core.odometry import odometry_step
from igvc_types import Pose2D, WheelTicks

K = {"m_per_tick": 0.001, "track_width": 0.5}


def test_straight():
    pose, tw = odometry_step(
        Pose2D(), WheelTicks(0, 0), WheelTicks(1000, 1000), dt_s=0.5, **K
    )
    assert (pose.x, pose.y, pose.yaw) == pytest.approx((1.0, 0.0, 0.0))
    assert (tw.v, tw.w) == pytest.approx((2.0, 0.0))


def test_spin_in_place():
    pose, tw = odometry_step(
        Pose2D(), WheelTicks(0, 0), WheelTicks(-250, 250), dt_s=1.0, **K
    )
    assert (pose.x, pose.y, pose.yaw) == pytest.approx((0.0, 0.0, 1.0), abs=1e-9)
    assert (tw.v, tw.w) == pytest.approx((0.0, 1.0), abs=1e-9)


def test_heading_matters():
    start = Pose2D(0.0, 0.0, math.pi / 2)
    pose, _ = odometry_step(
        start, WheelTicks(0, 0), WheelTicks(1000, 1000), dt_s=1.0, **K
    )
    assert (pose.x, pose.y) == pytest.approx((0.0, 1.0), abs=1e-9)


def test_reverse():
    pose, _ = odometry_step(
        Pose2D(), WheelTicks(0, 0), WheelTicks(-1200, -1000), dt_s=1.0, **K
    )
    assert (pose.x, pose.y) == pytest.approx((-1.078073235, -0.218536263), abs=1e-9)
