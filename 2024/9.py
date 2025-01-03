import pathlib


path = pathlib.Path("9.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


def run():
    line = lines[0]
    result = []
    _id = 0
    is_file = True
    for i in line:
        if is_file:
            result += [str(_id)] * int(i)
            _id += 1
            is_file = False
        else:
            result += ["."] * int(i)
            is_file = True

    W = len(result) - 1

    for i, c in enumerate(reversed(result)):

        if c != ".":
            for n in range(len(result)):
                if i + n >= W:
                    break
                if result[n] == ".":
                    result[n] = c
                    result[W - i] = "."
                    break
        if i + n >= W:
            break

    # print("".join(result))
    total = 0
    for i, n in enumerate(result[: result.index(".")]):
        total += i * int(n)

    print("Part One:", total)  # It's really slow :)


if __name__ == "__main__":
    run()
