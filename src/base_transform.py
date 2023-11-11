import scipy as sp
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class BaseTransform:

	def __init__(self, 
		samples=512, 
		xstride=16, 
		ystride=8,
		colors=[
			'white', 'black'
		]
	):
		self.figure, self.axis = plt.subplots(layout='constrained')
		self.set_resolution((1280, 720), dpi=72)
		self.figure.get_layout_engine().set(
			w_pad=0, h_pad=0, hspace=0, wspace=0
		)

		self._xstride = xstride
		self._ystride = ystride
		self._colors  = colors

		self.set_samples(samples)


	def create_image(self, filename, resolution=None, dpi=None):
		self.set_resolution(resolution, dpi=dpi)

		self.axis.set_xlim(self.get_axis_xlim())
		self.axis.set_ylim(self.get_axis_ylim())
		self.axis.axis('off')

		self._eval_polys_path(*self._apply(self._data))

		self.figure.savefig(filename, pad_inches=0, dpi=self.figure.dpi)


	def create_video(self, filename, 
		resolution=None, 
		dpi=None, 
		speed=1, 
		frame_rate=30, 
		duration=15
	):

		self.set_resolution(resolution, dpi=dpi)

		def call(frames, total_frames):
			print(f'frame = {1 + frames} / {total_frames}')

		def init():
			self.axis.set_xlim(self.get_axis_xlim())
			self.axis.set_ylim(self.get_axis_ylim())
			self.axis.axis('off')

			return self._polys

		def update(time):
			return self._eval_polys_path(*self._apply(
				self._shift_data(speed * time / 90)
			)) 
			
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

		self._data  = self._generate_data()
		self._path_slices = self._generate_polys_path()
		self._polys = self._initialize_polys()

	def set_xstride(self, xstride):
		self.axis.clear()

		self._xstride = xstride

		self._path_slices = self._generate_polys_path()
		self._polys = self._initialize_polys()

	def set_ystride(self, ystride):
		self.axis.clear()
		
		self._ystride = ystride

		self._path_slices = self._generate_polys_path()
		self._polys = self._initialize_polys()

	def set_colors(self, colors):
		self._axis.clear()

		self._colors = colors

		self._polys = self._initialize_polys()

	def set_resolution(self, resolution, dpi=None):
		
		if(resolution == None and dpi == None):
			pass

		if (resolution == None):
			width  = self.figure.get_figwidth()  * self.figure.dpi
			height = self.figure.get_figheight() * self.figure.dpi
		else:
			width  = resolution[0]
			height = resolution[1]

		if(dpi == None):
			dpi = self.figure.dpi

		self._aspect_rate = width / height

		self.figure.set_dpi(dpi)
		self.figure.set_figwidth(width / dpi)
		self.figure.set_figheight(height / dpi)
	
	def _generate_polys_path(self):
		s = len(self._colors)

		return [
			[
				np.s_[   i:i+self._xstride,      j+self._ystride],
				np.s_[     i+self._xstride, j+self._ystride:j:-1],
				np.s_[i+self._xstride:i:-1,                    j],
				np.s_[                   i,  j:j+self._ystride+1]
			]

			for i in range(0, self._samples, self._xstride)
			for j in range(0, self._samples, self._ystride)
			if( (i//self._xstride + j//self._ystride) % s < s - 1 )
		]

	def _initialize_polys(self):
		polys = self.axis.fill(*[[], []]*len(self._path_slices),
			closed=True,
			linewidth=0,
			animated=True, 
			antialiased=True,
			rasterized=True,
		)

		self.figure.set_facecolor(self._colors[0])
		
		s = len(self._colors)
		color_index = [
			(i//self._xstride + j//self._ystride) % s

			for i in range(0, self._samples, self._xstride)
			for j in range(0, self._samples, self._ystride)
			if( (i//self._xstride + j//self._ystride) % s < s - 1)
		]

		for poly, idx in zip(polys, color_index):
			poly.set_color(self._colors[1 + idx])

		return polys

	def _eval_polys_path(self, x, y):

		for poly, sl in zip(self._polys, self._path_slices):
			poly.set_xy(np.column_stack([
				np.concatenate([x[s] for s in sl]),
				np.concatenate([y[s] for s in sl])
			]))

		return self._polys

	def _shift_data(self, t):
		shift = self._get_shift(t)

		return sp.ndimage.shift(self._data, shift, 
			prefilter=False, 
			order=3, 
			mode='wrap'
		)

	def _generate_data(self):
		raise NotImplementedError('This is a abstract method.')

	def _get_shift(self, t):
		raise NotImplementedError('This is a abstract method.')

	def _apply(self, data):
		raise NotImplementedError('This is a abstract method.')

	def get_axis_xlim(self):
		raise NotImplementedError('This is a abstract method.')

	def get_axis_ylim(self):
		raise NotImplementedError('This is a abstract method.')

