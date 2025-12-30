#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Sho Harukawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class BowlingScoreNode(Node):
    def __init__(self):
        super().__init__('bowling_score_node')
        self.sub = self.create_subscription(
            Int32, '/bowling/roll', self.roll_callback, 10
        )
        self.pub = self.create_publisher(
            String, '/bowling/score', 10
        )

        self.rolls = []
        self.get_logger().info('Bowling score node started')

    def roll_callback(self, msg):
        pins = msg.data
        if pins < 0 or pins > 10:
            self.get_logger().warn('Invalid roll value')
            return

        self.rolls.append(pins)
        score, frame = self.calculate_score()

        out = String()
        out.data = f'Frame: {frame} | Total Score: {score}'
        self.pub.publish(out)

def calculate_score(self):
    score = 0
    frame = 0
    i = 0

    while frame < 10 and i < len(self.rolls):
        # Strike
        if self.rolls[i] == 10:
            score += 10
            if i + 2 < len(self.rolls):
                score += self.rolls[i + 1] + self.rolls[i + 2]
            i += 1

        # Spare
        elif i + 1 < len(self.rolls) and self.rolls[i] + self.rolls[i + 1] == 10:
            score += 10
            if i + 2 < len(self.rolls):
                score += self.rolls[i + 2]
            i += 2

        # Normal
        else:
            if i + 1 < len(self.rolls):
                score += self.rolls[i] + self.rolls[i + 1]
            i += 2

        frame += 1

    return score, frame



def main(args=None):
    rclpy.init(args=args)
    node = BowlingScoreNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

