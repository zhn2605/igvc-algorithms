"""
Core value types used throughout core logic, in SI units, radians, integer nanoseconds.
Frames follow ROS conventions: x forward, y left, yaw counterclockwise-positive.
"""

import math
from dataclasses import dataclass


def wrap_angle(a: float) -> float:
    """Wrap angle to [-pi, pi]."""
    return math.remainder(a, math.tau)


@dataclass(frozen=True, slots=True)
class Stamped[T]:
    """A value plus when it was measured and which frame it is expressed in."""

    t_ns: int
    frame_id: str
    value: T


@dataclass(frozen=True, slots=True)
class Pose2D:
    """Position (m) and heading (rad) in the plane."""

    x: float = 0.0
    y: float = 0.0
    yaw: float = 0.0

    def compose(self, other: "Pose2D") -> "Pose2D":
        """Apply `other`, expressed in this pose's frame."""
        c, s = math.cos(self.yaw), math.sin(self.yaw)
        return Pose2D(
            self.x + c * other.x - s * other.y,
            self.y + s * other.x + c * other.y,
            wrap_angle(self.yaw + other.yaw),
        )

    def inverse(self) -> "Pose2D":
        """The pose that undoes this one: p.compose(p.inverse()) is the identity."""
        c, s = math.cos(self.yaw), math.sin(self.yaw)
        return Pose2D(
            -c * self.x - s * self.y,
            s * self.x - c * self.y,
            wrap_angle(-self.yaw),
        )


@dataclass(frozen=True, slots=True)
class Twist2D:
    """Body-frame velocity: v forward (m/s), w counterclockwise yaw rate (rad/s)."""

    v: float = 0.0
    w: float = 0.0


@dataclass(frozen=True, slots=True)
class WheelSpeeds:
    """Wheel ground speeds (m/s), positive is forward."""

    left: float = 0.0
    right: float = 0.0


@dataclass(frozen=True, slots=True)
class WheelTicks:
    """Cumulative encoder counts. Odometry uses the change between two readings."""

    left: int = 0
    right: int = 0


@dataclass(frozen=True, slots=True)
class McuStatus:
    """Flags from each MCU telemetry frame."""

    estop: bool = False
    watchdog_tripped: bool = False
    fault: bool = False
