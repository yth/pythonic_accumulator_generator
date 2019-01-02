from functools import partial

def accumulate(op, init, seq):
	if seq:
		return op(seq[0], accumulate(op, init, seq[1:]))
	else:
		return init

class accumulator(object):
	def __init__(self, bi_op, init, save_state=False):
		self.bi_op = bi_op
		self.init = init
		self.save_state = save_state

	def __call__(self, seq, init=None, func=None):
		if init: self.init = init

		if func: bi_op = partial(self.bi_op, f=func)
		else: bi_op = self.bi_op

		if self.save_state:
			self.init = accumulate(bi_op, self.init, seq)
			return self.init
		else:
			return accumulate(bi_op, self.init, seq)

if __name__ == "__main__":

	def add2(a, b): return a + b

	foo = accumulator
	f = foo(add2, 1, save_state=True)
	print(f([1]))
	print(f([1]))
	print(f([1, 1]))