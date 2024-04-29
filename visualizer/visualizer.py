import vpython
from cube import Cube
from rubik import Rubik
from time import sleep


def makeRubik():
	cube1 = Cube(R='red', F='green', D='grey', L='grey', B='grey', U='yellow', position=vpython.vector(-1.05, 1.05, 1.05))
	cube2 = Cube(R='red', F='grey', D='grey', L='grey', B='grey', U='yellow', position=vpython.vector(0, 1.05, 1.05))
	cube3 = Cube(R='red', F='grey', D='grey', L='grey', B='blue', U='yellow', position=vpython.vector(1.05, 1.05, 1.05))

	cube4 = Cube(R='red', F='green', D='grey', L='grey', B='grey', U='grey', position=vpython.vector(-1.05, 0, 1.05))
	cube5 = Cube(R='red', F='grey', D='grey', L='grey', B='grey', U='grey', position=vpython.vector(0, 0, 1.05))
	cube6 = Cube(R='red', F='grey', D='grey', L='grey', B='blue', U='grey', position=vpython.vector(1.05, 0, 1.05))

	cube7 = Cube(R='red', F='green', D='white', L='grey', B='grey', U='grey', position=vpython.vector(-1.05, -1.05, 1.05))
	cube8 = Cube(R='red', F='grey', D='white', L='grey', B='grey', U='grey', position=vpython.vector(0, -1.05, 1.05))
	cube9 = Cube(R='red', F='grey', D='white', L='grey', B='blue', U='grey', position=vpython.vector(1.05, -1.05, 1.05))


	cube10 = Cube(R='grey', F='green', D='grey', L='grey', B='grey', U='yellow', position=vpython.vector(-1.05, 1.05, 0))
	cube11 = Cube(R='grey', F='grey', D='grey', L='grey', B='grey', U='yellow', position=vpython.vector(0, 1.05, 0))
	cube12 = Cube(R='grey', F='grey', D='grey', L='grey', B='blue', U='yellow', position=vpython.vector(1.05, 1.05, 0))

	cube13 = Cube(R='grey', F='green', D='grey', L='grey', B='grey', U='grey', position=vpython.vector(-1.05, 0, 0))
	cube14 = Cube(R='grey', F='grey', D='grey', L='grey', B='blue', U='grey', position=vpython.vector(1.05, 0, 0))

	cube15 = Cube(R='grey', F='green', D='white', L='grey', B='grey', U='grey', position=vpython.vector(-1.05, -1.05, 0))
	cube16 = Cube(R='grey', F='grey', D='white', L='grey', B='grey', U='grey', position=vpython.vector(0, -1.05, 0))
	cube17 = Cube(R='grey', F='grey', D='white', L='grey', B='blue', U='grey', position=vpython.vector(1.05, -1.05, 0))


	cube18 = Cube(R='grey', F='green', D='grey', L='orange', B='grey', U='yellow', position=vpython.vector(-1.05, 1.05, -1.05))
	cube19 = Cube(R='grey', F='grey', D='grey', L='orange', B='grey', U='yellow', position=vpython.vector(0, 1.05, -1.05))
	cube20 = Cube(R='grey', F='grey', D='grey', L='orange', B='blue', U='yellow', position=vpython.vector(1.05, 1.05, -1.05))

	cube21 = Cube(R='grey', F='green', D='grey', L='orange', B='grey', U='grey', position=vpython.vector(-1.05, 0, -1.05))
	cube22 = Cube(R='grey', F='grey', D='grey', L='orange', B='grey', U='grey', position=vpython.vector(0, 0, -1.05))
	cube23 = Cube(R='grey', F='grey', D='grey', L='orange', B='blue', U='grey', position=vpython.vector(1.05, 0, -1.05))

	cube24 = Cube(R='grey', F='green', D='white', L='orange', B='grey', U='grey', position=vpython.vector(-1.05, -1.05, -1.05))
	cube25 = Cube(R='grey', F='grey', D='white', L='orange', B='grey', U='grey', position=vpython.vector(0, -1.05, -1.05))
	cube26 = Cube(R='grey', F='grey', D='white', L='orange', B='blue', U='grey', position=vpython.vector(1.05, -1.05, -1.05))

	rubik = Rubik([cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9, cube10, cube11, cube12, cube13, cube14, cube15, cube16, cube17, cube18, cube19, cube20, cube21, cube22, cube23, cube24, cube25, cube26])
	return (rubik)


if __name__ == '__main__':
	scene = vpython.canvas(width=2000, height=900, background=vpython.color.black)

	rubik = makeRubik()
	sleep(2)
	rubik.D(2)
	sleep(2)
	rubik.D_prime()
