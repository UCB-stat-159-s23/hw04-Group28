import pytest
import os
import numpy as np
from ligotools import readligo


def test_read_hdf5():
    filename = 'GW150914_4_template.hdf5'
    
    if os.path.isfile(filename):
        strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = read_hdf5(filename)

        assert strain is not None
        assert gpsStart is not None
        assert ts is not None
        assert qmask is not None
        assert shortnameList is not None
        assert injmask is not None
        assert injnameList is not None

        print("Passed: test_read_hdf5")
    else:
        print("Skipped: test_read_hdf5 (file not found)")
		
		
def test_loaddata():
    filename = 'L-L1_LOSC_4_V2-1126259446-32.hdf5'
    
    if os.path.isfile(filename):
        strain, time, channel_dict = loaddata(filename, 'L1')

        assert strain is not None
        assert time is not None
        assert channel_dict is not None

        print("Passed: test_loaddata")
    else:
        print("Skipped: test_loaddata (file not found)")
		
		
def test_dq2segs():
    filename = 'H-H1_LOSC_4_V2-1126259446-32.hdf5'

    if os.path.isfile(filename):
        strain, time, channel_dict = loaddata(filename, 'H1')

        seglist = dq2segs(channel_dict['DEFAULT'], time[0])
        assert isinstance(seglist, SegmentList)
        assert len(seglist) > 0
        print("Passed: test_dq2segs")
    else:
        print("Skipped: test_dq2segs (file not found)")
		
		
def test_dq_channel_to_seglist():
    filename = 'H-H1_LOSC_4_V2-1126259446-32.hdf5'

    if os.path.isfile(filename):
        strain, time, channel_dict = loaddata(filename, 'H1')

        seglist = dq_channel_to_seglist(channel_dict['DEFAULT'], fs=4096)
        assert len(seglist) > 0
        print("Passed: test_dq_channel_to_seglist")
    else:
        print("Skipped: test_dq_channel_to_seglist (file not found)")

