# IGVC 2027 AutoNav - Rules Summary

This is a quick summary of competition rules and guidelines necessary for ALGORITHMS ONLY. Refer to the docs for full rules. This summary could also be inaccurate / outdated, in which case you should refer to the actual rules PDF (and fix here).

- Competition: June 4–8, 2027. 
- Design report due: May 15, 2027.
- Source: the team planning doc (09/04/26), which is based on the **2026** rules (http://www.igvc.org/2026rules.pdf).

## Rules that constrain software

- **Fully autonomous:** no remote control during a run, all compute onboard.
- **No mapping or memorization:** perceive and react live. Mapping *during* a run is fine. The course is rearranged between runs.
- **Speed band:** at least 1 mph (0.447 m/s) *average*. At most 5 mph (2.235 m/s), capped by hardware.
- **Start:** a judge starts the robot with one action.
- **Autonomy flag:** the safety light flashes in autonomous mode. We only report the mode, firmware integrates it to the light.
- **E-stops does not go through software.** Don't design anything that assumes software can stop the robot on an E-stop.
- **Robot size:** width 0.61–1.22 m, length 0.91–2.13 m. Check in with hardware / robot for actual measurements
- **Payload:** 20 lb (9.1 kg) on every run (affects acceleration)

## Course

| Item | Rule | SI |
|---|---|---|
| Surface | Asphalt, outdoors, varied lighting, possible light rain | |
| Length | ~500 ft | ~152 m |
| Lane width | 10–20 ft | 3.05–6.10 m |
| Min turning radius | ≥ 5 ft | ≥ 1.52 m |
| Lane shape | Mostly sinusoidal; also switchbacks, traps, and dead ends | |
| Lines | White, ~3–4 in wide, continuous or dashed | 0.076–0.10 m |
| Ramp | Up to 15% grade | |
| Obstacles | Barrels/drums of varying colors plus natural and manmade obstacles, randomized, ≥ 5 ft from lines | ≥ 1.52 m |
| Potholes | 2 ft solid white circles | 0.61 m diameter |
| GPS waypoints | Given in advance: No Man's Land entrance/exit and ramp approach | 2 m diameter target |
| Run time | 6 minutes | 360 s |

**Run-ending events:** crossing an internal lane line, driving over a pothole.

## Qualification (autonomy parts)

There will only be ONE software stack (no reconfiguration) and it needs to achieve all of the following:
1. Lane following.
2. Obstacle avoidance.
3. Navigating around an obstacle to a single 2 m waypoint.
4. Minimum speed sustained over the qualification distance (the team guide says the first 44 ft, 13.4 m; confirm).

## Scoring

- Rank by shortest adjusted time. If nobody finishes, rank by longest adjusted distance.
- Penalties for collisions and boundary crossings, in feet (1 ft = 1 s).

## Design report

- **Perception** and **Driving Logic** (most likely). We likely contribute to cybersecurity too (the laptop, wireless links).
- Each section needs stated requirements with target values **and measured results**.
- The report must also cover testing, bug tracking, version control, the simulation testing process, and sim-vs-real differences.

## Algorithm tasks

| Task | Pass |
|---|---|
| Lane perception | Keeps the robot in-lane through curves |
| Obstacle and pothole perception | Enough range and accuracy to avoid them with ≥ 5 ft clearance |
| Localization and GPS waypoints | Reaches the waypoints using only live sensing |
| Path planning and avoidance | Collision-free, in-bounds, real time; finishes within 6 min or maximizes distance |
| Control commands | Smooth, in-bounds motion within the speed band |

**Stuff that needs to be checked in with other subteams:**
- **Firmware:** the command interface (format, rate, units, safety semantics) → `serial-protocol.md`.
- **Hardware:** sensor type, count, position, and field of view, agreed before mounts are built.
- **Hardware + Firmware:** the compute and sensor power draw, agreed before battery sizing.
