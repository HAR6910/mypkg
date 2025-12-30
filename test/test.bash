#!/bin/bash
# SPDX-FileCopyrightText: 2025 Sho Harukawa
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

from mypkg.bowlingscore_node import BowlingScoreNode


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

