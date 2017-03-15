from particle import Particle

class NeighbourTree:
	"""
	NeighbourTree

	A tree class that computes the FMM using only nearest neighbours
	for the near field calculations on each particle.
	"""
	def __init__(self, r, q):
		self.p = [Particle(rp, qp) for rp, qp in zip(r, q)]