from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import numpy as np

# Read the base image and extract its width and height
base_img = Image.open("veblen_numbers_base_img.jpg")
base_img = base_img.convert("RGB") # Make sure we are in RGB "mode"
width, height = base_img.size

# Use the following font for the numbers
font = ImageFont.truetype("DejaVuSans.ttf", 1200)

# Use a different color for each Veblen number. Each of the five colors is
# assigned to 200 randomly chosen images.
hacker_green = (10, 230, 20)
gold = (255, 215, 0)
indian_red = (205, 92, 92)
royal_purple = (120, 81, 169)
deep_sky_blue = (0, 191, 255)

# The list of 1000 colors
color_list = [hacker_green for n in range(0, 200)] +\
             [gold for n in range(0, 200)] +\
             [indian_red for n in range(0, 200)] +\
             [royal_purple for n in range(0, 200)] +\
             [deep_sky_blue for n in range(0, 200)]
# Set a seed for reproducibility, then shuffle the color list.
random.seed(42)
random.shuffle(color_list)

for n in range(0, 1000):
    img = base_img.copy()
    img_color = color_list[n]

    # Determine the offset, xy, needed to center the number
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(str(n), font=font)
    width_offset, height_offset = font.getoffset(str(n))
    text_width = text_width + width_offset
    text_height = text_height + height_offset
    top_left_x = width / 2 - text_width / 2
    top_left_y = height / 2 - text_height / 2
    xy = top_left_x, top_left_y

    # Add the number to the image
    draw.text(xy, str(n), font=font, fill=img_color)

    # Replace the non-black pixels with the chosen color
    data = np.array(img)
    data[(data != [0, 0, 0]).all(axis=-1)] = img_color
    img = Image.fromarray(data, mode='RGB')

    img.save('veblen_number_' + str(n) + '.png')