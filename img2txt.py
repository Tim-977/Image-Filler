from PIL import Image
import csv

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

with open('out.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    for row in pixel_colors_array:
        csv_writer.writerow(row)
