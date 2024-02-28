import unittest
import os

import RestClient as client


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = []
        quantity = 1000
        for x in range(quantity):
            p.append(client.RestClientGetRequest())
        # print(p)
        worldsPercentage = (p.count('"World"') * 100) / quantity
        errorsPercentage = (p.count('"Error"') * 100) / quantity
        print('success percentage: {}'.format(worldsPercentage))
        print('failure percentage: {}'.format(errorsPercentage))

        self.assertEqual(worldsPercentage > 88 or worldsPercentage < 92, True)
        self.assertEqual(errorsPercentage > 8 or errorsPercentage < 12, True)# add assertion here


if __name__ == '__main__':
    unittest.main()
