import sys
from itertools import ifilter, tee


def read_numbers(filename):
	with open(filename) as input:
		while True:
			line = input.readline().strip()
			if not line:
				raise StopIteration()
			yield int(line)


def median(*numbers):
	"""
	>>> median(4, 2, 8)
	4
	>>> median(6, 8, 7)
	7
	"""
	return list(set(numbers) - {min(numbers), max(numbers)})[0]


def select_pivot(numbers):
	if len(numbers) == 2:
		return numbers[0]

	return median(numbers[0], numbers[-1], numbers[len(numbers) / 2])


def select_first(numbers):
	return numbers[0]


def select_last(numbers):
	return numbers[-1]


def split_by_pivot(numbers, pivot):
	"""
	>>> left, right = split_by_pivot([1, 5, 2, 4, 6], 3)
	>>> list(left), list(right)
	([1, 2], [6, 4, 5])
	"""
	left, right = tee(numbers)
	return (
		ifilter(lambda x: x < pivot, left),
		reversed(filter(lambda y: y > pivot, right)),
	)


def split(numbers, pivot):
	left, right = [], []
	for item in numbers:
		if item < pivot:
			left.append(item)
		else:
			right.insert(0, item)
	return left, right


def main(numbers):
	if len(list(numbers)) <= 1:
		return 0

	pivot = select_pivot(numbers)
	left, right = split(numbers, pivot)
	comparisons = len(list(left)) + len(list(right)) - 2
	left_comp, right_comp = main(left), main(right)
	return comparisons + left_comp + right_comp


if __name__ == '__main__':
	numbers = [n for n in read_numbers(sys.argv[1])]
	comparisons = main(numbers)
	print comparisons
