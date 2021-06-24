"""Calculation of density and ssa.

This module implements the methods to derive density and specific surface area
(SSA) from SnowMicroPen's signal as described in publication
`Density, specific surface area, and correlation length of snow measured by
high‐resolution penetrometry <https://doi.org/10.1002/2014JF003266>`_ by Martin
Proksch, Henning Löwe and Martin Schneebeli, publicised in `Journal of
Geophysical Research: Earth Surface
<https://agupubs.onlinelibrary.wiley.com/journal/21699011>`_, Volume 120,
Issue 2, February 2015.
"""

from pandas import np as np
import pandas as pd

import loewe2012
import windowing

DENSITY_ICE = 917.


def calc_step(median_force, element_size):
    """Calculation of density and ssa from median of force and element size.

    This is the actual math described in the publication.

    :param median_force: Median of force.
    :param element_size: Element size.
    :return: Tuple containing density and ssa value.
    """
    l = element_size
    fm = median_force

    # Equation 9 in publication
    a1 = 420.47
    a2 = 102.47
    a3 = -121.15
    a4 = -169.96
    density = a1 + a2 * np.log(fm) + a3 * np.log(fm) * l + a4 * l

    # Equation 11 in publication
    c1 = 0.131
    c2 = 0.355
    c3 = 0.0291
    lc = c1 + c2 * l + c3 * np.log(fm)

    # Equation 12 in publication
    ssa = 4 * (1 - (density / DENSITY_ICE)) / lc

    return density, ssa


def calc_from_loewe2012(shotnoise_dataframe):
    """Calculate ssa and density from a pandas dataframe containing shot noise
    model values.

    :param shotnoise_dataframe: A pandas dataframe containing shot noise model values.
    :return: A pandas dataframe with the columns 'distance', 'P2015_density' and 'P2015_ssa'.
    """
    result = []
    for index, row in shotnoise_dataframe.iterrows():
        density, ssa = calc_step(row.force_median, row.L2012_L)
        result.append((row.distance, density, ssa))
    return pd.DataFrame(result, columns=['distance', 'P2015_density', 'P2015_ssa'])


def calc(samples, window=windowing.DEFAULT_WINDOW, overlap=windowing.DEFAULT_WINDOW_OVERLAP):
    """Calculate ssa and density from a pandas dataframe containing the samples
    of a SnowMicroPen recording.

    :param samples: A pandas dataframe containing the columns 'distance' and 'force'.
    :param window: Size of window in millimeters.
    :param overlap: Overlap factor in percent.
    :return: A pandas dataframe with the columns 'distance', 'P2015_density' and 'P2015_ssa'.
    """
    sn = loewe2012.calc(samples, window, overlap)
    result = []
    for index, row in sn.iterrows():
        density, ssa = calc_step(row.force_median, row.L2012_L)
        result.append((row.distance, density, ssa))
    return pd.DataFrame(result, columns=['distance', 'P2015_density', 'P2015_ssa'])
