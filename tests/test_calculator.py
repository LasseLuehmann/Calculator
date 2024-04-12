import unittest
from typing import NoReturn
from src.calculator import Calculator
from src.custom_ex import IncorrectInputError

class CalculatorAddTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
    
    def test_add_3_numbers(self) -> None | NoReturn:
        # Arrange
        x = 4
        y = 3
        z = 1
        expected_result = 8

        # Act
        result = self.calculator.add(x,y,z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_add_with_no_args(self) -> None | NoReturn:
        # Arange
        expected_result = 0
        # Act
        result = self.calculator.add()
        # Assert
        self.assertEqual(result, expected_result)

    def test_add_with_incorrect_argument(self) -> None | NoReturn:
        # Arange

        x = '6'
        z = [4,5]

        # Act/Assert
        with self.assertRaises(TypeError):
            self.calculator.add(x,z)

    def tearDown(self):
        pass

class CalculatorMultTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_mult_with_correct_input(self):
        # Arrange
        x = 1
        y = 2
        z = 3
        expected_result = 6

        # Act
        result = self.calculator.multiply(x,y,z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_mult_with_no_input(self):
        
        with self.assertRaises(ValueError):
            self.calculator.multiply()

    def test_mult_with_incorrect_input(self):

        # Arange

        x = []
        y = (1,2)
        z = '5'

        # Act/Assert
        with self.assertRaises(IncorrectInputError):
            self.calculator.multiply(x,y,z)

    def tearDown(self):
        pass

class CalculatorSubTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sub_with_correct_input(self):
        # Arange
        x = 4
        y = 6
        z = 20
        expected_result = -22

        # Act
        result = self.calculator.sub(x,y,z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_sub_with_no_input(self):
        # Arange
        expected_result = 0
        # Act
        result = self.calculator.sub()
        # Assert
        self.assertEqual(result, expected_result)
    
    def test_sub_with_incorrect_input(self):
        # Arange

        x = '6'
        z = [4,5]

        # Act/Assert
        with self.assertRaises(TypeError):
            self.calculator.sub(x,z)

class CalculatorDivTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_div_with_corect_input(self):
        x = 20
        y = 5

        expected_result = 4

        result = self.calculator.div(x,y)

        self.assertEqual(result, expected_result)

    def test_div_with_no_input(self):

        with self.assertRaises(TypeError):
            self.calculator.div()

class CalculatorModTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_mod_with_corect_input(self):
        x = 19
        y = 5

        expected_result = 4

        result = self.calculator.mod(x,y)

        self.assertEqual(result, expected_result)

