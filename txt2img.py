from PIL import Image

def create_image_from_pixel_colors(txt_file_path, output_image_path):
    with open(txt_file_path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    pixel_colors_array = []
    for line in lines:
        pixel_colors = line.strip().split(',')
        pixel_colors_array.append(pixel_colors)

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

txt_file_path = 'out.txt'
output_image_path = 'recreated_image.png'
create_image_from_pixel_colors(txt_file_path, output_image_path)
