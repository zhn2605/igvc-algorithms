#!/usr/bin/env bash
# Sets up a ROS machine (Ubuntu 24.04). Safe to re-run. See docs/setup.md.
set -euo pipefail
cd "$(dirname "$0")"

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

# apt packages listed in ros/*/package.xml. --rosdistro instead of sourcing
# /opt/ros/jazzy/setup.bash, which trips set -u.
[ -f /etc/ros/rosdep/sources.list.d/20-default.list ] || sudo rosdep init
rosdep update --rosdistro jazzy
if ! rosdep check --from-paths ros --ignore-src --rosdistro jazzy >/dev/null 2>&1; then
    sudo apt-get update
    rosdep install --from-paths ros --ignore-src --rosdistro jazzy -y
fi

# The venv bridge: Ubuntu's python + ROS (system site-packages) + core packages.
# --no-dev keeps pytest/ruff out so they don't shadow ROS's apt versions.
if ! command -v uv >/dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi
[ -d .venv-ros ] || uv venv --system-site-packages --python /usr/bin/python3 .venv-ros
UV_PROJECT_ENVIRONMENT=.venv-ros uv sync --locked --no-dev

echo "done. to build: source /opt/ros/jazzy/setup.zsh (or .bash), source .venv-ros/bin/activate, python -m colcon build"
