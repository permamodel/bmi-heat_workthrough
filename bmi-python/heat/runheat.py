# runheat.py
# simple python code to run the heat module under local bmi-python

from __future__ import absolute_import, division, print_function
import numpy as np
import yaml
import matplotlib.pyplot as plt

from heat import Heat
from bmi_heat import BmiHeat

if __name__ == '__main__':
    # Verify that this code is running
    print("Running runheat.py")

    # Create a bmi-heat object
    bheat = Heat()

    """
    # Write out the temperature array, so I can re-read it later
    bheat._temperature.tofile("bheat_inittemp.dat")
    """

    # Read in the temperature array, so it's consistent
    bheat._temperature = np.fromfile("bheat_inittemp.dat").reshape(10,20)

    # Write out a quick 10x20 floating point array
    bheat._temperature.astype('float32').tofile("tempcheck.dat")

    # Create an array with the output of the heat run
    harr = np.zeros((100, 10, 20))
    harr[0, :, :] = bheat._temperature

    for t in range(1, 100):
        print("t: %d" % t)

        bheat.advance_in_time()
        harr[t, :, :] = bheat._temperature

    # Write out the temperature time series
    harr.astype('float32').tofile("heatseries.dat")

    # Ending statement
    print("...Finished running runheat.py")

