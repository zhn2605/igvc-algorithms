"""ruff rejects ROS imports outside ros/."""

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parents[1]


def ruff_bans(code: str, pretend_path: str) -> bool:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "ruff",
            "check",
            "--no-cache",
            "--select",
            "TID251",
            "--stdin-filename",
            pretend_path,
            "-",
        ],
        input=code,
        text=True,
        capture_output=True,
        cwd=REPO_ROOT,
        check=False,
    )
    return result.returncode != 0


@pytest.mark.parametrize(
    "code",
    [
        "import rclpy\n",
        "from rclpy.node import Node\n",
        "from std_msgs.msg import String\n",
    ],
)
def test_ros_banned_in_core(code):
    assert ruff_bans(code, "core/igvc_types/src/igvc_types/x.py")


def test_ros_allowed_in_ros():
    assert not ruff_bans("import rclpy\n", "ros/igvc_ros_drive/x.py")


def test_other_imports_allowed_in_core():
    assert not ruff_bans("import numpy\n", "core/igvc_types/src/igvc_types/x.py")
