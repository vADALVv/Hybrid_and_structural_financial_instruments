import unittest
import numpy as np

from options import BasketOption

class TestOptionPricer(unittest.TestCase):
    '''
    The parameters and price for these unit tests are taken from 
    Krekel, de Kock, & Man (2004), published in Wilmott (pp 82-89).
    '''
    def test_levy(self):
        self.weights = np.ones(4)*0.25
        self.prices = np.ones(4)*100.
        self.vol = 0.4
        self.corr = np.array([[1.,0.5,0.5,0.5],
                              [0.5,1.,0.5,0.5],
                              [0.5,0.5,1.,0.5],
                              [0.5,0.5,0.5,1.]])
        self.strike = 100.
        self.time = 5
        self.rate = 0.
        opt = BasketOption(
                self.weights,
                self.prices, 
                self.vol, 
                self.corr, 
                self.strike, 
                self.time, 
                self.rate)

        levy_price = opt.get_levy_price()
        self.assertAlmostEqual(levy_price, 28.05, places=2)

    def test_ju_taylor(self):
        self.weights = np.ones(4) * 0.25
        self.prices = np.ones(4) * 100.
        self.vol = np.array([0.4, 0.4, 0.4, 0.4])  # Вектор волатильности
        self.corr = np.array([[1., 0.5, 0.5, 0.5],
                              [0.5, 1., 0.5, 0.5],
                              [0.5, 0.5, 1., 0.5],
                              [0.5, 0.5, 0.5, 1.]])
        self.strike = 100.
        self.time = 5
        self.rate = 0.
    
        opt = BasketOption(
            self.weights,
            self.prices,
            self.vol,
            self.corr,
            self.strike,
            self.time,
            self.rate
        )
    
        ju_price = opt.ju_taylor_approximation_call()
        expected_price = 28.05  # Укажите корректное значение
        self.assertAlmostEqual(ju_price, expected_price, places=2)


if __name__ == '__main__':
    unittest.main()
