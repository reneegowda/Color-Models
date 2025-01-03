"""
Functions for Color Converter

Renee Gowda (rsg276)
10/10/2024
"""
import introcs
import math

def complement_rgb(rgb):
    """
    Returns the complement of color rgb.

    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # Calculate the complement by subtracting each RGB component from 255
    new_red = 255 - rgb.red
    new_green = 255 - rgb.green
    new_blue = 255 - rgb.blue
    # Return the new RGB object with the complemented values
    return introcs.RGB(new_red, new_green, new_blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly
    5 characters.

    The decimal point counts as one of the five characters.

    Parameter value: the number to convert to a 5-character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Ensure value is a float for consistency
    value = float(value)
    # Convert the float value to a string
    value_str = str(value)
    # Split the string into the integer and decimal parts
    split = value_str.split('.')
    before_decimal = split[0]

    # Handle cases where there may not be a decimal part
    if len(split) > 1:
        after_decimal = split[1]
    else:
        after_decimal = ''  # Default to an empty string if no decimal part exists

    # Initialize rounded_value with a default value
    rounded_value = 0.0

    # Determine rounding precision based on the length of the integer part
    if len(before_decimal) == 3:
        rounded_value = round(value, 1)  # Round to one decimal place
    elif len(before_decimal) == 2:
        rounded_value = round(value, 2)  # Round to two decimal places
    elif len(before_decimal) == 1:
        rounded_value = round(value, 3)  # Round to three decimal places
    elif len(before_decimal) == 0:
        rounded_value = round(value, 4)  # Round to four decimal places

    # Convert the rounded value back to a string
    rounded_string = str(rounded_value)

    # Format the string to ensure it is exactly 5 characters long
    if len(rounded_string) < 5:
        if len(rounded_string) == 4:
            rounded_string += '0'
        elif len(rounded_string) == 3:
            rounded_string += '00'
        elif len(rounded_string) == 2:
            rounded_string += '000'
        elif len(rounded_string) == 1:
            rounded_string += '0000'
    elif len(rounded_string) > 5:
        rounded_string = rounded_string[:5]

    return rounded_string


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "<C, M, Y, K>".

    Each value is converted to a 5-character string.

    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is a CMYK object.
    """
    # Convert each CMYK component to a 5-character string using str5
    c_str = str5(cmyk.cyan)
    m_str = str5(cmyk.magenta)
    y_str = str5(cmyk.yellow)
    k_str = str5(cmyk.black)

    # Format the CMYK values into the required string representation
    return f"<{c_str}, {m_str}, {y_str}, {k_str}>"


def str5_hsl(hsl):
    """
    Returns the string representation of hsl in the form "<H, S, L>".

    Each value is converted to a 5-character string.

    Parameter hsl: the color to convert to a string
    Precondition: hsl is an HSL object.
    """
    # Convert each HSL component to a 5-character string using str5
    h_str = str5(hsl.hue)
    s_str = str5(hsl.saturation)
    l_str = str5(hsl.lightness)

    # Format the HSL values into the required string representation
    return f"<{h_str}, {s_str}, {l_str}>"


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.

    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # Normalize RGB values to the range 0..1
    new_red = rgb.red / 255.0
    new_green = rgb.green / 255.0
    new_blue = rgb.blue / 255.0
    # Calculate the black (K) component
    K = 1 - max(new_red, new_green, new_blue)

    # Handle special case when K = 1
    if K == 1:
        cyan = 0
        magenta = 0
        yellow = 0
    else:
        # Compute CMY components when K != 1
        cyan = (1 - new_red - K) / (1 - K)
        magenta = (1 - new_green - K) / (1 - K)
        yellow = (1 - new_blue - K) / (1 - K)

    # Scale the CMYK components to the range 0..100
    cyan *= 100
    magenta *= 100
    yellow *= 100
    black = K * 100

    # Return the CMYK object with the computed values
    return introcs.CMYK(cyan, magenta, yellow, black)


def cmyk_to_rgb(cmyk, rgb):
    """
    MODIFIES rgb to make it equivalent to cmyk.

    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html

    Parameter cmyk: the color to convert to an RGB object
    Precondition: cmyk is a CMYK object.

    Parameter rgb: the RGB object to store the results
    Precondition: rgb is an RGB object
    """
    # Normalize CMYK values to the range 0..1
    new_cyan = cmyk.cyan / 100.0
    new_magenta = cmyk.magenta / 100.0
    new_yellow = cmyk.yellow / 100.0
    new_K = cmyk.black / 100.0

    # Compute the RGB components using the conversion formulas
    red = (1 - new_cyan) * (1 - new_K)
    green = (1 - new_magenta) * (1 - new_K)
    blue = (1 - new_yellow) * (1 - new_K)

    # Modify the RGB object with the computed values (scaled to 0..255)
    rgb.red = int(round(red * 255))
    rgb.green = int(round(green * 255))
    rgb.blue = int(round(blue * 255))

def rgb_to_hsl(rgb):
    """
    Returns an HSL object equivalent to rgb

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter rgb: the color to convert to an HSL object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.

    # Dividing the RGB values by 255 to normalize them to the range [0, 1]
    new_red = rgb.red / 255.0
    new_green = rgb.green / 255.0
    new_blue = rgb.blue / 255.0

    # Finding the maximum and minimum values among the normalized RGB values
    max_rgb = max(new_red, new_green, new_blue)  # Maximum RGB value
    min_rgb = min(new_red, new_green, new_blue)  # Minimum RGB value

    # Initializing an HSL object with default values (hue=0, saturation=0, lightness=0)
    hsl = introcs.HSL(0, 0, 0)

    # Conditional logic to calculate the hue based on the maximum RGB value
    if max_rgb == min_rgb:  # Case: no color dominance, results in a neutral hue
        hsl.hue = 0
    elif max_rgb == new_red and new_green >= new_blue:
        # Case: red is the dominant color, with green >= blue
        hsl.hue = 60.0 * (new_green - new_blue) / (max_rgb - min_rgb)
    elif max_rgb == new_red and new_green <= new_blue:
        # Case: red is the dominant color, with green <= blue
        hsl.hue = 60.0 * (new_green - new_blue) / (max_rgb - min_rgb) + 360.0
    elif max_rgb == new_green:
        # Case: green is the dominant color
        hsl.hue = 60.0 * (new_blue - new_red) / (max_rgb - min_rgb) + 120.0
    elif max_rgb == new_blue:
        # Case: blue is the dominant color
        hsl.hue = 60.0 * (new_red - new_green) / (max_rgb - min_rgb) + 240.0

    # Calculating lightness as the average of the max and min RGB values
    hsl.lightness = (max_rgb + min_rgb) / 2

    # Conditional logic to calculate saturation based on lightness
    if hsl.lightness == 0 or hsl.lightness == 1:
        # Saturation is 0 if lightness is 0 (black) or 1 (white)
        hsl.saturation = 0
    else:
        # Formula for saturation when lightness is between 0 and 1
        hsl.saturation = (max_rgb - min_rgb) / (1 - abs(2 * hsl.lightness - 1))

    # Returning the HSL object (fruitful function)
    return hsl
