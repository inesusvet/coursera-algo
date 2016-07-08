import sys


def read_numbers(filename):
	with open(filename) as input:
		while True:
			line = input.readline().strip()
			if not line:
				raise StopIteration()
			yield int(line)


def split(numbers):
	"""
	>>> split([1, 2, 3, 4])
	([1, 2], [3, 4])
	>>> split([1, 2, 3, 4, 5])
	([1, 2], [3, 4, 5])
	"""
	middle = len(numbers) / 2
	return numbers[:middle], numbers[middle:]


def merge(left, right):
	"""
	>>> merge([1, 2, 3], [4, 5, 6])
	([1, 2, 3, 4, 5, 6], 0)
	>>> merge([1, 3, 5], [2, 4, 6])
	([1, 2, 3, 4, 5, 6], 3)
	>>> merge([1, 5], [2, 3, 4])
	([1, 2, 3, 4, 5], 3)
	>>> merge([1, 3, 5], [2, 4])
	([1, 2, 3, 4, 5], 3)
	>>> merge([], [3, 4])
	([3, 4], 0)
	>>> merge([1, 2], [])
	([1, 2], 0)
	"""
	result = []
	invertions = 0
	while (left or right):
		if left and right:
			if left[0] <= right[0]:
				item = left.pop(0)
			else:
				item = right.pop(0)
				invertions += len(left)

			result.append(item)

		elif left:
			result.extend(left)
			left = []
		else:
			result.extend(right)
			right = []

	return result, invertions



def main(numbers):
	if len(numbers) == 1:
		return numbers, 0

	left, right = split(numbers)
	left_result, left_inversions = main(left)
	right_result, right_invertions = main(right)

	result, invertions = merge(left_result, right_result)
	return result, left_inversions + right_invertions + invertions


if __name__ == '__main__':
	numbers = [n for n in read_numbers(sys.argv[1])]
	sorted_numbers, invertions = main(numbers)
	print invertions
