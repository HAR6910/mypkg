#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Sho Harukawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from mypkg.bowlingscore_node import BowlingScoreNode

def setup_module(module):
    if not rclpy.ok():
        rclpy.init()

def teardown_module(module):
    if rclpy.ok():
        rclpy.shutdown()

def test_strike_score():
    node = BowlingScoreNode()
    node.role = [10, 3, 4]
    score, frame = node.calculate_score()
    assert score == 24 

def test_spare_score():
    node = BowlingScoreNode()
    node.role = [5, 5, 3]
    score, frame = node.calculate_score()
    assert score == 16

def test_normal_score():
    node = BowlingScoreNode()
    node.role = [3, 6]
    score, frame = node.calculate_score()
    assert score == 9
