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


arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 100, 
       [11, 12, 13, 14, 15, 16, 17, 18, 19, 20] * 100, 
       [21, 22, 23, 24, 25, 26, 27, 28, 29, 30] * 100, 
       [31, 32, 33, 34, 35, 36, 37, 38, 39, 40] * 100, 
       [41, 42, 43, 44, 45, 46, 47, 48, 49, 50] * 100,
       [51, 52, 53, 54, 55, 56, 57, 58, 59, 60] * 100, 
       [61, 62, 63, 64, 65, 66, 67, 68, 69, 70] * 100, 
       [71, 72, 73, 74, 75, 76, 77, 78, 79, 80] * 100, 
       [81, 82, 83, 84, 85, 86, 87, 88, 89, 90] * 100, 
       [91, 92, 93, 94, 95, 96, 97, 98, 99, 100] * 100] * 100

# arr = [[1, 2, 3, 4, 5], 
#        [6, 7, 8, 9, 10], 
#        [11, 12, 13, 14, 15], 
#        [16, 17, 18, 19, 20], 
#        [21, 22, 23, 24, 25]]

# arr = [[1, 2, 3], 
#        [4, 5, 6], 
#        [7, 8, 9]]

arr_2 = sort_neighbors(arr)
#print(arr_2)
print(sum(len(rows) for rows in arr))
print(len(arr_2))
