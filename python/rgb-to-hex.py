# RGB to Hex conversion
def rgb(r,g,b):
    def convert(decimal):
        if decimal > 255:
            decimal = 255
        elif decimal < 0:
            decimal = 0
        hexidecimal = hex(decimal)
        if len(hexidecimal[2:]) == 1:
            hexidecimal = '0'+hexidecimal[2:]
        else:
            hexidecimal = hexidecimal[2:]
        return hexidecimal.upper()
    
    red = convert(r)
    green = convert(g)
    blue = convert(b)
    rgb = red+green+blue
    print(rgb)


# rgb(0, 0, 0)
# rgb(1, 2, 3)
# rgb(255, 255, 255)
# rgb(254, 253, 252)
# rgb(-20, 275, 125)
