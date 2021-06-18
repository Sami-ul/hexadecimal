from hexadecimal import Hexadecimal
x = Hexadecimal("A1B") # 2587 in base 10
y = Hexadecimal("74")
print((x+y).hexadecimal_sval) # prints the string value(more stylistically better than nval)
print((x+y).decimal_val) # prints the decimal value
