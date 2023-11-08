import scipy as sp
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from . import BaseTransform

class LoxodromicTransform(BaseTransform):
	
	def __init__(self, p, q, **kwargs):
		self._p = p
		self._q = q

		super().__init__(**kwargs)
	
	
	def _get_shift(self, t):
		return self._samples * np.array([
			        t,
			np.pi * t
		])

	def _generate_data(self):
		r = np.exp(np.linspace(-8, 8, self._samples, endpoint=True))
		theta = np.linspace(-np.pi, np.pi, self._samples, endpoint=True)

		#virtual points
		r = np.concatenate([ r, [ r[-1] ] ])
		theta = np.concatenate([ theta, [ theta[-1] ] ])

		THETA, R = np.meshgrid(theta, r)
		
		return R * np.exp(1j * THETA)

	def _apply(self, data):
		z = data
		p, q = self._p, self._q

		w = (z * q - p) / (1 + z)
		x, y = np.real(w), np.imag(w)

		a, b = self.get_axis_xlim()
		x[np.abs(x) > (b - a)] = np.NaN

		a, b = self.get_axis_ylim()
		y[np.abs(y) > (b - a)] = np.NaN

		return (x, y)

	def _distance(self):
		x1, x2 = np.real(self._p), np.real(self._q)
		y1, y2 = np.imag(self._p), np.imag(self._q)
		
		return np.max([np.abs(x2 - x1), np.abs(y2 - y1)])

	def get_axis_xlim(self):
		x1, x2 = np.real(self._p), np.real(self._q)
		
		dist = self._distance()

		a = self._aspect_rate * np.min([x1, x2]) - dist / 2
		b = self._aspect_rate * np.max([x1, x2]) + dist / 2

		return (a, b)

	def get_axis_ylim(self):
		y1, y2 = np.imag(self._p), np.imag(self._q)
		
		dist = self._distance()

		a = np.min([y1, y2]) - dist / 2
		b = np.max([y1, y2]) + dist / 2

		return (a, b)

