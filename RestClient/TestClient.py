import unittest
import os

import RestClient as client


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = []
        quantity = int(os.getenv("TEST_QUANTITY"))
        for x in range(quantity):
            p.append(client.RestClientGetRequest())
        worldsPercentage = (p.count('"World"') * 100) / quantity
        errorsPercentage = (p.count('"Error"') * 100) / quantity
        print('success percentage: {}'.format(worldsPercentage))
        print('failure percentage: {}'.format(errorsPercentage))

        self.assertEqual(worldsPercentage > 88 or worldsPercentage < 92, True,'success percentage: {}'.format(worldsPercentage) + " is not within range (88,92)")
        self.assertEqual(errorsPercentage > 8 or errorsPercentage < 12, True, 'failure percentage: {}'.format(errorsPercentage)+ " is not within range (8,12)")


if __name__ == '__main__':
    unittest.main()
