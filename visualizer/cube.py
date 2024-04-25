import vpython
# from numpy import vector


class Cube:

	def __init__(self):
		self.side1 = vpython.box(pos=vpython.vector(-1, 0, 0), length=0, height=1, width=1, color=vpython.color.red)

