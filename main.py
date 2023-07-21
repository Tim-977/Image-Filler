from PIL import Image
import csv
import random
# from utils import *

# IMAGE MUST BE 500x500 in .png format

def hex_to_dec_array(hex_array):
    decimal_array = []
    for row in hex_array:
        decimal_row = []
        for element in row:
            decimal_value = int(element[1:], 16)
            decimal_row.append(decimal_value)
        decimal_array.append(decimal_row)
    return decimal_array


def sort_neighbors(arr):
    def find_median(arr):
        sorted_arr = sorted(arr)
        n = len(sorted_arr)

        if n % 2 == 1:
            median = sorted_arr[n // 2]
        else:
            middle_right = n // 2
            middle_left = middle_right - 1
            median = (sorted_arr[middle_left] + sorted_arr[middle_right]) / 2.0
        return median

    def get_neighbors(row, col, rows, cols):
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r = row + dr
                c = col + dc
                if 0 <= r < rows and 0 <= c < cols:
                    neighbors.append((r, c))
        return neighbors

    rows = len(arr)
    cols = len(arr[0])

    #pprint(arr)
    print('LEN ARR: ', sum(len(row) for row in arr)) # 250000

    pixel_neighbors = []

    for i in range(rows):
        for j in range(cols):
            pixel = arr[i][j]
            neighbors = get_neighbors(i, j, rows, cols)
            temp_arr = []
            temp_arr.append(pixel)
            temp_arr += [arr[r][c] for r, c in neighbors]
            pixel_neighbors.append(temp_arr)
    #pprint(pixel_neighbors)
    print('LEN NEW ARR: ', len(pixel_neighbors)) # 43796
    for i in range(len(pixel_neighbors)):
        #print('ELEM=1: ', pixel_neighbors[i])
        if len(pixel_neighbors[i]) < 9:
            temp_median = find_median(pixel_neighbors[i])
            pixel_neighbors[i] += [temp_median] * (9 - len(pixel_neighbors[i]))
        #print('ELEM=2: ', pixel_neighbors[i], len(pixel_neighbors[i]))
    return pixel_neighbors


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


image_path = 'pics\\image_2.png'
pixel_colors_array = get_pixel_colors(image_path)

decimal_array = hex_to_dec_array(pixel_colors_array)

print('LEN: ', sum(len(row) for row in decimal_array))

sorted_nbs_decimal_array = sort_neighbors(decimal_array)

sorted_nbs_decimal_array = [[float(element) for element in row] for row in sorted_nbs_decimal_array]

print('LEN_nbs: ', len(sorted_nbs_decimal_array))

# with open('nbs.txt', 'w', encoding='UTF-8') as f:
    # f.write(sorted_nbs_decimal_array)

# print(sorted_nbs_decimal_array[0])

with open('nbs.txt', 'w', encoding='UTF-8') as f:
    stop_sign = 0
    # [[7566706, 7500913, 7435635, 7369842, 7468274.0, 7468274.0, 7468274.0, 7468274.0, 7468274.0],
    # [7566706, 7500913, 7435635, 7369842, 7468274.0, 7468274.0, 7468274.0, 7468274.0, 7468274.0],
    # [7566706, 7500913, 7435635, 7369842, 7468274.0, 7468274.0, 7468274.0, 7468274.0, 7468274.0],
    # [7566706, 7500913, 7435635, 7369842, 7468274.0, 7468274.0, 7468274.0, 7468274.0, 7468274.0]]
    for i in range(len(sorted_nbs_decimal_array)):
        if stop_sign < 10 or True:
            f.write(f"Pixel: {sorted_nbs_decimal_array[i][0]}, Neighbors: {sorted_nbs_decimal_array[i][1:]} - {len(sorted_nbs_decimal_array[i][1:])} - {stop_sign}\n")
            stop_sign += 1
            #print(stop_sign)
        else:
            break
    print('DONE')

with open('out.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    for row in sorted_nbs_decimal_array:
        csv_writer.writerow(row)

# csv_file_path = 'out.csv'
# output_image_path = 'recreated_image.png'
# create_image_from_csv(csv_file_path, output_image_path)