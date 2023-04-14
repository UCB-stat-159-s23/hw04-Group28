import os
import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot
=======
>>>>>>> 11adb4830ca4c03ad0b0f0f097369be4927e97db
from ligotools import readligo
from ligotools import *

import inspect 
from scipy.io import wavfile
<<<<<<< HEAD
from ligotools import write_wavfile, reqshift 

def test_whiten():
    assert len(inspect.signature(utils.whiten).parameters) == 3
=======
from ligotools import write_wavfile, reqshift, plotting

def test_whiten():
	assert len(inspect.signature(whiten).parameters) == 3
>>>>>>> 11adb4830ca4c03ad0b0f0f097369be4927e97db

def test_write_wavfile():
    fs = 12345
    duration = 1
    freq = 234
    samples = np.linspace(0, duration, num=fs * duration, endpoint=False)
    data = np.sin(2 * np.pi * freq * samples)
    test_filename = "test_output.wav"
    write_wavfile(test_filename, fs, data)
<<<<<<< HEAD
    assert os.path.exists(test_filename)
    rate, loaded_data = wavfile.read(test_filename)
    assert rate == fs

=======
	
    assert os.path.exists(test_filename)
	
    rate, loaded_data = wavfile.read(test_filename)
    assert rate == fs



>>>>>>> 11adb4830ca4c03ad0b0f0f097369be4927e97db
def test_reqshift():
    data = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    fshift = 100
    sample_rate = 4096
    shifted_data = reqshift(data, fshift, sample_rate)
<<<<<<< HEAD
    expected_shifted_data = np.array([0., 1., 2., 3., 4., 5., 6., 7.])
    assert np.allclose(shifted_data, expected_shifted_data, rtol=1e-05, atol=1e-08)

#assertion test for plotting() function in utils.py
=======

    expected_shifted_data = np.array([0., 1., 2., 3., 4., 5., 6., 7.])
    assert np.allclose(shifted_data, expected_shifted_data, rtol=1e-05, atol=1e-08)
	



>>>>>>> 11adb4830ca4c03ad0b0f0f097369be4927e97db
def test_plotting():
    det = "L1"
    strain_H1_whitenbp = np.array([1, 2, 3, 4])
    strain_L1_whitenbp = np.array([5, 6, 7, 8])
    template_match = np.array([9, 10, 11, 12])
    time = np.linspace(0.1, 0.4, 4)  
    timemax = 0.6
    SNR = np.array([0.2, 0.3, 0.4, 0.5])
    eventname = "GW150914"
    plottype = "png"
    tevent = 0.4
    template_fft = np.array([0.5, 0.6, 0.7, 0.8])
    datafreq = np.array([0.3, 0.4, 0.5, 0.6])
    d_eff = 0.02
    freqs = np.array([0.5, 0.6, 0.7, 0.8])
    data_psd = np.array([0.9, 0.1, 0.11, 0.12])
    fs = 0.03

    if not os.path.exists('figures'):
        os.makedirs('figures')
<<<<<<< HEAD
        
=======

>>>>>>> 11adb4830ca4c03ad0b0f0f097369be4927e97db
    plotting(
        det,
        strain_H1_whitenbp,
        strain_L1_whitenbp,
        template_match,
        time,
        timemax,
        SNR,
        eventname,
        plottype,
        tevent,
        template_fft,
        datafreq,
        d_eff,
        freqs,
        data_psd,
        fs,
    )
# check that the figures were saved correctly
    assert plt.fignum_exists(1)
    assert plt.fignum_exists(2)
    assert plt.fignum_exists(3)