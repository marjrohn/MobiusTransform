#from .parabolic import Parabolic
from .loxodromic import Loxodromic
from .elliptic import Elliptic
from .hyperbolic import Hyperbolic

from numpy import seterr
seterr(divide='ignore', invalid='ignore')