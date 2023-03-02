import sys
sys.path.append('..')
from mongodb import brevet_insert, brevet_fetch

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_brevet_functions_1():
    # insert test data
    brev_dist = 200
    begin_date = "2000-06-03T00:00:00"
    checkpoints = {"miles": 0.0, "km": 0, "open_time": '2000-06-03T00:00', "close_time": '2000-06-03T01:00' 
    }
    brevet_insert(brev_dist, begin_date, checkpoints)
    
    # fetch the inserted data
    fetched_dist, fetched_date, fetched_checkpoints = brevet_fetch()
    
    # check if the fetched data matches the original
    assert fetched_dist == brev_dist
    assert fetched_date == begin_date
    assert fetched_checkpoints == checkpoints


def test_brevet_functions_2():
    # insert test data
    brev_dist = 200
    begin_date = "2000-06-03T00:00:00"
    checkpoints = {"miles": 62.1371, "km": 100, "location": "Paris", "open_time": '2000-06-03T02:56', "close_time": '2000-06-03T06:40' 
    }
    brevet_insert(brev_dist, begin_date, checkpoints)
    
    # fetch the inserted data
    fetched_dist, fetched_date, fetched_checkpoints = brevet_fetch()
    
    # check if the fetched data matches the original
    assert fetched_dist == brev_dist
    assert fetched_date == begin_date
    assert fetched_checkpoints == checkpoints


test_brevet_functions_1()
test_brevet_functions_2()