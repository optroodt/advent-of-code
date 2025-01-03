from utils import load_file

lines = load_file()


def get_rules(p, rs):
    return [r for r in rs if r.endswith(f"|{p}")]


def apply_rule(a, b, rs):
    for r in rs:
        if r == f"{a}|{b}":
            return a, b
        if r == f"{b}|{a}":
            return b, a
    return a, b


def is_correct(p, px, rs):
    for x in px[1:]:
        for r in rs:
            if r.startswith(f"{x}|"):
                return False
    return True


def run():
    rules = []
    orders = []
    target = rules
    for line in lines:
        if line == "":
            target = orders
            continue
        target.append(line)

    rules.sort()

    total_correct = 0
    tally = 0
    incorrect = []
    for order in orders:
        pages = order.split(",")
        breaking = 0
        for i, page in enumerate(pages):
            rs = get_rules(page, rules)
            if not is_correct(page, pages[i:], rs):
                breaking += 1
        if breaking == 0:
            total_correct += 1
            tally += int(pages[len(pages) // 2])
        else:
            incorrect.append(pages)

    print("Part One", tally)

    for inc in incorrect:
        prev = []
        while True:
            for i in range(len(inc) - 1):
                inc[i], inc[i + 1] = apply_rule(inc[i], inc[i + 1], rules)
            if inc == prev:
                break
            else:
                prev = inc[:]
    tally = 0
    for inc in incorrect:
        tally += int(inc[len(inc) // 2])
    print("Part Two:", tally)


if __name__ == "__main__":
    run()
