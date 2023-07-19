from PIL import Image
import csv

def create_image_from_csv(csv_file_path, output_image_path):
    with open(csv_file_path, 'r', newline='') as f:
        csv_reader = csv.reader(f)
        pixel_colors_array = [row for row in csv_reader]

    height = len(pixel_colors_array)
    width = len(pixel_colors_array[0])

    new_image = Image.new('RGB', (width, height), color='white')
    pixels = new_image.load()

    for y in range(height):
        for x in range(width):
            hex_color = pixel_colors_array[y][x]
            r = int(hex_color[1:3], 16)
            g = int(hex_color[3:5], 16)
            b = int(hex_color[5:7], 16)
            pixels[x, y] = (r, g, b)

    new_image.save(output_image_path)

csv_file_path = 'out.csv'
output_image_path = 'recreated_image.png'
create_image_from_csv(csv_file_path, output_image_path)
