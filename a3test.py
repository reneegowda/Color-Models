"""
Unit Tests for Color Converter

This module implements several test cases for the Color Converter application.

Renee Gowda (rsg276)
10/10/2024
"""

import introcs
import a3

def test_complement():
    """
    Test function complement
    """
    print('Testing complement')

    # One test is really good enough here
    rgb = introcs.RGB(250, 0, 71)
    comp = a3.complement_rgb(rgb)
    introcs.assert_equals(255-250, comp.red)
    introcs.assert_equals(255-0,   comp.green)
    introcs.assert_equals(255-71,  comp.blue)

    # Check we did not modify the original color
    introcs.assert_equals(250, rgb.red)
    introcs.assert_equals(0,   rgb.green)
    introcs.assert_equals(71,  rgb.blue)

    # One more for good measure
    comp = a3.complement_rgb(introcs.RGB(128, 64, 255))
    introcs.assert_equals(255-128, comp.red)
    introcs.assert_equals(255-64,  comp.green)
    introcs.assert_equals(255-255, comp.blue)


def test_str5():
    """
    Test function str5
    """
    introcs.assert_equals('130.6',  a3.str5(130.59))
    introcs.assert_equals('130.5',  a3.str5(130.54))
    introcs.assert_equals('100.0',  a3.str5(100))
    introcs.assert_equals('100.6',  a3.str5(100.56))
    introcs.assert_equals('99.57',  a3.str5(99.566))
    introcs.assert_equals('99.99',  a3.str5(99.99))
    introcs.assert_equals('100.0',  a3.str5(99.995))
    introcs.assert_equals('22.00',  a3.str5(21.99575))
    introcs.assert_equals('21.99',  a3.str5(21.994))
    introcs.assert_equals('10.01',  a3.str5(10.013567))
    introcs.assert_equals('10.00',  a3.str5(10.000000005))
    introcs.assert_equals('10.00',  a3.str5(9.9999))
    introcs.assert_equals('9.999',  a3.str5(9.9993))
    introcs.assert_equals('1.355',  a3.str5(1.3546))
    introcs.assert_equals('1.354',  a3.str5(1.3544))
    introcs.assert_equals('0.046',  a3.str5(.0456))
    introcs.assert_equals('0.045',  a3.str5(.0453))
    introcs.assert_equals('0.006',  a3.str5(.0056))
    introcs.assert_equals('0.001',  a3.str5(.0013))
    introcs.assert_equals('0.000',  a3.str5(.0004))
    introcs.assert_equals('0.001',  a3.str5(.0009999))
    introcs.assert_equals('0.000',  a3.str5(1e-9))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsl.
    """
    print('Testing str5_cmyk and str5_hsl')

    # Tests for str5_cmyk
    # We need to make sure the coordinates round properly
    text = a3.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0))
    introcs.assert_equals('<98.45, 25.36, 72.80, 1.000>',text)

    text = a3.str5_cmyk(introcs.CMYK(0.0, 1.5273, 100.0, 57.846))
    introcs.assert_equals('<0.000, 1.527, 100.0, 57.85>',text)

    # Tests for str5_hsl (add two)
    more_text = a3.str5_hsl(introcs.HSL(45.678, 0.321, 0.5))
    introcs.assert_equals('<45.68, 0.321, 0.500>',more_text)

    more_text = a3.str5_hsl(introcs.HSL(78.9, 0.72, 0.003 ))
    introcs.assert_equals('<78.90, 0.720, 0.003>',more_text)

    more_text = a3.str5_hsl(introcs.HSL(100, 0, 1.0))
    introcs.assert_equals('<100.0, 0.000, 1.000>',more_text)

    more_text = a3.str5_hsl(introcs.HSL(123.456, 0.7839, 0.12345))
    introcs.assert_equals('<123.5, 0.784, 0.123>', more_text)

    more_text = a3.str5_hsl(introcs.HSL(3.4567, 0.1, 0.01))
    introcs.assert_equals('<3.457, 0.100, 0.010>', more_text)


def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    print('Testing rgb_to_cmyk')

    # The function should guarantee accuracy to three decimal places
    rgb = introcs.RGB(255, 255, 255)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(0.0, round(cmyk.black,3))

    rgb = introcs.RGB(0, 0, 0)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(100.0, round(cmyk.black,3))

    rgb = introcs.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(80.184, round(cmyk.magenta,3))
    introcs.assert_equals(24.424, round(cmyk.yellow,3))
    introcs.assert_equals(14.902, round(cmyk.black,3))


def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    print('Testing cmyk_to_rgb')

    # Create an RGB to store the answer
    # Should start off DIFFERENT from expected answer
    rgb  = introcs.RGB(255,255,255)
    cmyk = introcs.CMYK(100, 100, 100, 100)
    a3.cmyk_to_rgb(cmyk,rgb)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    #all values starting at 0
    rgb  = introcs.RGB(0,0,0)
    cmyk = introcs.CMYK(0, 0, 0, 0)
    a3.cmyk_to_rgb(cmyk,rgb)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    #edge case where k=1 (max black)
    rgb  = introcs.RGB(255,255,255)
    cmyk = introcs.CMYK(0, 0, 0, 100)
    a3.cmyk_to_rgb(cmyk,rgb)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    #edge case where k=0 (no black)
    rgb  = introcs.RGB(0,0,0)
    cmyk = introcs.CMYK(50, 50, 50, 0)
    a3.cmyk_to_rgb(cmyk,rgb)
    introcs.assert_equals(128, rgb.red)
    introcs.assert_equals(128, rgb.green)
    introcs.assert_equals(128, rgb.blue)

    #using the color converter and testing random cmyk values
    #rgb starts at 0,0,0
    rgb  = introcs.RGB(0,0,0)
    cmyk = introcs.CMYK(20, 40, 60, 30)
    a3.cmyk_to_rgb(cmyk,rgb)
    introcs.assert_equals(143, rgb.red)
    introcs.assert_equals(107, rgb.green)
    introcs.assert_equals(71, rgb.blue)

    #using the color converter and testing more random cmyk values
    #rgb starts at something random
    rgb  = introcs.RGB(78,26,52)
    cmyk = introcs.CMYK(63, 29, 94, 8)
    a3.cmyk_to_rgb(cmyk,rgb)
    introcs.assert_equals(87, rgb.red)
    introcs.assert_equals(167, rgb.green)
    introcs.assert_equals(14, rgb.blue)

    #testing random decimal cmyk values
    rgb  = introcs.RGB(0,0,0)
    cmyk = introcs.CMYK(12.345, 48.03, 9.1, 11.78)
    a3.cmyk_to_rgb(cmyk,rgb)
    introcs.assert_equals(197, rgb.red)
    introcs.assert_equals(117, rgb.green)
    introcs.assert_equals(204, rgb.blue)

    #testing random decimal and number cmyk values
    rgb  = introcs.RGB(23,0,0)
    cmyk = introcs.CMYK(56.78, 6.9, 90.0, 17)
    a3.cmyk_to_rgb(cmyk,rgb)
    introcs.assert_equals(91, rgb.red)
    introcs.assert_equals(197, rgb.green)
    introcs.assert_equals(21, rgb.blue)

    #intermediate values of k
    rgb  = introcs.RGB(0,0,0)
    cmyk = introcs.CMYK(0, 0, 0, 50)
    a3.cmyk_to_rgb(cmyk,rgb)
    introcs.assert_equals(128, rgb.red)
    introcs.assert_equals(128, rgb.green)
    introcs.assert_equals(128, rgb.blue)

    #color mixing case
    rgb  = introcs.RGB(22,37,86)
    cmyk = introcs.CMYK(100, 0, 24, 50)
    a3.cmyk_to_rgb(cmyk,rgb)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(128, rgb.green)
    introcs.assert_equals(97, rgb.blue)


def test_rgb_to_hsl():
    """
    Test translation function rgb_to_hsl
    """
    print('Testing rgb_to_hsl')

    #testing equal rgb values
    rgb = introcs.RGB(128, 128, 128)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(0.0, round(hsl.saturation,3))
    introcs.assert_equals(0.502, round(hsl.lightness,3))

    #testing max_rgb == new_red and new_green >= new_blue
    rgb = introcs.RGB(255, 100, 100)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.696, round(hsl.lightness,3))

    #testing max_rgb == new_red and new_green <= new_blue
    rgb = introcs.RGB(255, 0, 8)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_equals(358.118, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))

    #testing max_rgb == new_green
    rgb = introcs.RGB(100, 255, 100)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_equals(120.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.696, round(hsl.lightness,3))

    #testing max_rgb == new_blue
    rgb = introcs.RGB(100, 100, 255)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_equals(240.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.696, round(hsl.lightness,3))

    #testing lightness == 0 (black)
    rgb = introcs.RGB(0, 0, 0)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(0.0, round(hsl.saturation,3))
    introcs.assert_equals(0.0, round(hsl.lightness,3))

    #testing lightness == 1 (white)
    rgb = introcs.RGB(255, 255, 255)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(0.0, round(hsl.saturation,3))
    introcs.assert_equals(1.0, round(hsl.lightness,3))

    #testing random rgb values
    rgb = introcs.RGB(247, 84, 106)
    hsl = a3.rgb_to_hsl(rgb)
    introcs.assert_equals(351.902, round(hsl.hue,3))
    introcs.assert_equals(0.911, round(hsl.saturation,3))
    introcs.assert_equals(0.649, round(hsl.lightness,3))


def test_hsl_to_rgb():
    """
    Test translation function hsl_to_rgb
    """
    print('Testing hsl_to_rgb')

    #testing new_hue == 0 or new_hue == 5 for red = p
    hsl = introcs.HSL(0.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    #testing new_hue == 1 for red = v
    hsl = introcs.HSL(60.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    #testing new_hue == 2 or new_hue == 3 for red = q
    hsl = introcs.HSL(120.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    #testing new_hue == 4 for red = u
    hsl = introcs.HSL(240.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    #testing new_hue == 0 for green = u
    hsl = introcs.HSL(0.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    #testing new_hue == 1 or new_hue == 2 for green = p
    hsl = introcs.HSL(120.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    #testing new_hue == 3 for green = v
    hsl = introcs.HSL(180.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    #testing new_hue == 4 or new_hue == 5 for green = q
    hsl = introcs.HSL(240.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    #testing new_hue == 0 or new_hue == 1 for blue = q
    hsl = introcs.HSL(0.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    #testing new_hue == 2 for blue = u
    hsl = introcs.HSL(120.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    #testing new_hue == 3 or new_hue == 4 for blue = p
    hsl = introcs.HSL(180.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    #testing new_hue == 5 for blue = v
    hsl = introcs.HSL(300.0, 1.0, 0.5)
    rgb = introcs.RGB(0, 0, 0)
    a3.hsl_to_rgb(hsl,rgb)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(255, rgb.blue)


# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == '__main__':
    test_complement()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsl()
    test_hsl_to_rgb()
    print('Module a3 passed all tests.')
