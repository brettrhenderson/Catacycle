"""A python visualization package for generating data-rich catalytic cycle drawings"""

# Add imports here
from .catacycle import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
