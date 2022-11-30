i = 1
while i < 18:
    oct_i = format(i, 'o')
    hex_i = format(i, 'X')
    bin_i = format(i, 'b')
    print(f"{i}  {oct_i}  {hex_i}  {bin_i}")
    i += 1



#In this version I wrote Decimal to Octal's formula without "format"
"""
i = 1
while i<18:
    oct = i
    i_oct = ""
    while oct != 0:
        if oct>=8:
            oct_r = oct//8
            octal_full = oct_r*10
            oct_r = oct - 8*oct_r
            octal_full += oct_r
        else:
            octal_full = oct
        oct=0
    hex_i = format(i, 'X')
    bin_i = format(i, 'b')
    print(f"{i}  {octal_full}  {hex_i}  {bin_i}")
    i += 1
"""    