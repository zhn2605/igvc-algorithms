import dataclasses
import math

import pytest
from igvc_types import Pose2D, wrap_angle


def test_wrap_angle():
    assert wrap_angle(3 * math.pi / 2) == pytest.approx(-math.pi / 2)
    assert wrap_angle(-3 * math.pi / 2) == pytest.approx(math.pi / 2)


def test_compose_drives_forward_in_robot_frame():
    p = Pose2D(1.0, 0.0, math.pi / 2).compose(Pose2D(1.0, 0.0, 0.0))
    assert (p.x, p.y, p.yaw) == pytest.approx((1.0, 1.0, math.pi / 2))


def test_inverse_undoes_compose():
    p = Pose2D(2.0, -1.0, 2.5)
    q = p.compose(p.inverse())
    assert (q.x, q.y, q.yaw) == pytest.approx((0.0, 0.0, 0.0), abs=1e-12)


def test_frozen():
    with pytest.raises(dataclasses.FrozenInstanceError):
        Pose2D().x = 1.0
