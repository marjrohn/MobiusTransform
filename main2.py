import numpy as np
np.seterr(divide='ignore', invalid='ignore')

import scipy

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n_points = 2**9
n_circles = 2**6
n_lines = 2**5

i_stride = (n_points // n_lines) 
j_stride = (n_points // n_circles)

slices = []

for i in range(0, n_points, i_stride): 
	for j in range(0, n_points, j_stride):  
		if ( (i//i_stride + j//j_stride) % 2 == 0 ):
				
			slices.append([
				np.s_[i:i+i_stride, j+j_stride],
				np.s_[i+i_stride, j+j_stride:j:-1],
				np.s_[i+i_stride:i:-1, j],
				np.s_[i, j:j+j_stride+1]
			])


DPI = 72
aspect = 16 / 9
h = 720 / DPI
w = aspect * h

fig, ax = plt.subplots(figsize=(w, h), dpi=DPI, facecolor='white', layout='constrained')
fig.get_layout_engine().set(
	w_pad=0, h_pad=0, hspace=0, wspace=0
)

polys = ax.fill(*[[], []]*len(slices),
	closed=True,
	facecolor='black', 
	linewidth=0,
	animated=True, 
	antialiased=True,
	rasterized=True,
)

r = np.exp(np.linspace(-8, 8, n_points, endpoint=True))
theta = np.linspace(-np.pi, np.pi, n_points, endpoint=True)

#virtual points
r = np.concatenate([ r, [ r[-1] ] ])
theta= np.concatenate([ theta, [ theta[-1] ] ])

R, THETA = np.meshgrid(r, theta)
Z = R * np.exp(1j * THETA)

def init():
	ax.set_xlim(aspect*-1.5, aspect*1.5)
	ax.set_ylim(-1.5, 1.5)
	ax.axis('off')
	
	return polys


speed = 1
def update(time):
	
	time *= speed / 90
	
	shift = n_points * np.array([
		np.pi * time,
		time
	]) 
	mZ = scipy.ndimage.shift(Z, shift, 
		prefilter=False, order=3, mode='wrap'
	)

	W = (1 + mZ) / (1 - mZ)
	
	_X, _Y = np.real(W), np.imag(W)
	_X[np.abs(_X) > 2*1.5*aspect] = np.NaN
	_Y[np.abs(_Y) > 2*1.5] = np.NaN

	for poly, sl in zip(polys, slices):		
		poly.set_xy(np.column_stack([
			np.concatenate([_X[s] for s in sl]),
			np.concatenate([_Y[s] for s in sl])
		]))

	return polys

def progress_call(frame, total_frames):
	print(f"Saving frame {1+frame} of {total_frames}...")

fps = 30
duration = 30 #seconds
frames = np.linspace(0, duration, fps*duration, endpoint=True)


ani = FuncAnimation(fig, update, init_func=init, frames=frames, blit=True)
ani.save('vid_test.mp4', writer='ffmpeg', fps=fps, dpi=DPI,
	progress_callback=progress_call)

