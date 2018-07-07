# Functions from coverage under the Apache License: http://www.apache.org/licenses/LICENSE-2.0

def _make_version(major, minor, patch, releaselevel, serial):
    """Create a readable version string from version_info tuple components."""
    assert releaselevel in ['alpha', 'beta', 'candidate', 'final']
    version = "%d.%d.%d" % (major, minor, patch)
    short = {'alpha': '-a.%d' % (serial), 'beta': '-b.%d' % (serial), 
        'candidate': '-rc.%d' % (serial), 'final': ''}[releaselevel]
    version += "%s" % (short)
    return version

# Same semantics as semver.org
version_info = (1, 1, 0, 'final', 0)
__version__ = _make_version(*version_info)
