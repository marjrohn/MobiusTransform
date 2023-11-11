from src import Loxodromic, Hyperbolic, Elliptic


if __name__ == "__main__":
	Loxodromic(-1, 1).create_image("media/images/mobius_trans.png", resolution=(1920, 1080))

	Loxodromic(-1, 1).create_video("media/videos/loxodromic.mp4", resolution=(1920, 1080))
	Hyperbolic(-1, 1).create_video("media/videos/hyperbolic.mp4", resolution=(1920, 1080))
	Elliptic(-1, 1).create_video("media/videos/elliptic.mp4", resolution=(1920, 1080))
