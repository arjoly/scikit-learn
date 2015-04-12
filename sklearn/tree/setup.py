import os

import numpy
from numpy.distutils.misc_util import Configuration


def configuration(parent_package="", top_path=None):
    config = Configuration("tree", parent_package, top_path)
    libraries = []
    if os.name == 'posix':
        libraries.append('m')
    config.add_extension("_tree",
                         sources=["_tree.c"],
                         include_dirs=[numpy.get_include()],
                         libraries=libraries,
                         extra_compile_args=["-O3"])
    config.add_extension("_utils",
                         sources=["_utils.c"],
                         include_dirs=[numpy.get_include()],
                         libraries=libraries,
                         extra_compile_args=["-O3"])

    # config.add_extension("_noise",
    #                  sources=["_noise.pyx", "_noise.cpp"],
    #                  extra_compile_args=["-std=c++11"],
    #                  language="c++",
    #                  include_dirs=[numpy.get_include()],
    #                  libraries=libraries)


    config.add_subpackage("tests")

    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup, Extension
    # from Cython.Build import cythonize

    # setup(ext_modules = cythonize(Extension(
    #        "_noise",                                # the extesion name
    #        sources=["_noise.pyx", "Noise.cpp"], # the Cython source and c++ file
    #        extra_compile_args=["-std=c++11"],
    #        language="c++",
    #   )))
    setup(**configuration().todict())


