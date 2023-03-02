"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
import sys
sys.path.append('..')
from acp_times import *
import arrow

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


start_time = arrow.get("2000-06-03 00:00", "YYYY-MM-DD HH:mm")

def test_acp_1():
    brevet_dist = 200
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3 , minutes=30)),
        150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10, minutes=0)),
        200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=30))
    }

    for point, time_tuple in checkpoints.items():
        opening_time, closing_time = time_tuple
        assert open_time(point, brevet_dist, start_time) == opening_time
        assert close_time(point, brevet_dist, start_time) == closing_time
        

def test_acp_2():
    brevet_dist = 300
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6 , minutes=40)),
        200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=20)),
        300: (start_time.shift(hours=9, minutes=0), start_time.shift(hours=20, minutes=0)),
        320: (start_time.shift(hours=9, minutes=0), start_time.shift(hours=20, minutes=0))
    }

    for point, time_tuple in checkpoints.items():
        opening_time, closing_time = time_tuple
        assert open_time(point, brevet_dist, start_time) == opening_time
        assert close_time(point, brevet_dist, start_time) == closing_time


def test_acp_3():
    brevet_dist = 400
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3 , minutes=30)),
        150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10, minutes=0)),
        250: (start_time.shift(hours=7, minutes=27), start_time.shift(hours=16, minutes=40)),
        400: (start_time.shift(hours=12, minutes=8), start_time.shift(hours=27, minutes=0))
    }

    for point, time_tuple in checkpoints.items():
        opening_time, closing_time = time_tuple
        assert open_time(point, brevet_dist, start_time) == opening_time
        assert close_time(point, brevet_dist, start_time) == closing_time


def test_acp_4():
    brevet_dist = 600
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3 , minutes=30)),
        350: (start_time.shift(hours=10, minutes=34), start_time.shift(hours=23, minutes=20)),
        550: (start_time.shift(hours=17, minutes=8), start_time.shift(hours=36, minutes=40)),
        600: (start_time.shift(hours=18, minutes=48), start_time.shift(hours=40, minutes=0))
    }

    for point, time_tuple in checkpoints.items():
        opening_time, closing_time = time_tuple
        assert open_time(point, brevet_dist, start_time) == opening_time
        assert close_time(point, brevet_dist, start_time) == closing_time  


def test_acp_5():
    brevet_dist = 1000
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3 , minutes=30)),
        500: (start_time.shift(hours=15, minutes=28), start_time.shift(hours=33 , minutes=20)),
        700: (start_time.shift(hours=22, minutes=22), start_time.shift(hours=48, minutes=45)),
        1200: (start_time.shift(hours=33, minutes=5), start_time.shift(hours=75, minutes=0))
    }

    for point, time_tuple in checkpoints.items():
        opening_time, closing_time = time_tuple
        assert open_time(point, brevet_dist, start_time) == opening_time
        assert close_time(point, brevet_dist, start_time) == closing_time

test_acp_1()
test_acp_2()
test_acp_3()
test_acp_4()
test_acp_5()