import numpy as np

from . import Loxodromic

class Hyperbolic(Loxodromic):
	
	def _get_shift(self, t):
		return self._samples * np.array([
			0,
			t
		])