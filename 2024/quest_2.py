import re
quest_no = "02"


def part_1(input):
    words, runes = input.splitlines()[::2]
    words = words[6:].split(",")
    matches = sum([len(re.findall(word, runes)) for word in words])
    return matches

def part_2(input):
    words = input.splitlines()[0][6:]
    words = set(v for w in words.split(",") for v in [w, w[::-1]]) # why do i use double comprehensions, they're so difficult to read
    # set to avoid repeats
    runes = input.splitlines()[2:]
    
    # go character by character:
    # starting from that character, check if it (+ next characters if necessary) match a word
    # if they do, add their positions to a set (to avoid duplicates) (can't end their because some words are longer than others) - can I fix this by sorting and going in descending order? Maybe but i cba
    # then the size of the set is the number of matched symbols
    matches = 0
    for line in runes:
        matching_symbols = set()
        for pos, char in enumerate(line):
            for word in words:
                if line[pos:pos+len(word)] == word:
                    # matched a word
                    matching_symbols.update(range(pos, pos + len(word)))
                
        matches += len(matching_symbols)

    return matches


def part_3(input):
    # it ain't pretty (and it definitely isn't fast) but it works
    # so I'll just do this the same way as before

    words = input.splitlines()[0][6:]
    words = set(v for w in words.split(",") for v in [w, w[::-1]]) # why do i use double comprehensions, they're so difficult to read
    # set to avoid repeats
    runes = input.splitlines()[2:]

    width = len(runes[0])
    height = len(runes)

    # pad each horizontal line so it's it's length repeated
    # grab the verticals
    padded_lines = [l + l[:-1] for l in runes]
    verts = ["".join([l[i] for l in runes]) for i in range(width)]

    # check each character to see if it's in a word, then add those positions
    line_matches = []
    for line in padded_lines:
        matching_symbols = set()
        for pos, char in enumerate(line):
            for word in words:
                if line[pos:pos+len(word)] == word:
                    # matched, add the positions MODULO WIDTH
                    matching_symbols.update(i % width for i in range(pos, pos + len(word)))
        line_matches.append(matching_symbols)

    # do the same with the verticals
    vert_matches = []
    for vert in verts:
        matching_symbols = set()
        for pos, char in enumerate(vert):
            for word in words:
                if vert[pos:pos+len(word)] == word:
                    matching_symbols.update(i % height for i in range(pos, pos + len(word)))
        vert_matches.append(matching_symbols)

    # need to convert the vertical indices back into normal ones
    # if i is in jth element of vert_matches,
    # then the ith line is a match at position j
    converted_verts = [set() for _ in range(height)]
    for j, vert in enumerate(vert_matches):
        for i in vert:
            converted_verts[i].add(j)
    
    # combine vert and line matches
    matched_symbols = [line_matches[i].union(converted_verts[i]) for i in range(height)]

    
    return sum(len(s) for s in matched_symbols)


prefix = f'inputs/everybody_codes_e2024_q{quest_no}_p'

with open(f'{prefix}1.txt') as f:
    input = f.read()
    print(part_1(input))

with open(f'{prefix}2.txt') as f:
    input = f.read()
    print(part_2(input))

with open(f'{prefix}3.txt') as f:
    input = f.read()
    print(part_3(input))
