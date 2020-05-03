wire1 = input().split(",")
wire2 = input().split(",")

wire1Coords = set(())
x, y = 0, 0
for segment in wire1:
    direction = segment[0]
    magnitude = int(segment[1:])
    for i in range(magnitude):
        if direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        elif direction == 'L':
            x += 1
        elif direction == 'R':
            x -= 1
        wire1Coords.add((x, y))


wire2Coords = set(())
x, y = 0, 0
for segment in wire2:
    direction = segment[0]
    magnitude = int(segment[1:])
    for i in range(magnitude):
        if direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        elif direction == 'L':
            x += 1
        elif direction == 'R':
            x -= 1
        wire2Coords.add((x, y))



intersections = wire1Coords.intersection(wire2Coords)

# minManDist = 9999999999
# minTuple = (0,0)
# for intersection in intersections:
#     manDist = abs(intersection[0]) + abs(intersection[1])
#     if manDist < minManDist:
#         minManDist = manDist
#         minTuple = intersection


def distTravelled(wire, point):
    x, y = 0, 0
    destX = point[0]
    destY = point[1]
    distTravelled = 0
    intersected = False

    for segment in wire:
        direction = segment[0]
        magnitude = int(segment[1:])

        for i in range(magnitude):
            distTravelled += 1
            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'L':
                x += 1
            elif direction == 'R':
                x -= 1
            if x == destX and y == destY:
                return distTravelled
    
    return -1

dist = 0
minDist = 9999999999
for intersection in intersections:
    dist = distTravelled(wire1, intersection)
    dist += distTravelled(wire2, intersection)
    minDist = min(minDist, dist)
print(minDist)