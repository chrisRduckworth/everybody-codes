def part_1(monsters):
    potions_per_monster = {"A": 0, "B": 1, "C": 3}
    total = sum(potions_per_monster[m] for m in monsters)
    return total


def part_2(monsters):
    potions_per_monster = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}
    pairs = [monsters[2*i:2*i+2] for i in range(len(monsters)//2)]
    total_potions = 0
    for p in pairs:
        potions = 0
        if "x" not in p:
            potions += 2
        potions += potions_per_monster[p[0]] + potions_per_monster[p[1]]
        total_potions += potions
    return total_potions


def part_3(monsters):
    potions_per_monster = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}
    triplets = [monsters[3*i:3*i+3] for i in range(len(monsters)//3)]
    total_potions = 0
    for t in triplets:
        potions = 0

        # make adjustment for having 2 or 3 monsters
        monster_count = 3 - t.count("x")
        monster_mult_adj = 2 - t.count("x")
        # if xxx, monster_mult_adj = -1 but then monster_count = 0 so it's 0 anyway
        potions += monster_count * monster_mult_adj

        potions += sum(potions_per_monster[m] for m in t)

        total_potions += potions

    return total_potions


prefix = "inputs/everybody_codes_e2024_q01_p"

with open(f'{prefix}1.txt') as f:
    monsters = list(f.read())
    print(part_1(monsters))

with open(f'{prefix}2.txt') as f:
    monsters = f.read()
    print(part_2(monsters))

with open(f'{prefix}3.txt') as f:
    monsters = f.read()
    print(part_3(monsters))
