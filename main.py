#!/usr/bin/env python3

from src import *


if __name__ == "__main__":
	mtrans = {
		'elliptic': Elliptic(-1, 1),
		'hyperbolic': Hyperbolic(-1, 1),
		'loxodromic': Loxodromic(-1, 1),
		'parabolic': Parabolic(0) 
	}
	
	mtrans['elliptic'].create_image("media/images/mtrans_1.png", resolution=(1920, 1080))
	mtrans['parabolic'].create_image("media/images/mtrans_2.png", resolution=(1920, 1080))
	
	mtrans['elliptic'].create_video("media/videos/elliptic.mp4", resolution=(1920, 1080))
	mtrans['hyperbolic'].create_video("media/videos/hyperbolic.mp4", resolution=(1920, 1080))
	mtrans['loxodromic'].create_video("media/videos/loxodromic.mp4", resolution=(1920, 1080))
	mtrans['parabolic'].create_video("media/videos/parabolic.mp4", resolution=(1920, 1080))
	