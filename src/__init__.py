from .loxodromic import Loxodromic
from .hyperbolic import Hyperbolic
from .elliptic import Elliptic

from numpy import seterr
seterr(divide='ignore', invalid='ignore')