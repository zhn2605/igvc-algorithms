# ROS setup

This is only required for work with `ros/`. Core setup is in [getting-started.md](getting-started.md#setup).

## Ubuntu 24.04 shell
ROS 2 Jazzy requires Ubuntu 24.04:

| Machine | Ubuntu 24.04 shell |
|---|---|
| Ubuntu 24.04 | use directly |
| Windows | `wsl --install -d Ubuntu-24.04`; clone inside WSL, not under `/mnt/c` |
| Other Linux | `distrobox create --name jazzy --image ubuntu:24.04`, then `distrobox enter jazzy` |
| macOS | SSH into a Linux machine, or an Ubuntu 24.04 VM |

## Setup
From the repo root:

```bash
./setup.sh
```

Installs Jazzy, the apt packages in `ros/*/package.xml`, and `.venv-ros`. It is safe to rerun and you should re-run after `uv.lock` or a `package.xml` changes.

Each terminal (bash or zsh):

```bash
source /opt/ros/jazzy/setup.bash      # setup.zsh in zsh
source .venv-ros/bin/activate
```

## Build, run, and test
From the repo root:

```bash
python -m colcon build
source install/setup.bash             # setup.zsh in zsh

ros2 launch igvc_hello hello_launch.py
python -m colcon test --return-code-on-test-failure
```

- Always `python -m colcon`. Plain `colcon` uses the system Python, and nodes can't import `core/`.
- Never `pip install` into `.venv-ros`. It hides ROS's own versions of packages.
- View topics in [Foxglove](https://foxglove.dev): Open connection -> Foxglove WebSocket -> `ws://localhost:8765`
- On a shared network, set a unique `export ROS_DOMAIN_ID=<1-100>`.

## Troubleshooting

| Error | Fix |
|---|---|
| `ModuleNotFoundError: igvc_types` in a node | `rm -rf build install log`, rebuild with `python -m colcon build` |
| `No module named colcon` | wrong venv: `deactivate`, activate `.venv-ros` |
