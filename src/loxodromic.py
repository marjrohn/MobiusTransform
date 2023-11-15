import scipy as sp
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from .base_transform import BaseTransform

class Loxodromic(BaseTransform):
	
	def __init__(self, p, q, **kwargs):
		self.set_fixed_points(p, q)
		super().__init__(**kwargs)
		
	def set_fixed_points(self, p, q):
		self._p = p
		self._q = q
		self._center = .5 * (p + q)

		self._xlim = None
		self._ylim = None

	def _get_shift(self, t):
		return self._gridsize * np.array([
			np.pi * t,
			        t
		])

	def _generate_data(self):
		r = np.exp(np.linspace(-8, 8, 1 + self._gridsize, endpoint=True))
		theta = np.linspace(0, 2*np.pi, 1 + self._gridsize, endpoint=True)

		R, THETA = np.meshgrid(r, theta)
		
		return R * np.exp(1j * THETA)

	def _apply(self, data):
		z = data
		p, q, c = self._p, self._q, self._center

		w = (p - z * q) / (1 - z)
		x, y = np.real(w), np.imag(w)

		a, b = self.get_axis_xlim()
		x[np.abs(x - c) > 2*(b - a)] = np.NaN

		a, b = self.get_axis_ylim()
		y[np.abs(y - c) > 2*(b - a)] = np.NaN

		return (x, y)

	def _distance(self):
		x1, x2 = np.real(self._p), np.real(self._q)
		y1, y2 = np.imag(self._p), np.imag(self._q)
		
		return np.max([np.abs(x2 - x1), np.abs(y2 - y1)])

	def get_axis_xlim(self):
		if (self._xlim != None):
			return self._xlim

		xcenter = np.real(self._center)
		dist = self._distance()

		self._xlim = (
			self._aspect_rate * (xcenter - dist),	
			self._aspect_rate * (xcenter + dist)
		)

		return self._xlim

	def get_axis_ylim(self):
		if (self._ylim != None):
			return self._ylim

		ycenter = np.imag(self._center)
		dist = self._distance()

		self._ylim = (
			ycenter - dist,
			ycenter + dist
		)

		return self._ylim
