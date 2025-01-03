# Color-Models
This repository contains Python functions that implement color conversions between RGB, HSL, and CMYK color models. These functions rely on well-established formulas derived from color theory, providing an easy and reliable way to work with different color spaces in projects involving color manipulation, graphic design, data visualization, UI development, or any other domain that requires accurate color transformations.

Features
RGB to HSL Conversion
Converts RGB (Red, Green, Blue) values into the HSL (Hue, Saturation, Lightness) color model, allowing for more intuitive adjustments to color properties like saturation and brightness.

HSL to RGB Conversion
Converts HSL values back into RGB values, enabling seamless transitions between the two color models for various applications such as web development and graphic design.

RGB to CMYK Conversion
Converts RGB colors to CMYK (Cyan, Magenta, Yellow, Black) format, which is commonly used in printing applications where color mixing is more complex than with light-based RGB models.

CMYK to RGB Conversion
Converts CMYK values back into RGB format, allowing designers to work in print-based color spaces and still use web and digital color models.

Color Models:
RGB (Red, Green, Blue)
RGB is a color model used primarily for digital displays. Colors are created by combining varying intensities of red, green, and blue light. Each of the three components can range from 0 to 255, allowing for over 16 million color combinations.

HSL (Hue, Saturation, Lightness)
The HSL color model represents colors more intuitively by separating hue (the type of color), saturation (the intensity of the color), and lightness (the brightness or darkness of the color). This model is often used in graphic design and image processing because it allows users to adjust colors more easily by modifying these three attributes.

CMYK (Cyan, Magenta, Yellow, Black)
CMYK is a color model used in color printing, where colors are created by subtracting varying amounts of light from the four primary ink colors. The model works on the principle of "subtractive" color mixing, unlike RGB, which uses additive mixing (light-based). The CMYK model is especially useful for printing because it accounts for how inks combine on paper.
