import unittest
import math
from scientific_calculator import sin, cos, tan, squareroot, log, exp

class TestScientificCalculator(unittest.TestCase):
    # for Sin Function
    def test_sin_positive(self):
        self.assertAlmostEqual(sin(math.pi/2), 1.0)

    def test_sin_negative(self):
        self.assertAlmostEqual(sin(-math.pi/2), -1.0)

    def test_sin_zero(self):
        self.assertAlmostEqual(sin(0), 0.0)

    def test_sin_non_numeric(self):
        with self.assertRaises(TypeError):
            sin("hello") 

    # for Cos Function
    def test_cos_positive(self):
        self.assertAlmostEqual(cos(math.pi/2), 0.0)

    def test_cos_negative(self):
        self.assertAlmostEqual(cos(-math.pi/2), 0.0)

    def test_cos_zero(self):
        self.assertAlmostEqual(cos(0), 1.0)

    def test_cos_non_numeric(self):
        with self.assertRaises(TypeError):
            cos("hello")

    # for Tan Function
    def test_tan_positive(self):
        self.assertAlmostEqual(tan(math.pi/4), 1.0)
        self.assertAlmostEqual(tan(math.pi/3), math.sqrt(3))

    def test_tan_negative(self):
        self.assertAlmostEqual(tan(-math.pi/4), -1.0)

    def test_tan_zero(self):
        self.assertAlmostEqual(tan(0), 0.0)

    def test_tan_non_numeric(self):
        with self.assertRaises(TypeError):
            tan("hello")

    # for Square Root Function
    def test_sqrt_positve(self):
        self.assertAlmostEqual(squareroot(9), 3.0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            squareroot(-9)

    def test_sqrt_zero(self):
        self.assertAlmostEqual(squareroot(0), 0.0)

    def test_sqrt_non_numeric(self):
        with self.assertRaises(TypeError):
            squareroot("hello")

    # for logarithm function
    def test_log_postive(self):
        self.assertAlmostEqual(log(10, 10), 1)
        self.assertAlmostEqual(log(16, 2), 4)
        self.assertAlmostEqual(log(1), 0)
        self.assertAlmostEqual(log(math.e), 1)
    
    def test_log_negative(self):
        with self.assertRaises(ValueError):
            log(-10)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            log(0)

    def test_log_non_numeric(self):
        with self.assertRaises(TypeError):
            log("hello")

    def test_log_custom_base(self):
        self.assertAlmostEqual(log(32, 2), 5)

    # for Exponential Function
    def test_exp_positive(self):
        self.assertAlmostEqual(exp(1), math.e)
        self.assertAlmostEqual(exp(0.5), math.e**0.5)
        self.assertAlmostEqual(exp(3), math.e**3)

    def test_exp_negative(self):
        self.assertAlmostEqual(exp(-5), 1/(math.e**5))
        self.assertAlmostEqual(exp(-0.5), 1/(math.e**0.5))

    def test_exp_zero(self):
        self.assertAlmostEqual(exp(0), 1)

    def test_exp_non_numeric(self):
        with self.assertRaises(TypeError):
            exp("hello")

if __name__ == '__main__':
    unittest.main()