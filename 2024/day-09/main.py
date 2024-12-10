def part_one(disk_map):
    tmp_map = disk_map.copy()
    i, j = 0, len(tmp_map) - 1
    checksum = 0
    pos = 0
    while i <= j:
        if i & 1:  # i is space
            file_id = j // 2
            spaces = tmp_map[i]
            if spaces < tmp_map[j]:
                for _ in range(spaces):
                    checksum += pos * file_id
                    pos += 1
                i += 1
                tmp_map[j] -= spaces
            else:
                for _ in range(tmp_map[j]):
                    checksum += pos * file_id
                    pos += 1
                tmp_map[i] -= tmp_map[j]
                j -= 2
        else:  # i is file
            file_id = i // 2
            for _ in range(tmp_map[i]):
                checksum += pos * file_id
                pos += 1
            i += 1
    return checksum


def part_two(disk_map):
    files = [[] for _ in range(10)]  # files[size] = [id, ...]
    id = 0
    for i, size in enumerate(disk_map):
        if i & 1 == 0:  # is file
            files[size].append(id)
            id += 1

    used = [False] * id  # file id is used in checksum
    id = pos = checksum = i = 0
    while i < len(disk_map):
        # process file
        size = disk_map[i]
        if not used[id]:
            for _ in range(size):
                checksum += pos * id
                pos += 1
            used[id] = True
        else:
            pos += size
        id += 1
        i += 1

        # process space
        if i < len(disk_map):
            spaces = disk_map[i]
            while size := max(
                (sz for sz in range(1, spaces + 1) if len(files[sz]) > 0),
                key=lambda x: files[x][-1],
                default=None,
            ):
                nid = files[size].pop()
                if not used[nid]:
                    for _ in range(size):
                        checksum += pos * nid
                        pos += 1
                    spaces -= size
                    used[nid] = True
            pos += spaces
            i += 1

    return checksum


def read_input(filename: str):
    with open(filename, "r") as f:
        return [int(c) for c in f.read()]


inp = read_input("input.txt")
print(f"Part 1: {part_one(inp)}")
print(f"Part 2: {part_two(inp)}")
