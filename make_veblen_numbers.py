from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# We want only the best for our Veblen numbers, so use the golden ratio to set
# the image dimensions.
width = 1024
height = round(width / 1.61803398875)

# Generate each image using the DejaVuSans font and green on a black background
font = ImageFont.truetype("DejaVuSans.ttf", 400)
hacker_green = (10, 230, 20)
black = (0, 0, 0)

for n in range(0, 1000):
    # Initialize the image
    img = Image.new("RGB", (width, height), black)

    # Determine the offset, xy, needed to center the number
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(str(n), font=font)
    width_offset, height_offset = font.getoffset(str(n))
    text_width = text_width + width_offset
    text_height = text_height + height_offset
    top_left_x = width / 2 - text_width / 2
    top_left_y = height / 2 - text_height / 2
    xy = top_left_x, top_left_y

    # Add the number to the image, and save it to file
    draw.text(xy, str(n), font=font, fill=hacker_green)
    img.save('veblen_number_' + str(n) + '.png')

# Create a logo for the Veblen Numbers collection using the same procedure as
# before, but now with the text VN for Veblen Good and a smaller font size.
font = ImageFont.truetype("DejaVuSans.ttf", 200)
width = 350
height = 350
img = Image.new("RGB", (width, height), black)
draw = ImageDraw.Draw(img)
text_width, text_height = draw.textsize("VN", font=font)
width_offset, height_offset = font.getoffset("VN")
text_width = text_width + width_offset
text_height = text_height + height_offset
top_left_x = width / 2 - text_width / 2
top_left_y = height / 2 - text_height / 2
xy = top_left_x, top_left_y
draw.text(xy, "VN", font=font, fill=hacker_green)
img.save('vn_logo.png')

# Create a featured image for the Veblen Numbers collection with the text VN.
font = ImageFont.truetype("DejaVuSans.ttf", 200)
width = 600
height = 400
img = Image.new("RGB", (width, height), black)
draw = ImageDraw.Draw(img)
text_width, text_height = draw.textsize("VN", font=font)
width_offset, height_offset = font.getoffset("VN")
text_width = text_width + width_offset
text_height = text_height + height_offset
top_left_x = width / 2 - text_width / 2
top_left_y = height / 2 - text_height / 2
xy = top_left_x, top_left_y
draw.text(xy, "VN", font=font, fill=hacker_green)
img.save('vn_featured.png')

# Create a banner image for the Veblen Numbers collection with the text
# Veblen Numbers.
font = ImageFont.truetype("DejaVuSans.ttf", 150)
width = 1400
height = 400
img = Image.new("RGB", (width, height), black)
draw = ImageDraw.Draw(img)
text_width, text_height = draw.textsize("Veblen Numbers", font=font)
width_offset, height_offset = font.getoffset("Veblen Numbers")
text_width = text_width + width_offset
text_height = text_height + height_offset
top_left_x = width / 2 - text_width / 2
top_left_y = height / 2 - text_height / 2
xy = top_left_x, top_left_y
draw.text(xy, "Veblen Numbers", font=font, fill=hacker_green)
img.save('vn_banner.png')