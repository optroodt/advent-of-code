from utils import load_file

lines = load_file()


def get_direction(a, b):
    dist = b - a
    if dist > 0:
        new_direction = True
    elif dist < 0:
        new_direction = False
    else:
        new_direction = None

    return new_direction


def is_safe(level):
    for i in range(len(level) - 1):
        cur_val, next_val = level[i], level[i + 1]
        if abs(next_val - cur_val) > 3:
            return False

        new_direction = get_direction(cur_val, next_val)
        if i == 0:
            direction = new_direction
        elif direction != new_direction or direction is None:
            return False
    return True


def run():
    levels = []
    for l in lines:
        levels.append(list(map(int, l.split(" "))))

    safe_counter_one = 0
    safe_counter_two = 0
    for n, level in enumerate(levels):
        if is_safe(level):
            safe_counter_one += 1

        for i in range(len(level)):
            lvl = level[:i] + level[i + 1 :]
            if is_safe(lvl):
                safe_counter_two += 1
                break

    print("Part One:", safe_counter_one)
    print("Part Two:", safe_counter_two)


if __name__ == "__main__":
    run()
