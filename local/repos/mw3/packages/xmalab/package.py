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
#     spack install xmalab
#
# You can edit this file again by typing:
#
#     spack edit xmalab
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Xmalab(CMakePackage):
    """XMALab is software for marker-based fluoromicrometry and XROMM, with tools for standard (non-X-ray) video analysis as well. The developer is Dr. Ben Knorlein, a computer-vision expert and software engineer at the Center for Computation and Visualization at Brown University. XMALab has been described and validated in a peer-reviewed paper in the Journal of Experimental Biology. Publications using XMALab must provide attribution by citing: Knšrlein, B.J., Baier, D.B., Gatesy, S.M., Laurence-Chasen, J.D. and Brainerd, E.L. 2016. Validation of XMALab software for marker-based XROMM. Journal of Experimental Biology, 219: 3701-3711. doi:10.1242/jeb.145383."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://bitbucket.org/xromm/xmalab"
    url = "https://bitbucket.org/xromm/xmalab/get/a559d2523e90d9c849459e95c4c701dcc2f0a83f.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("2.1.0", sha256="902af77acfe99715bdfb4476e16734861476ecec07d5d3d84766bf56ce316e18")

    depends_on("qt@5.15.11")
    depends_on("opencv@4.8.0")
    depends_on("quazip@1.4")
    depends_on("levmar@2.6")
    depends_on("glew@2.2.0")

    # def cmake_args(self):
    #     args = [
    #         "LEVMAR_INCLUDE_DIR="
    #         "LEVMAR_LIBRARY"
    #         "QUAZIP_INCLUDE_DIR"
    #         "QUAZIP_LIBRARY"
    #         "QUAZIP_ZLIB_INCLUDE_DIR"
    #         "GLEW_INCLUDE_DIR"
    #         "GLEW_STATIC_LIBRARY_DEBUG"
    #     ]
    #     return args