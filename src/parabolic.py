import numpy as np
import matplotlib.pyplot as plt

from .base_transform import BaseTransform

class Parabolic(BaseTransform):

	def __init__(self, p, zoom=1,, xstride=8, ystride=8, **kwargs):
		self.set_fixed_point(p)
		self.set_zoom(zoom)
		
		super().__init__(xstride=xstride, ystride=ystride, **kwargs)

		
	def get_fixed_point(self):
		return self._p

	def set_fixed_point(self, p):
		
		if(not self._ispoint2d(p)):
			raise ValueError(f"cannot interpret '{p}' as a 2d point.")

		self._p = p if isinstance(p, (int, float, complex)) else p[0] + 1j * p[1]

		self._xlim = None
		self._ylim = None

	def set_zoom(self, zoom):
		if(not isinstance(zoom, (int, float))):
			raise TypeError(f"'zoom' is expected to be a int or float, but received: f'{type(zoom)}'")

		self.zoom = min(10, max(1, zoom))

	def _ani_start(self):
		self.axis.set_xlim(self.get_axis_xlim())
		self.axis.set_ylim(self.get_axis_ylim())
		self.axis.axis('off')

		circles = []
		for z in [-.5, .5, -.5j, .5j]:
			z0 = z + self._p
			xy = (np.real(z0), np.imag(z0))
			circ = plt.Circle(xy, .5,
				facecolor='white',
				edgecolor='white',
				fill=True,
				animated=True,
				antialiased=True,
				rasterized=True,
				zorder=2
			)
			circles.append(circ)
			self.axis.add_patch(circ)

		return circles

	def _generate_data(self):
		t = np.linspace(-1, 1, 1 + self.gridsize, endpoint=True)
		
		x, y = np.meshgrid(t, t)
		
		return x + 1j*y

	def _get_shift(self, t):
		return self.gridsize * np.array([t, 0])

	def _apply(self, data):
		z = data
		p = self._p

		w = (1 / z) + p

		x, y = np.real(w), np.imag(w)
		
		return self._threshold(x, y)

	def get_axis_xlim(self):
		if(self._xlim != None):
			return self._xlim

		x0 = np.real(self._p)
		self._xlim = (
			self._aspect_rate * (x0 - (10 / self.zoom)),
			self._aspect_rate * (x0 + (10 / self.zoom))
		)

		return self._xlim

	def get_axis_ylim(self):
		if(self._ylim != None):
			return self._ylim

		y0 = np.imag(self._p)
		self._ylim = (
			y0 - (10 / self.zoom),
			y0 + (10 / self.zoom)
		)

		return self._ylim

