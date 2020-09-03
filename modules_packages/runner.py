from modules.calculator import * #way to import from a package
print(add(10, 20))
print(multiply(3,4))
print(subtract(7,4))
print(divide(8,2))

import modules.calculator as calc # another way to import from packages

print(calc.add(10, 20))
print(calc.multiply(3,4))
print(calc.subtract(7,4))
print(calc.divide(8,2))