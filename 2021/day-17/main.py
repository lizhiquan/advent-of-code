def initial_velocity_list(x_range, y_range):
    max_x_velocity = x_range[1]
    init_y_velocity = -y_range[0] - 1
    ans = []

    while init_y_velocity >= y_range[0]:
        for init_x_velocity in range(max_x_velocity + 1):
            x_velocity = init_x_velocity
            y_velocity = init_y_velocity
            x = 0
            y = 0

            while (x < x_range[0] or y > y_range[1]) and not (x_velocity == 0 and not (x_range[0] <= x <= x_range[1])):
                x += x_velocity
                x_velocity -= 1 if x_velocity > 0 else 0
                y += y_velocity
                y_velocity -= 1

            if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
                ans.append((init_x_velocity, init_y_velocity))

        init_y_velocity -= 1

    return ans


def part_one(x_range, y_range):
    y = initial_velocity_list(x_range, y_range)[0][1]
    return y * (y + 1) // 2


def part_two(x_range, y_range):
    return len(initial_velocity_list(x_range, y_range))


def main():
    x_range = (34, 67)
    y_range = (-215, -186)
    print('Part 1: ', part_one(x_range, y_range))
    print('Part 2: ', part_two(x_range, y_range))


if __name__ == '__main__':
    main()
