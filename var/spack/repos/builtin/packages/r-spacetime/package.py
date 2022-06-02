# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacetime(RPackage):
    """Classes and Methods for Spatio-Temporal Data.

    Classes and methods for spatio-temporal data, including space-time regular
    lattices, sparse lattices, irregular data, and trajectories; utility
    functions for plotting data as map sequences (lattice or animation) or
    multiple time series; methods for spatial and temporal selection and
    subsetting, as well as for spatial/temporal/spatio-temporal matching or
    aggregation, retrieving coordinates, print, summary, etc."""

    cran = "spacetime"

    version('1.2-6', sha256='8fd46606ed9589ffce19368d40004890f96e8fe77f13b546e6a2f8b9ced0dd81')
    version('1.2-5', sha256='8f2acc3886780a902fb0476d6ab271e6640be1a1af4c7f9a21d8a2882fb72746')
    version('1.2-3', sha256='ca7c0b962d5da0741f6dd85b271d693598756e0eeeb364ada828dbb6d1b9b25b')
    version('1.2-2', sha256='1e9d3f92e5c4614a69c82a58bf0b5c829b4ed262bf1250bef943ae286056ea2d')

    depends_on('r@3.0.0:', type=('build', 'run'))
    depends_on('r-lattice', type=('build', 'run'))
    depends_on('r-sp@1.1-0:', type=('build', 'run'))
    depends_on('r-zoo@1.7-9:', type=('build', 'run'))
    depends_on('r-xts@0.8-8:', type=('build', 'run'))
    depends_on('r-intervals', type=('build', 'run'))
