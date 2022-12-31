class Solution:
	def digitCount(self, num: str) -> bool:
		c = Counter(num)
		for i, digit in enumerate(num):
			if c[str(i)] != int(digit):
				return False
		return True
