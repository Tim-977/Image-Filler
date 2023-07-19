from PIL import Image

# IMAGE MUST BE 500x500 in .png format

def get_pixel_colors(image_path):
    image = Image.open(image_path)
    width, height = image.size

    pixel_colors = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = image.getpixel((x, y))
            hex_color = "#{:02x}{:02x}{:02x}".format(*pixel[:3])
            row.append(hex_color)
        pixel_colors.append(row)

    return pixel_colors

image_path = 'image_1.png'
pixel_colors_array = get_pixel_colors(image_path)

temp = ''

with open('out.txt', 'w', encoding='UTF-8') as f:
    for elem in pixel_colors_array:
        f.write(','.join(elem) + '\n')
