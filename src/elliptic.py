import numpy as np

from . import Loxodromic

class Elliptic(Loxodromic):

	def _get_shift(self, t):
		return self.gridsize * np.array([
			np.pi * t,
			        0
		])