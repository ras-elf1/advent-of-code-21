from statistics import mode
with open(r"\Users\flesc\Projects\advent-of-code-21\day3\input.txt", "r") as f:
    input = f.read().splitlines()

#part 1
def power_consumption(input):
    gamma=[]
    for x in range(len(input[0])):
        bit=[]
        for y in range(len(input)):
            bit.append(int(input[y][x]))
        gamma.append(mode(bit))
    epsilon = [item^1 for item in gamma]

    g = int("".join(str(i) for i in gamma),2)
    e = int("".join(str(i) for i in epsilon),2)

    answer = g * e
    return answer

print(power_consumption(input))