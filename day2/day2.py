#part1
def part_1(input):
    position = [0,0]
    for i in range(len(input)):
        directions = input[i].split(" ")
        if directions[0] == 'forward':
            position[1] = position[1] + int(directions[1])
        elif directions[0] == 'up':
            position[0] = position[0] + int(directions[1])
        elif directions[0] == 'down':
            position[0] = position[0] - int(directions[1])
        else:
            print("you suck")

    answer = abs(position[0] * position [1])
    return answer

#part2
def part_2(input):
    position = [0,0, 0]
    for i in range(len(input)):
        directions = input[i].split(" ")
        if directions[0] == 'forward':
            position[0] = position[0] + int(directions[1])
            position[1] = position[1] - (position[2] * int(directions[1]))
        elif directions[0] == 'up':
            position[2] = position[2] - int(directions[1])
        elif directions[0] == 'down':
            position[2] = position[2] + int(directions[1])
        else:
            print("you suck")
    answer = abs(position[0] * position [1])
    return answer

with open(r"\Users\flesc\Projects\advent-of-code-21\day2\input.txt", "r") as f:
    input = f.read().splitlines()

print(part_1(input))
print(part_2(input))