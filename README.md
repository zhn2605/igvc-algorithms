# igvc-algorithms

Autonomy algorithms environment for IGVC AutoNav 2027

Rules summary: [docs/rules-summary.md](docs/rules-summary.md).
General setup: [docs/getting-started.md](docs/getting-started.md).

## Important
To maintain cross-platform compatibility for everyone and decouple logic from ROS, `core/` should never have ROS imports

## Layout

| Path | What |
|---|---|
| `core/` | All autonomy logic |
| `ros/` | Thin ROS 2 adapters around `core/` |
| `tests/` | Repo-wide checks |
| `docs/` | Documentation for setup, rules, etc. |

## Contributors

@RAdev-py
@yang-junwon
