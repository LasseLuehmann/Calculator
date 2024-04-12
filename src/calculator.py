import operator
from .custom_ex import IncorrectInputError, NoArgumentsGivenError

class Calculator:
    def add(self, *args: float) -> float:
        return sum(args)

    def multiply(self, *args: float) -> float:
        try:
            result: float = 1 
            if len(args) <= 1:
                raise NoArgumentsGivenError('Operation not possible without values')
            for i in args:
                result *= i
            return result
        except TypeError:
            raise IncorrectInputError('Wrong input')

    def sub(self, *args):
        try:
            if len(args) == 0:
                return 0
            first = args[0]
            for i in range(1,len(args)):
                first -= args[i]
            return first
        except TypeError:
            raise IncorrectInputError('Unsoported data types')
    
    def div(self, divisor, divident):
        result = divisor / divident
        return result
    
    def mod(self, divisor, divident):
        result = divisor % divident
        return result

# cal = Calculator()

# print(cal.multiply())

