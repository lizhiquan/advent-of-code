def read_input(filename):
    with open(filename, 'r') as file:
        algo = file.readline().rstrip()
        file.readline()
        image = []
        for line in file:
            image.append(line.rstrip())
        return algo, image


def get_pixel(image, i, j, default):
    if i < 0 or j < 0 or i > len(image) - 1 or j > len(image[0]) - 1:
        return default
    return image[i][j]


def enhance_image(image, algo, default_pixel):
    new_image = [[None] * (len(image[0]) + 2) for _ in range(len(image) + 2)]
    for i in range(len(new_image)):
        for j in range(len(new_image[i])):
            bin_code = ''
            for n in range(i - 2, i + 1):
                for m in range(j - 2, j + 1):
                    bin_code += '0' if get_pixel(image, n, m, default_pixel) == '.' else '1'
            new_image[i][j] = algo[int(bin_code, 2)]

    return new_image


def lit_pixels_after_enhancement(image, algo, times):
    default_pixel = '.'
    for _ in range(times):
        image = enhance_image(image, algo, default_pixel)
        default_pixel = algo[0] if default_pixel == '.' else algo[-1]
    return sum(sum(p == '#' for p in row) for row in image)


def part_one(algo, image):
    return lit_pixels_after_enhancement(image, algo, 2)


def part_two(algo, image):
    return lit_pixels_after_enhancement(image, algo, 50)


def main():
    algo, image = read_input('input.txt')
    print('Part 1: ', part_one(algo, image))
    print('Part 2: ', part_two(algo, image))


if __name__ == '__main__':
    main()
