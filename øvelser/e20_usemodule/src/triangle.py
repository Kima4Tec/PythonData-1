# Enter you module contents here
"""
Dette modul håndterer basale udregninger for retvinklede trekanter.
Du kan udregne længden af hypotenusen og arealet af den retvinklede trekant.
Der er desuden inkluderet forfatternavn og versionsnummer.
"""


import math

__author__ = "Kim M"
__version__ = "1.0"

def hypothenuse(a,b):
    """Finder længden af hypotenusen."""
    return math.sqrt(a**2 + b**2)

def area(a,b):
    """Finder trekantens areal."""
    return (a*b)/2