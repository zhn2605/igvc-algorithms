# Getting Started
For pure development on algorithms software, anyone can install the uv package manager and develop directly in `core/`. This helps us avoid specific OS restrictions and dependency issues. (You do not need anything ROS related, until you wish to integrate with ROS).

That being said, do not add any ROS imports in `core/`. That means no `rclpy`, `*_msgs`, `rosidl_*`, etc.

 This is less of a suggestion, and more of a must-do... (see below in the Git and CI section).

For ROS work see: [ros-setup.md](ros-setup.md)

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```bash
git clone https://github.com/zhn2605/igvc-algorithms.git
cd igvc-algorithms
uv sync
uv run pytest
```

All tests should pass.

## Git

```bash
git switch main
git pull
git switch -c <topic>
# commit, push, open a pull request into dev/main
```

Important:
- Run `uv run ruff format` before pushing. This formats code to keep styling consistent.
- Run `uv run ruff check` before pushing. This catches likely bugs (e.g. unused or undefined names) and ROS imports in `core/`.
- Every pull request runs those checks and tests on Linux, macOS, and Windows (and an addition ROS test) 
- Merging into dev or main requires a pull request with all CI checks passing.

## CI

| Check | Step | Fix |
|---|---|---|
| `core (...)` | Format check | `uv run ruff format` |
| `core (...)` | Lint | `uv run ruff rule <CODE>` explains the rule |
| `core (...)` | Test | `uv run pytest`, fix locally |
| `core (...)` | Install dependencies | `uv sync`, commit `uv.lock` |
| `ros` | any | read the log, but usually due to a `core/` change that broke an adapter |

## Adding code
Core
- To make a new core package (example): `uv init --lib --vcs none core/igvc_perception_core`
- Tests go in the package's `tests/` folder. `uv run pytest core/<package>` tests one package.

ROS
- New ROS dependency: add it to `package.xml`, re-run `./setup.sh`.
- Minimal ROS package example: `ros/igvc_hello`.
