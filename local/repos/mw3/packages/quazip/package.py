# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install quazip
#
# You can edit this file again by typing:
#
#     spack edit quazip
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Quazip(CMakePackage):
    """QuaZip is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package (AKA Minizip) using Trolltech's Qt library."""

    
    homepage = "https://stachenov.github.io/quazip/"
    url = "https://github.com/stachenov/quazip/archive/refs/tags/v1.4.tar.gz"


    maintainers("pnsinha")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("GNU Library or Lesser General Public License version 2.0")

    version("1.4", sha256="79633fd3a18e2d11a7d5c40c4c79c1786ba0c74b59ad752e8429746fe1781dd6")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def cmake_args(self):
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = [
                "QUAZIP_QT_MAJOR_VERSION=5"
                ]
        return args
