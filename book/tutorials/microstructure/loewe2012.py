"""Implementation of poisson shot noise model

This module implements the shot noise model according to publication
`A Poisson shot noise model for micro-penetration of snow
<https://doi.org/10.1016/j.coldregions.2011.09.001>`_ by Henning Löwe
and Alec van Herwijnen, publicised in `Cold Regions Science and
Technology
<https://www.sciencedirect.com/journal/cold-regions-science-and-technology>`_,
Volume 70, January 2012, with one addition: As suggested in Proksch,
Henning Löwe and Martin Schneebeli, publicised in `Journal of
Geophysical Research: Earth Surface
<https://agupubs.onlinelibrary.wiley.com/journal/21699011>`_, Volume
120, Issue 2, February 2015, the force signals are detrended before
the force correlation function is computed.

"""

import math

import pandas as pd
from pandas import np as np
from scipy import signal

from windowing import chunkup, DEFAULT_WINDOW, DEFAULT_WINDOW_OVERLAP

#: Default value for SnowMicroPen's cone diameter im mm.
SMP_CONE_DIAMETER = 5  # [mm]
#: Default value for SnowMicroPen's projected cone area, depends on :const:`SMP_CONE_DIAMETER`.
SMP_CONE_AREA = (SMP_CONE_DIAMETER / 2.) ** 2 * math.pi  # [mm^2]


def calc_step(spatial_res, forces, cone_area=SMP_CONE_AREA):
    """Calculate shot noise parameters for a segment of a profile.

    This is the actual implementation of the algorithm described in the
    publication and calculates the derived parameters for a single segment of
    the profile.

    :param spatial_res: Spatial resolution of profile.
    :param forces: Iterable containing the force values.
    :param cone_area: Projected area of cone (tip) of SnowMicroPen in square
           millimeters.
    :return: A tuple containing lambda, f0, delta and L.
    """
    n = len(forces)

    # Mean and variance of force signal
    k1 = np.mean(forces)
    k2 = np.var(forces)

    # signal detrending as suggested by Proksch 2015
    force_detrended = signal.detrend(forces-k1, type='linear')
    
    # Covariance/Autocorrelation (Equation 8 in publication)
    c_f = np.correlate(force_detrended, force_detrended, mode='full')

    # Equation 11 in publication
    delta = -(3. / 2) * c_f[n - 1] / (c_f[n] - c_f[n - 1]) * spatial_res

    # Equation 12 in publication
    lambda_ = (4. / 3) * (k1 ** 2) / k2 / delta  # Intensity
    f0 = (3. / 2) * k2 / k1

    # According to equation 2 in publication
    L = (cone_area / lambda_) ** (1. / 3)

    return lambda_, f0, delta, L


def calc(samples, window=DEFAULT_WINDOW, overlap=DEFAULT_WINDOW_OVERLAP):
    """Calculation of shot noise model parameters.

    :param samples: A pandas dataframe with columns called 'distance' and 'force'.
    :param window: Size of moving window.
    :param overlap: Overlap factor in percent.
    :return: Pandas dataframe with the columns 'distance', 'force_median',
             'L2012_lambda', 'L2012_f0', 'L2012_delta', 'L2012_L'.
    """

    # Calculate spatial resolution of the distance samples as median of all
    # step sizes.
    spatial_res = np.median(np.diff(samples.distance.values))

    # Split dataframe into chunks
    chunks = chunkup(samples, window, overlap)
    result = []
    for center, chunk in chunks:
        f_median = np.median(chunk.force)
        sn = calc_step(spatial_res, chunk.force)
        result.append((center, f_median) + sn)
    return pd.DataFrame(result, columns=['distance', 'force_median', 'L2012_lambda', 'L2012_f0',
                                         'L2012_delta', 'L2012_L'])
