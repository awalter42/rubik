import vpython

class Cube:

	faceColor = {
		'green': vpython.color.green,
		'blue': vpython.color.blue,
		'white': vpython.color.white,
		'red': vpython.color.red,
		'yellow': vpython.color.yellow,
		'orange': vpython.color.orange,
		'grey': vpython.vector(0.2, 0.2, 0.2)}

	def __init__(self, U, B, F, R, D, L, position):
		sideR = vpython.box(pos=vpython.vector(0, 0, 0.5), length=1, height=1, width=0.1, color=self.faceColor[R])
		sideL = vpython.box(pos=vpython.vector(0, 0, -0.5), length=1, height=1, width=0.1, color=self.faceColor[L])
		sideF = vpython.box(pos=vpython.vector(-0.5, 0, 0), length=0.1, height=1, width=1, color=self.faceColor[F])
		sideB = vpython.box(pos=vpython.vector(0.5, 0, 0), length=0.1, height=1, width=1, color=self.faceColor[B])
		sideD = vpython.box(pos=vpython.vector(0, -0.5, 0), length=1, height=0.1, width=1, color=self.faceColor[D])
		sideU = vpython.box(pos=vpython.vector(0, 0.5, 0), length=1, height=0.1, width=1, color=self.faceColor[U])

		self.object = vpython.compound([sideR, sideL, sideF, sideB, sideD, sideU], origin=vpython.vector(0, 0, 0), pos=position)
