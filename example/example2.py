import multiversion
multiversion.require_version('mylib', '1.0')

import mylib
print ('mylib in %s: %s' % (__name__, mylib.version))

del __multiversion_mapping__

multiversion.require_version('mylib', '2.0')

import mylib
print ('mylib in %s: %s' % (__name__, mylib.version))