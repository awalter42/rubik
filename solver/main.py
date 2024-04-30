import argparse

F = [1, 1, 1, 1, 1, 1, 1, 1, 1]

B = [6, 6, 6, 6, 6, 6, 6, 6, 6]

R = [2, 2, 2, 2, 2, 2, 2, 2, 2]

L = [5, 5, 5, 5, 5, 5, 5, 5, 5]

U = [3, 3, 3, 3, 3, 3, 3, 3, 3]

D = [4, 4, 4, 4, 4, 4, 4, 4, 4]



def F_move(n):
	global F, B, R, L, U, D

	for i in range (n):
		R[0], R[3], R[6], D[2], D[1], D[0], L[2], L[5], L[8], U[8], U[7], U[6] = U[6], U[7], U[8], R[0], R[3], R[6], D[0], D[1], D[2], L[2], L[5], L[8]
		F[0], F[1], F[2], F[3], F[5], F[6], F[7], F[8] = F[6], F[3], F[0], F[7], F[1], F[8], F[5], F[2]


def Fprime_move():
	global F, B, R, L, U, D

	U[6], U[7], U[8], R[6], R[3], R[0], D[0], D[1], D[2], L[8], L[5], L[2] = R[0], R[3], R[6], D[0], D[1], D[2], L[2], L[5], L[8], U[6], U[7], U[8]
	F[6], F[3], F[0], F[7], F[1], F[8], F[5], F[2] = F[0], F[1], F[2], F[3], F[5], F[6], F[7], F[8]


def B_move(n):
	global F, B, R, L, U, D

	for i in range(n):
		R[8], R[5], R[2], D[6], D[7], D[8], L[6], L[3], L[0], U[0], U[1], U[2] = D[6], D[7], D[8], L[0], L[3], L[6], U[0], U[1], U[2], R[2], R[5], R[8]
		B[0], B[1], B[2], B[3], B[5], B[6], B[7], B[8] = B[6], B[3], B[0], B[7], B[1], B[8], B[5], B[2]


def Bprime_move():
	global F, B, R, L, U, D

	D[8], D[7], D[6], L[0], L[3], L[6], U[2], U[1], U[0], R[2], R[5], R[8] = R[2], R[5], R[8], D[6], D[7], D[8], L[0], L[3], L[6], U[0], U[1], U[2]
	B[6], B[3], B[0], B[7], B[1], B[8], B[5], B[2] = B[0], B[1], B[2], B[3], B[5], B[6], B[7], B[8]


def R_move(n):
	global F, B, R, L, U, D

	for i in range(n):
		B[0], B[3], B[6], D[8], D[5], D[2], F[2], F[5], F[8], U[2], U[5], U[8] = U[8], U[5], U[2], B[0], B[3], B[6], D[2], D[5], D[8], F[2], F[5], F[8]
		R[0], R[1], R[2], R[3], R[5], R[6], R[7], R[8] = R[6], R[3], R[0], R[7], R[1], R[8], R[5], R[2]


def Rprime_move():
	global F, B, R, L, U, D

	U[8], U[5], U[2], B[6], B[3], B[0], D[2], D[5], D[8], F[8], F[5], F[2] = B[0], B[3], B[6], D[2], D[5], D[8], F[2], F[5], F[8], U[8], U[5], U[2]
	R[6], R[3], R[0], R[7], R[1], R[8], R[5], R[2] = R[0], R[1], R[2], R[3], R[5], R[6], R[7], R[8]


def L_move(n):
	global F, B, R, L, U, D

	for i in range(n):
		B[8], B[5], B[2], D[0], D[3], D[6], F[0], F[3], F[6], U[6], U[3], U[0] = D[0], D[3], D[6], F[0], F[3], F[6], U[0], U[3], U[6], B[2], B[5], B[8]
		L[0], L[1], L[2], L[3], L[5], L[6], L[7], L[8] = L[6], L[3], L[0], L[7], L[1], L[8], L[5], L[2]


def Lprime_move():
	global F, B, R, L, U, D

	D[0], D[3], D[6], F[0], F[3], F[6], U[0], U[3], U[6], B[2], B[5], B[8] = B[8], B[5], B[2], D[0], D[3], D[6], F[0], F[3], F[6], U[6], U[3], U[0]
	L[6], L[3], L[0], L[7], L[1], L[8], L[5], L[2] = L[0], L[1], L[2], L[3], L[5], L[6], L[7], L[8]


def U_move(n):
	global F, B, R, L, U, D

	for i in range(n):
		F[0], F[1], F[2], L[0], L[1], L[2], B[0], B[1], B[2], R[0], R[1], R[2] = R[0], R[1], R[2], F[0], F[1], F[2], L[0], L[1], L[2], B[0], B[1], B[2]
		U[0], U[1], U[2], U[3], U[5], U[6], U[7], U[8] = U[6], U[3], U[0], U[7], U[1], U[8], U[5], U[2]


def Uprime_move():
	global F, B, R, L, U, D

	R[0], R[1], R[2], F[0], F[1], F[2], L[0], L[1], L[2], B[0], B[1], B[2] = F[0], F[1], F[2], L[0], L[1], L[2], B[0], B[1], B[2], R[0], R[1], R[2]
	U[6], U[3], U[0], U[7], U[1], U[8], U[5], U[2] = U[0], U[1], U[2], U[3], U[5], U[6], U[7], U[8]


def D_move(n):
	global F, B, R, L, U, D

	for i in range(n):
		F[6], F[7], F[8], L[6], L[7], L[8], B[6], B[7], B[8], R[6], R[7], R[8] = L[6], L[7], L[8], B[6], B[7], B[8], R[6], R[7], R[8], F[6], F[7], F[8]
		D[0], D[1], D[2], D[3], D[5], D[6], D[7], D[8] = D[6], D[3], D[0], D[7], D[1], D[8], D[5], D[2]


def Dprime_move():
	global F, B, R, L, U, D

	L[6], L[7], L[8], B[6], B[7], B[8], R[6], R[7], R[8], F[6], F[7], F[8] = F[6], F[7], F[8], L[6], L[7], L[8], B[6], B[7], B[8], R[6], R[7], R[8]
	D[6], D[3], D[0], D[7], D[1], D[8], D[5], D[2] = D[0], D[1], D[2], D[3], D[5], D[6], D[7], D[8]






def scramble(moves):
	instructions = moves.split()


	for inst in instructions:
		match inst:
			case 'F':
				F_move(1)
			case 'F\'':
				Fprime_move()
			case 'F2':
				F_move(2)

			case 'B':
				B_move(1)
			case 'B\'':
				Bprime_move()
			case 'B2':
				B_move(2)

			case 'R':
				R_move(1)
			case 'R\'':
				Rprime_move()
			case 'R2':
				R_move(2)

			case 'L':
				L_move(1)
			case 'L\'':
				Lprime_move()
			case 'L2':
				L_move(2)

			case 'U':
				U_move(1)
			case 'U\'':
				Uprime_move()
			case 'U2':
				U_move(2)

			case 'D':
				D_move(1)
			case 'D\'':
				Dprime_move()
			case 'D2':
				D_move(2)

			case _:
				print(f"{inst} is not a good instruction: ignored\n")


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('moves', type=str)
	parser.add_argument("-v", "--visualisation", action="store_true", default=False, help='concatenates scrambler and solution for visualiser')
	args = parser.parse_args()

	scramble(args.moves)


	print(F, B, R, L, U, D, sep='\n\n')

