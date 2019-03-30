import unittest

from lecture import FirstObject


class UnitTesting(unittest.TestCase):
	
	def test_shipping_cost(self):
		small_weights = [15.0, 10.0, 20.0, 25.0, 10.0]
		large_weights = [45.0, 30.1, 30.0, 55.0]
		
		def compute_shipping_cost(weight):
			if weight < 30:
				return 5.0
			else:
				return 5.0 + (weight - 30.0) * 0.25
		
		for small_weight in small_weights:
			self.assertTrue(FirstObject.computeShippingCost(
				small_weight) == compute_shipping_cost(
				small_weight), small_weight)
		
		for large_weight in large_weights:
			self.assertTrue(FirstObject.computeShippingCost(
				large_weight) == compute_shipping_cost(
				large_weight), large_weight)


if __name__ == '__main__':
	unittest.main()
