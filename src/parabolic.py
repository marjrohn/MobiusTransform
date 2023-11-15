import numpy as np
import matplotlib.pyplot as plt

from .base_transform import BaseTransform

class Parabolic(BaseTransform):

	def __init__(self, p, zoom=1, xstride=8, ystride=8, **kwargs):
		self._zoom = zoom
		self.set_fixed_point(p)

		super().__init__(xstride=xstride, ystride=ystride, **kwargs)

	def set_fixed_point(self, p):
		self._p = p

		self._xlim = None
		self._ylim = None

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
		t = np.linspace(-1, 1, 1 + self._gridsize, endpoint=True)
		
		x, y = np.meshgrid(t, t)
		
		return x + 1j*y

	def _get_shift(self, t):
		return self._gridsize * np.array([t, 0])

	def _apply(self, data):
		z = data
		p = self._p

		w = (1 / z) + p

		x, y = np.real(w), np.imag(w)
		
		a, b = self.get_axis_xlim()
		x[np.abs(x - p) > 2*(b - a)] = np.NaN

		a, b = self.get_axis_ylim()
		y[np.abs(y - p) > 2*(b - a)] = np.NaN

		return (x, y)

	def get_axis_xlim(self):
		if(self._xlim != None):
			return self._xlim

		x0 = np.real(self._p)
		self._xlim = (
			self._aspect_rate * (x0 - 10) / self._zoom,
			self._aspect_rate * (x0 + 10) / self._zoom
		)

		return self._xlim

	def get_axis_ylim(self):
		if(self._ylim != None):
			return self._ylim

		y0 = np.imag(self._p)
		self._ylim = (
			(y0 - 10) / self._zoom,
			(y0 + 10) / self._zoom
		)

		return self._ylim

