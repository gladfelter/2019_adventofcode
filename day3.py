#! /usr/bin/python3

import sys


class point(object):

    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

    def __repr__(self):
        return '(%d,%d)' % (self.x, self.y)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __key(self):
        return (self.x, self.y)

    def __hash__(self):
        return hash(self.__key())

    def copy(self):
        return point(self.x, self.y)

    def pointsTo(self, instruction):
        distance = int(instruction[1:])
        if instruction[0] == 'D':
            return [point(self.x, self.y + i, self.dist + i) for i in range(1, distance + 1)]
        elif instruction[0] == 'U':
            return [point(self.x, self.y - i, self.dist + i) for i in range(1, distance + 1)]
        elif instruction[0] == 'L':
            return [point(self.x - i, self.y, self.dist + i) for i in range(1, distance + 1)]
        elif instruction[0] == 'R':
            return [point(self.x + i, self.y, self.dist + i) for i in range(1, distance + 1)]

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)



def main():
    with open(sys.argv[1]) as day3:
        first = getPoints(day3.readline())
        second = getPoints(day3.readline())
    intersections = list(first & second)
    print('\n'.join([str(i) for i in intersections]))
    closest = intersections[0]
    origin = point(0, 0, 0)
    min_distance = origin.manhattan(closest)
    for p in intersections[1:]:
        distance = origin.manhattan(p)
        if distance < min_distance:
            min_distance = distance
            closest = p

    print(closest, min_distance)

    first_distances = dict([(p, p.dist) for p in first])
    second_distances = dict([(p, p.dist) for p in second])

    min_distance2 = first_distances[intersections[0]] + second_distances[intersections[0]]
    closest2 = intersections[0]
    for p in intersections[1:]:
        distance = first_distances[p] + second_distances[p]
        if distance < min_distance2:
            min_distance2 = distance
            closest2 = p
    print(closest2, min_distance2)
        

def getPoints(instructions):
    pos = point(0, 0, 0)
    points = set()
    for instruction in instructions.split(','):
      new_points = pos.pointsTo(instruction)
      points = points | set(new_points)
      pos = new_points[-1:][0]
    return points


if __name__ == '__main__':
    main()
