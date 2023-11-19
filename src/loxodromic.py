import scipy as sp
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from .base_transform import BaseTransform

class Loxodromic(BaseTransform):
	
	def __init__(self, p, q, zoom=(1, -1), **kwargs):
		self.set_fixed_points(p, q)
		self.set_zoom(zoom)
		
		super().__init__(**kwargs)
		
	def get_fixed_points(self):
		return (self._p, self._q)

	def set_fixed_points(self, p, q):
		if(any(not self._ispoint2d(x) for x in [p, q])):
			raise ValueError(f"cannot interpret '{p}' or '{q}' as a 2d point.")

		self._p = p if isinstance(p, (int, float, complex)) else p[0] + 1j * p[1]
		self._q = q if isinstance(p, (int, float, complex)) else q[0] + 1j * q[1]

		self._center = .5 * (self._p + self._q)

		self._xlim = None
		self._ylim = None

	def set_zoom(self, zoom):
		if(not self._ispoint2d(zoom)):
			raise ValueError("unexpected value for 'zoom', received : {zoom}")

		if(isinstance(zoom, complex)):
			self.zoom = [np.real(zoom), np.imag(zoom)]
		elif(isinstance(zoom, (int, float))):
			self.zoom = [zoom, -1]
		else:
			self.zoom = zoom.tolist() if isinstance(zoom, numpy.ndarray) else list(zoom)

		self.zoom[1] = int(self.zoom[1])
		if(not self.zoom[1] in [-1, 0, 1]):
			raise ValueError("second value of 'zoom' should be -1, 0 or 1")

		dist = self._distance()
		self.zoom[0] = min(dist, max(1, self.zoom[0])) 
		
		if(self.zoom[1] != -1):		
			point = (self._p, self._q)[self.zoom[1]]	
			alpha = (self.zoom[0] - 1) / dist	
			self._center = self._center + alpha * (point - self._center)

	def _get_shift(self, t):
		return self.gridsize * np.array([
			np.pi * t,
			        t
		])

	def _generate_data(self):
		r = np.exp(np.linspace(-8, 8, 1 + self.gridsize, endpoint=True))
		theta = np.linspace(0, 2*np.pi, 1 + self.gridsize, endpoint=True)

		R, THETA = np.meshgrid(r, theta)
		
		return R * np.exp(1j * THETA)

	def _apply(self, data):
		z = data
		p, q, c = self._p, self._q, self._center

		w = (p - z * q) / (1 - z)
		x, y = np.real(w), np.imag(w)

		return self._threshold(x, y)

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
			self._aspect_rate * (xcenter - dist / self.zoom[0]),	
			self._aspect_rate * (xcenter + dist / self.zoom[0])
		)

		return self._xlim

	def get_axis_ylim(self):
		if (self._ylim != None):
			return self._ylim

		ycenter = np.imag(self._center)
		dist = self._distance()

		self._ylim = (
			ycenter - (dist / self.zoom[0]),
			ycenter + (dist / self.zoom[0])
		)

		return self._ylim
