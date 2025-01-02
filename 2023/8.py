import math
import pathlib
import re
import string
import operator
from collections import Counter

path = pathlib.Path("8.txt")
with path.open("r") as fh:
    lines = list(map(str.strip, fh.readlines()))


class Node:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        l_value = self.left.value if self.left is not None else ""
        r_value = self.right.value if self.right is not None else ""
        return f"<Node value={self.value} left={l_value} right={r_value}>"

    def set_nodes(self, left, right):
        self.left = left
        self.right = right

    def is_end(self):
        return self.value == "ZZZ"
        return self.left is None and self.right is None

    def is_start_node(self):
        return self.value[2] == "A"

    def is_end_v2(self):
        return self.value[2] == "Z"

    def get_node_for_instruction(self, instruction):
        if instruction == "L":
            return self.left
        elif instruction == "R":
            return self.right


def run():
    lookup = {}
    instructions = lines[0]

    nodes = reversed(lines[2:])

    for i, node in enumerate(nodes):
        value, rest = node.split(" = ")
        left, right = rest.strip("()").split(", ")
        print(value, left, right)
        n = lookup.setdefault(value, Node(value))
        # if value[2] != "Z":
        n.set_nodes(
            lookup.setdefault(left, Node(left)),
            lookup.setdefault(right, Node(right)),
        )
    start_value = "AAA"
    print(lookup)
    print(instructions)
    print(len(instructions))
    # print(lookup.get("DCR"))
    # exit()
    node = lookup.get(start_value)
    steps = 0
    while not node.is_end():
        for instruction in instructions:
            steps += 1
            # print(node)
            new_node = node.get_node_for_instruction(instruction)
            node = new_node
            # if steps % 100 == 0:
            #     print(f"taken {steps} steps")

    # correct: 14257
    print(steps, node, node.is_end())
    # exit()
    print("----- v2 -------")

    start_nodes = []
    end_nodes = []
    new_nodes = []
    steps = 0
    for k, v in lookup.items():
        if v.is_start_node():
            start_nodes.append(v)
        if v.is_end_v2():
            end_nodes.append(v)
    print(start_nodes)
    print(end_nodes)
    # print(all(list(map(lambda x: x.is_start_node(), start_nodes))))
    # exit()
    # for k, node in lookup.items():
    #     if node.left is None or node.right is None:
    #         print(node)

    start_node = start_nodes[0]

    steps_per_node = {}
    for start_node in start_nodes:
        steps = 0
        while not start_node.is_end_v2():
            for instruction in instructions:
                steps += 1
                start_node = start_node.get_node_for_instruction(instruction)
        steps_per_node[start_node.value] = steps
        print(steps, start_node)
    print(steps_per_node)
    # correct: 16187743689077
    print(math.lcm(*steps_per_node.values()))


if __name__ == "__main__":
    run()
