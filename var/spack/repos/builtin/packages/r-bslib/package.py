# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBslib(RPackage):
    """Custom 'Bootstrap' 'Sass' Themes for 'shiny' and 'rmarkdown'.

    Simplifies custom 'CSS' styling of both 'shiny' and 'rmarkdown' via
    'Bootstrap' 'Sass'. Supports both 'Bootstrap' 3 and 4 as well as their
    various 'Bootswatch' themes. An interactive widget is also provided for
    previewing themes in real time."""

    cran = "bslib"

    version("0.4.1", sha256="4ebd1fc84cd19b414e8f8c13fb95270fc28ede125b6e58b08c574ca8c9e0e62f")
    version("0.4.0", sha256="fbea4ecec726f23618e825624f1d9c03939f765ca5a490b171ebf95b815475c2")
    version("0.3.1", sha256="5f5cb56e5cab9039a24cd9d70d73b69c2cab5b2f5f37afc15f71dae0339d9849")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-htmltools@0.5.2:", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-sass@0.4.0:", type=("build", "run"))
    depends_on("r-jquerylib@0.1.3:", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-memoise", type=("build", "run"), when="@0.4.0:")
    depends_on("r-memoise@2.0.1:", type=("build", "run"), when="@0.4.1:")
    depends_on("r-cachem", type=("build", "run"), when="@0.4.0:")
