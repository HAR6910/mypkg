import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Empty

class BowlingListener(Node):
    def __init__(self):
        super().__init__('bowling_listener')
        self.sub = self.create_subscription(
            Int32, '/bowling/roll', self.callback, 10
        )

        self.rolls = []
        self.frame = 0

        self.get_logger().info('Bowling listener started')

    def callback(self, msg):
        self.rolls.append(msg.data)
        score, frame = self.calculate_score()

        self.get_logger().info(
            f'Current Frame: {frame} | Total Score: {score}'
        )

        if frame >= 10:
            self.get_logger().info('Game finished!')
            self.get_logger().info(f'Final Score: {score}')
            rclpy.shutdown()

    def calculate_score(self):
        score = 0
        frame = 0
        i = 0

        while frame < 10 and i < len(self.rolls):
            if self.rolls[i] == 10:  # Strike
                score += 10
                if i + 2 < len(self.rolls):
                    score += self.rolls[i+1] + self.rolls[i+2]
                i += 1
            elif i + 1 < len(self.rolls) and self.rolls[i] + self.rolls[i+1] == 10:
                score += 10
                if i + 2 < len(self.rolls):
                    score += self.rolls[i+2]
                i += 2
            else:
                if i + 1 < len(self.rolls):
                    score += self.rolls[i] + self.rolls[i+1]
                i += 2
            frame += 1

        return score, frame

def main():
    rclpy.init()
    node = BowlingListener()
    rclpy.spin(node)

