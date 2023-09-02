#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description='Elves and Calories solution')
    parser.add_argument('-f', '--file', help="Puzzle input raw file")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        inventory = f.readlines()

    elf = 0
    all_elves = []
    for entry in inventory:
        if entry != "\n":
            elf = elf + int(entry)
        else:
            all_elves.append(elf)
            elf = 0

    # Part 1
    print(max(all_elves))

    # Part 2
    top_three = 0
    for i in range(0, 3):
        top_three = top_three + max(all_elves)
        all_elves.remove(max(all_elves))

    print(top_three)

if __name__ == "__main__":
    main()
