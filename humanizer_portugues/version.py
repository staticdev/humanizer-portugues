# Functions from coverage under the Apache License: http://www.apache.org/licenses/LICENSE-2.0

def _make_version(major, minor, patch, releaselevel, serial):
    """Create a readable version string from version_info tuple components."""
    assert releaselevel in ['alpha', 'beta', 'candidate', 'final']
    version = "%d.%d.%d" % (major, minor, patch)
    short = {'alpha': 'a', 'beta': 'b', 'candidate': 'rc', 'final': ''}[releaselevel]
    version += "%s%d" % (short, serial)
    return version

# Same semantics as sys.version_info.
version_info = (1, 0, 0, 'final', 0)
__version__ = _make_version(*version_info)
