# ROS 2 Racing Challenge

Implement a vehicle controller for a ROS 2 racing simulator.

## Assignment Goal

Implement `racing_controller.py` so the vehicle can drive around the oval track.

Your controller should:

1. Drive stably without leaving the track
2. Pass the waypoint gates in order
3. Avoid the two obstacles on the track
4. Complete 10 laps as quickly as possible

## File To Modify

For the assignment, you should modify only this file:

```text
ros2_racing_challenge/racing_controller.py
```

Avoid modifying `racing_sim.py`, launch files, or message definitions so your solution stays compatible with the evaluation environment.

## Controller Interface

`racing_controller.py` already contains the basic publisher/subscriber structure.

- subscribe: `/racing/state`
- publish: `/racing/command`

The input `CarState` contains the current vehicle state.

```text
x         vehicle x position
y         vehicle y position
yaw       vehicle heading
speed     vehicle speed
steering  current steering angle
```

The output `CarCommand` is the command sent to the vehicle.

```text
acceleration   acceleration command in m/s^2
steering_rate  steering angle rate command in rad/s
```

The simulator applies the following command limits:

```text
acceleration:  -4.5 to 2.8
steering_rate: -6.0 to 6.0
```

## How To Run

Run the simulator, your controller, and RViz together:

```bash
ros2 launch ros2_racing_challenge racing.launch.py
```

Run the simulator, keyboard controller, and RViz together:

```bash
ros2 launch ros2_racing_challenge racing_keyboard.launch.py
```

## Keyboard Control

The following keys are available when using `racing_keyboard.launch.py`.

```text
a      steer left
d      steer right
w      return steering to zero
r      increase target speed
f      decrease target speed
space  maximum brake
x      release brake
q      quit
```

## Evaluation

The simulator reports the result based on the time required to complete 10 laps.

- Collision with an obstacle adds a time penalty.
- Leaving the track accumulates penalty time while the vehicle remains outside the track.
- Friction decreases randomly as laps progress, so the vehicle may become more slippery in later laps.
- The final score is the driving time plus accumulated penalty time.

You can check the lap count, time, penalty, and friction status in the RViz status text.
