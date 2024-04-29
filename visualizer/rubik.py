import vpython


class Rubik:

	def __init__(self, cubeList):
		self.cubeList = cubeList

	def R(self, n):
		lst = []
		for c in self.cubeList:
			if c.object.pos.z > 1:
				lst.append(c.object)

		for r in range (0, 50*n):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(0, 0, 1), angle=(-vpython.pi / 2)/50 , origin=vpython.vector(0,0,1.05))


	def R_prime(self):
		lst = []
		for c in self.cubeList:
			if c.object.pos.z > 1:
				lst.append(c.object)

		for r in range (0, 50):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(0, 0, 1), angle=(vpython.pi / 2)/50 , origin=vpython.vector(0,0,1.05))



	def L(self, n):
		lst = []
		for c in self.cubeList:
			if c.object.pos.z < -1:
				lst.append(c.object)

		for r in range (0, 50*n):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(0, 0, 1), angle=(vpython.pi / 2)/50 , origin=vpython.vector(0,0,-1.05))


	def L_prime(self):
		lst = []
		for c in self.cubeList:
			if c.object.pos.z < -1:
				lst.append(c.object)

		for r in range (0, 50):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(0, 0, 1), angle=(-vpython.pi / 2)/50 , origin=vpython.vector(0,0,-1.05))


	def F(self, n):
		lst = []
		for c in self.cubeList:
			if c.object.pos.x < -1:
				lst.append(c.object)

		for r in range (0, 50*n):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(1, 0, 0), angle=(vpython.pi / 2)/50 , origin=vpython.vector(-1.05,0,0))

	def F_prime(self):
		lst = []
		for c in self.cubeList:
			if c.object.pos.x < -1:
				lst.append(c.object)

		for r in range (0, 50):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(1, 0, 0), angle=(-vpython.pi / 2)/50 , origin=vpython.vector(-1.05,0,0))


	def B(self, n):
		lst = []
		for c in self.cubeList:
			if c.object.pos.x > 1:
				lst.append(c.object)

		for r in range (0, 50*n):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(1, 0, 0), angle=(-vpython.pi / 2)/50 , origin=vpython.vector(1.05,0,0))

	def B_prime(self):
		lst = []
		for c in self.cubeList:
			if c.object.pos.x > 1:
				lst.append(c.object)

		for r in range (0, 50):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(1, 0, 0), angle=(vpython.pi / 2)/50 , origin=vpython.vector(1.05,0,0))


	def U(self, n):
		lst = []
		for c in self.cubeList:
			if c.object.pos.y > 1:
				lst.append(c.object)

		for r in range (0, 50*n):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(0, 1, 0), angle=(-vpython.pi / 2)/50 , origin=vpython.vector(0,1.05,0))

	def U_prime(self):
		lst = []
		for c in self.cubeList:
			if c.object.pos.y > 1:
				lst.append(c.object)

		for r in range (0, 50):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(0, 1, 0), angle=(vpython.pi / 2)/50 , origin=vpython.vector(0,1.05,0))


	def D(self, n):
		lst = []
		for c in self.cubeList:
			if c.object.pos.y < -1:
				lst.append(c.object)

		for r in range (0, 50*n):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(0, 1, 0), angle=(vpython.pi / 2)/50 , origin=vpython.vector(0,-1.05,0))

	def D_prime(self):
		lst = []
		for c in self.cubeList:
			if c.object.pos.y < -1:
				lst.append(c.object)

		for r in range (0, 50):
			vpython.rate(60)
			for c in lst:
				c.rotate(axis=vpython.vector(0, 1, 0), angle=(-vpython.pi / 2)/50 , origin=vpython.vector(0,-1.05,0))


