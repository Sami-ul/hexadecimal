class Hexadecimal:
    def __init__(self, num) -> None:
        """
        conv_table is a dictionary that contains hexadecimal to deicmal
        conversions
        rev_conv_table is the same thing except it is used for the reverse
        conversion
        num_type is used to get the type given to the class so the
        hexadecimal_nval can be properly assigned
        hexadecimal_nval is the value that operations can be performed on
        while hexadecimal_sval is the string that is useful for outputs
        """
        self.conv_table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                           "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
                           "C": 12, "D": 13, "E": 14, "F": 15}  # hex:decimal
        self.rev_conv_table = {x: y for y, x in self.conv_table.items()}
        self.num_type = type(num)
        self.__clean_hex(num)
        self.hexadecimal_nval = num if self.num_type == str else self.conv_hex(
            num)
        self.hexadecimal_sval = "0x"+str(self.hexadecimal_nval)
        self.decimal_val = self.conv_decimal(self.hexadecimal_nval)

    def __clean_hex(self, val) -> None:
        """
        This method checks the datatype of the input value and checks if
        everything is valid
        """
        if isinstance(val, str):
            for i in val:
                if i not in self.conv_table.keys():
                    raise ValueError("hexadecimal value was invalid")
        elif isinstance(val, int):
            if val <= 0:
                raise ValueError("negative values are not supported")
        elif isinstance(val, float):
            raise ValueError(
                "'float' object is invalid, int or hexadecimal string only")
    """
    Numerical operations for hexadecimal values, will return hexadecimal 
    value if it can be expressed that way however if not it will return a 
    base 10 value, the cases of this returning a base 10 value include:
    - If the operation results in a floating point value
    - If the operation results in a negative value
    """
    def __add__(self, other) -> int or float:
        if isinstance(other, int) or isinstance(other, float):
            return Hexadecimal(self.conv_hex(self.decimal_val + other))
        return Hexadecimal(self.conv_hex(self.decimal_val + other.decimal_val))
    __radd__ = __add__

    def __sub__(self, other) -> int or float:
        if isinstance(other, int) or isinstance(other, float):
            decimal_result = self.decimal_val - other
            if decimal_result <= 0:
                return decimal_result
            elif decimal_result > 0:
                return self.conv_hex(decimal_result)
        decimal_result = self.decimal_val - other.decimal_val
        if decimal_result <= 0:
            return decimal_result
        elif decimal_result > 0:
            return Hexadecimal(self.conv_hex(decimal_result))

    def __rsub__(self, other) -> int or float:
        if isinstance(other, int) or isinstance(other, float):
            decimal_result = other - self.decimal_val
            if decimal_result <= 0:
                return decimal_result
            elif decimal_result > 0:
                return self.conv_hex(decimal_result)
        decimal_result = other.decimal_val - self.decimal_val
        if decimal_result <= 0:
            return decimal_result
        elif decimal_result > 0:
            return Hexadecimal(self.conv_hex(decimal_result))

    def __str__(self) -> str:
        return self.hexadecimal_sval

    def conv_hex(self, num_val) -> str:
        if isinstance(num_val, str):
            return num_val
        remainder_list = []
        result_list = []
        while num_val != 0:
            remainder_list.append(num_val % 16)
            num_val //= 16
        for i in remainder_list:
            result_list.append(self.rev_conv_table[i])
        return "".join(result_list)[::-1]
    def conv_decimal(self, hex_val) -> float:
        if isinstance(hex_val, float) or isinstance(hex_val, int):
            return hex_val
        hexadecimal_list = []
        for i in hex_val:
            hexadecimal_list.append(i)
        rev_list = hexadecimal_list[::-1]
        num_list = []
        calc_list = []
        power = 0
        for i in rev_list:
            num_list.append(self.conv_table[i])
        for i in num_list:
            calc_list.append(i*(16**power))
            power += 1
        return sum(calc_list)


# TODO add negative and float nums
