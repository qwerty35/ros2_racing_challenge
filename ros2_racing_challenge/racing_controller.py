from typing import Optional

from ros2_racing_challenge_msgs.msg import CarCommand, CarState
import rclpy
from rclpy.node import Node


class RacingController(Node):
    def __init__(self) -> None:
        super().__init__('racing_controller')
        self.current_state: Optional[CarState] = None

        self.drive_publisher = self.create_publisher(
            CarCommand,
            '/racing/command',
            10,
        )
        self.state_subscriber = self.create_subscription(
            CarState,
            '/racing/state',
            self.state_callback,
            10,
        )
        self.timer = self.create_timer(0.05, self.timer_callback)

        self.get_logger().info(
            'Racing controller ready. '
        )

    def state_callback(self, msg: CarState) -> None:
        self.current_state = msg

    def timer_callback(self) -> None:
        command = CarCommand()
        if self.current_state is not None:
            command = self.compute_control(
                self.current_state
            )
        self.drive_publisher.publish(command)

    def compute_control(self, state: CarState) -> CarCommand:
        """
        Return a CarCommand message.

        - `acceleration` unit: m/s^2
        - `steering_rate` unit: rad/s
        - simulator limits: acceleration in [-4.5, 2.8],
          steering_rate in [-6.0, 6.0]
        """
        _ = state
        command = CarCommand()
        command.acceleration = 0.0
        command.steering_rate = 0.0
        return command


def main(args=None) -> None:
    rclpy.init(args=args)
    node = RacingController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
