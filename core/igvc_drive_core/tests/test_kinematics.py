import pytest
from igvc_drive_core.kinematics import twist_to_wheels, wheels_to_twist
from igvc_types import Twist2D, WheelSpeeds


def test_straight():
    assert twist_to_wheels(Twist2D(1.0, 0.0), 0.5) == WheelSpeeds(1.0, 1.0)


def test_spin_in_place():
    w = twist_to_wheels(Twist2D(0.0, 2.0), 0.5)
    assert (w.left, w.right) == pytest.approx((-0.5, 0.5))


def test_round_trip():
    t = Twist2D(0.8, -0.3)
    back = wheels_to_twist(twist_to_wheels(t, 0.5), 0.5)
    assert (back.v, back.w) == pytest.approx((t.v, t.w))


# your test
def test_example(): ...
