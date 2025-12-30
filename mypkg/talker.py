import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class BowlingTalker(Node):
    def __init__(self):
        super().__init__('bowling_talker')
        self.pub = self.create_publisher(Int32, '/bowling/roll', 10)
        self.timer = self.create_timer(1.0, self.publish_roll)

        self.frame = 1
        self.roll_in_frame = 1
        self.remaining_pins = 10

        self.get_logger().info('Bowling talker started')

    def publish_roll(self):
        if self.frame > 10:
            self.get_logger().info('All frames sent. Shutting down talker.')
            rclpy.shutdown()
            return

        pins = random.randint(0, self.remaining_pins)
        msg = Int32()
        msg.data = pins
        self.pub.publish(msg)

        self.get_logger().info(
            f'Frame {self.frame} Roll {self.roll_in_frame}: {pins}'
        )

        # フレーム進行管理
        if pins == 10 or self.roll_in_frame == 2:
            self.frame += 1
            self.roll_in_frame = 1
            self.remaining_pins = 10
        else:
            self.roll_in_frame = 2
            self.remaining_pins -= pins

def main():
    rclpy.init()
    node = BowlingTalker()
    rclpy.spin(node)

