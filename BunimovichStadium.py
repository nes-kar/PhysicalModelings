class Particle:
	def __init__(self, pos, V, dt=0.01, a=5, r=3):
		self.x = pos[0]
		self.y = pos[1]
		self.Vx = V[0]
		self.Vy = V[1]
		self.a = a
		self.r = r
	def InBoundary(self, x, y):
		