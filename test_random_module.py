'''
Testing generation of random numbers.
'''

import unittest
import random


class TestSequenceFunctions(unittest.TestCase):

    def set_up(self):
        '''
        Initializing game.
        '''
        self.seq = range(10)

    def test_shuffle(self):
        '''
        Testing shuffle.
        '''
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

    def choice(self):
        '''
        Testing choice.
        '''
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        '''
        Testing sample.
        '''
        self.assertRaises(ValueError, random.sample, self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

# Alternative, verbose test runner
# suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
# unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    unittest.main()
