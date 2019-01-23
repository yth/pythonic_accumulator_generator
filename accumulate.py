def accumulate(op, init, seq):
	if seq:
		return op(seq[0], accumulate(op, init, seq[1:]))
	else:
		return init

foldr = accumulate

def foldl(op, init, seq):
	for item in seq:
		init = op(init, item)
	return init

if __name__ == "__main__":

	# foldr and foldl should be equivalent to each other if:
	# op is commutative
	def add2(a, b): return a + b
	def sum_l(seq): return foldl(add2, 0, seq)
	def sum_r(seq): return foldr(add2, 0, seq)
	assert(sum_l(list(range(10))) == sum_r(list(range(10))))

	# init does not have to be the identity element of a function
	def extend(original_list, new_list):
		def cat(a, b):
			return [a] + b
		return accumulate(cat, init=new_list, seq=original_list)

	l1 = list(range(5)) # [0, 1, 2, 3, 4]
	l2 = list(range(5, 10, 1)) # [5, 6, 7, 8, 9]

	assert(extend(l1, l2) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
