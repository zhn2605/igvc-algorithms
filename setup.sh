#!/usr/bin/env bash
# Sets up a ROS machine (Ubuntu 24.04). Safe to re-run. See docs/setup.md.
set -euo pipefail

codename=$(. /etc/os-release && echo "${UBUNTU_CODENAME:-${VERSION_CODENAME:-}}")
if [ "$codename" != noble ]; then
    echo "error: ROS 2 Jazzy needs Ubuntu 24.04 (noble), this is '$codename'" >&2
    exit 1
fi

# ROS 2 Jazzy, following docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html
if [ ! -f /opt/ros/jazzy/setup.bash ]; then
    # ros-dev-tools hits dependency conflicts if apt can't see noble-updates
    if ! grep -rqs noble-updates /etc/apt/sources.list /etc/apt/sources.list.d/; then
        echo "error: add noble-updates and noble-backports to the Suites: line" \
            "in /etc/apt/sources.list.d/ubuntu.sources, then re-run" >&2
        exit 1
    fi

    sudo apt-get update
    sudo apt-get install -y software-properties-common curl
    sudo add-apt-repository -y universe

    # ros2-apt-source adds ROS's apt repository and its signing key
    version=$(curl -fsSL https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest |
        grep -F '"tag_name"' | awk -F'"' '{print $4}')
    curl -fsSL -o /tmp/ros2-apt-source.deb \
        "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${version}/ros2-apt-source_${version}.${codename}_all.deb"
    sudo dpkg -i /tmp/ros2-apt-source.deb

    sudo apt-get update
    sudo apt-get upgrade -y
    # ros-base, not desktop: no RViz/Qt, Foxglove replaces them
    sudo apt-get install -y ros-jazzy-ros-base ros-dev-tools
fi
