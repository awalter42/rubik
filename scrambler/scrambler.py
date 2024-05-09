import random
import argparse


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('length', type=int)
	args = parser.parse_args()

	if args.length <= 0:
		print('F U')
		exit(69)

	base = ['F', 'B', 'R', 'L', 'U', 'D']
	suff = [' ', '\' ', '2 ']
	ret = ''
	instructions = ''

	for i in range(args.length):
		r1 = random.randint(0, len(base) - 1)
		r2 = random.randint(0, 2)

		instructions += base[r1]
		instructions += suff[r2]
		temp = base.pop(r1)
		if ret != '':
			base.append(ret)
		ret = temp

	print(instructions)
