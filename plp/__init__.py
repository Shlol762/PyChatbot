"""
PyLangProcessor
~~~~~~~~~~~~~~~

A speech pattern recognition and response module.

:copyright: Copyright 2021-Present Shlok
:license: MIT License
"""


__title__ = "plp"
__author__ = "Shlok"
__license__ = "MIT"
__copyright__ = "Copyright 2021-Present Shlok"
__version__ = "0.00.0"

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

ver_tuple = __version__.split(".")

from typing import NamedTuple, Literal

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int

versioninfo: VersionInfo = VersionInfo(major=ver_tuple[0], minor=ver_tuple[1], micro=ver_tuple[2], releaselevel='final',
                                       serial='0')
