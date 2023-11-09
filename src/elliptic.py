from . import Loxodromic

class Elliptic(Loxodromic):

	def _get_shift(self, t):
		return self._samples * np.array([
			np.pi * t,
			        0
		])