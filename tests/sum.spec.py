class Sum(object):
  def sum(self, a, b):
    a + b

import unittest

class TestSum(unittest.TestCase):
  def test_sum_1_2(self):
    s = Sum()
    self.assertEqual(s(1,2), 3)

if __name__ == '__main__':
  unittest.main()
