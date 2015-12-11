'''
    SASSIE  Copyright (C) 2011 Joseph E. Curtis
    This program comes with ABSOLUTELY NO WARRANTY; 
    This is free software, and you are welcome to redistribute it under certain
    conditions; see http://www.gnu.org/licenses/gpl-3.0.html for details.
'''
# System imports
from distutils.core import *
from distutils      import sysconfig

# Third-party modules - we depend on numpy for everything
import numpy

# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

# simple extension module
_sasview_vmd = Extension("_sasview_vmd",
                   ["sasview_vmd.i","sasview_vmd.c","imd.c","vmdsock.c"],
                   include_dirs = [numpy_include],
                   )

# NumyTypemapTests setup
setup(  name        = "SASVIEW VMD I/O",
        description = "Module handles sending and receiving coordinates to VMD using numpy.i",
        author      = "Joseph E. Curtis",
        version     = "0.1",
        ext_modules = [_sasview_vmd]
        )

