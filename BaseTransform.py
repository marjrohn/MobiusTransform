import scipy
import numpy as np
np.seterr(divice='ignore', invalid='ignore')

import matplotlib.pyploy as plt
from matplotlib.animation import FuncAnimation

class BaseTransform:

	def __init__(self, 
		samples=512, 
		rstride=32, 
		astride=32,
		colors=[
			(0, 0, 0), (1, 1, 1)
		]
	):
		self.figure, self.axis = plt.subplots(layout='constrained')
		self.set_resolution(1280, 720)
		self.figure.get_layout_engine().set(
			w_pad=0, h_pad=0, hspace=0, wspace=0
		)

		self._rstride = rstride
		self._astride = astride
		self._colors  = colors

		self.set_samples(samples)


	def animate(self, filename, resolution=None, speed=(1, 1), frame_rate=30, duration=10):
		
		def call(frames, total_frames):
			print(f'frame = {1 + frames} / {total_frames}')

		def init():
			self.axis.set_xlim(self.get_axis_xlim())
			self.axis.set_ylim(self.get_axis_ylim())
			self.axis.axis('off')

			return self._polys

		def update(time):
			rtime, atime = time * np.array(speed) / 90
		
			return self._eval_polys_path(
				self.apply(self.shift_data(rtime, atime))
			) 
			
		FuncAnimation(self.figure, update,
			init_func=init,
			frames=np.linspace(0, duration, frame_rate*duration, endpoint=True),
			blit=True
		).save(filename,
			writer='ffmpeg',
			fps=frame_rate,
			progress_callback=call
		)

	def set_samples(self, samples):
		self.axis.clear()

		self._samples = samples

		self._data  = self.generate_data()
		self._path_slices = self._generate_polys_path()
		self._polys = self._initialize_polys()

	def set_rstride(self, rstride):
		self.axis.clear()

		self._rstride = rstride

		self._path_slices = self._generate_polys_path()
		self._polys = self._initialize_polys()

	def set_astride(self, astride):
		self.axis.clear()
		
		self._astride = astride

		self._path_slices = self._generate_polys_path()
		self._polys = self._initialize_polys()


	def set_resolution(self, width, height, dpi=72)
		self._aspect_rate = width / height

		self.figure.set_dpi(dpi)
		self.figure.set_figwidth(width / dpi)
		self.figure.set_figheight(height / dpi)
	
	def _generate_polys_path(self):
		return [
			[
				np.s_[   i:i+self._rstride,      j+self._astride],
				np.s_[     i+self._rstride, j+self._astride:j:-1],
				np.s_[i+self._rstride:i:-1,                    j],
				np.s_[                   i,  j:j+self._astride+1]
			]

			for i in range(0, self._samples, self._rstride)
			for j in range(0, self._samples, self._astride)
		]

	def _initialize_polys(self):
		polys = self.axis.fill(*[[], []]*len(self._path_slices),
			closed=True,
			linewidth=0,
			animated=True, 
			antialiased=True,
			rasterized=True,
		)

		color_index = [
			(i//self._rstride + j//self._astride) % len(self._colors)

			for i in range(0, self._samples, self._rstride)
			for j in range(0, self._samples, self._astride)
		]

		for poly, idx in zip(polys, color_index):
			poly.set_color(self._colors[idx])

		return polys

	def _eval_polys_path(self, data):
		
		X, Y = np.real(self._data), np.imag(self._data)

		for poly, sl in zip(self._polys, self._path_slices):
			poly.set_xy(np.column_stack([
				np.concatenate([X[s] for s in sl]),
				np.concatenate([Y[s] for s in sl])
			]))

		return self._polys

	def generate_data(self):
		raise NotImplementedError('This is a abstract method.')

	def shift_data(self, rtime, atime):
		raise NotImplementedError('This is a abstract method.')

	def apply(self, data):
		raise NotImplementedError('This is a abstract method.')

	def get_axis_xlim(self):
		raise NotImplementedError('This is a abstract method.')

	def get_axis_ylim(self):
		NotImplementedError('This is a abstract method.')

