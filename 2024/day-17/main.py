from collections import deque


def part_one(reg_a, reg_b, reg_c, program):
    output = []
    instruction_ptr = 0
    while instruction_ptr < len(program):
        opcode, operand = program[instruction_ptr], program[instruction_ptr + 1]
        combo_operand = {
            operand: operand,
            4: reg_a,
            5: reg_b,
            6: reg_c,
        }[operand]

        if opcode == 0:  # adv instruction
            reg_a //= 2**combo_operand
        elif opcode == 1:  # bxl instruction
            reg_b ^= operand
        elif opcode == 2:  # bst instruction
            reg_b = combo_operand % 8
        elif opcode == 3:  # jnz instruction
            if reg_a != 0:
                instruction_ptr = operand
                continue
        elif opcode == 4:  # bxc instruction
            reg_b ^= reg_c
        elif opcode == 5:  # out instruction
            output.append(combo_operand % 8)
        elif opcode == 6:  # bdv instruction
            reg_b = reg_a // 2**combo_operand
        elif opcode == 7:  # cdv instruction
            reg_c = reg_a // 2**combo_operand
        instruction_ptr += 2
    return output


def part_two(reg_b, reg_c, program):
    q = deque()
    q.append((0, 1))
    while q:
        req_a, n = q.popleft()
        if n > len(program):
            return req_a

        for i in range(8):
            a = (req_a << 3) | i
            out = part_one(a, reg_b, reg_c, program)
            target = program[-n:]
            if out == target:
                q.append((a, n + 1))


def read_input(filename: str):
    with open(filename, "r") as f:
        reg_a = f.readline().split(": ")[1]
        reg_b = f.readline().split(": ")[1]
        reg_c = f.readline().split(": ")[1]
        f.readline()
        program = f.readline().split(": ")[1]
        return int(reg_a), int(reg_b), int(reg_c), [int(x) for x in program.split(",")]


reg_a, reg_b, reg_c, program = read_input("input.txt")
print(f"Part 1: {",".join(map(str, part_one(reg_a, reg_b, reg_c, program)))}")
print(f"Part 2: {part_two(reg_b, reg_c, program)}")
