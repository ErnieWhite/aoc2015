"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.
He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him
via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his new location.
However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and
Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:
    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""
import turtle
s = turtle.getscreen()

t = turtle.Turtle()
t.speed(0)
s.colormode(255)

def move(direction, location, presents):
    if direction == '^':
        t.pencolor((255, 0, 0))
        t.setheading(0)
        t.fd(5)
        location = location[0], location[1] + 1
    if direction == '<':
        t.pencolor((0, 255, 0))
        t.setheading(270)
        t.fd(5)
        location = location[0] - 1, location[1]
    if direction == 'v':
        t.pencolor((0, 0, 255))
        t.setheading(180)
        t.fd(5)
        location = location[0], location[1] - 1
    if direction == '>':
        t.pencolor((0, 0, 0))
        t.setheading(90)
        t.fd(5)
        location = location[0] + 1, location[1]
    presents[location] = presents.get(location, 0) + 1
    return location, presents


def main():
    with open('data/day3input.txt', 'r', encoding='utf-8') as f:
        directions = f.read().strip()
        santa_location = (0, 0)
        robot_location = (0, 0)

        presents = {santa_location: 1}
        presents[robot_location] = presents.get(robot_location, 0) + 1
        for i, direction in enumerate(directions):
            if i % 2 == 0:
                santa_location, presents = move(direction, santa_location, presents)
            else:
                robot_location, presents = move(direction, robot_location, presents)
        print(len(presents))


if __name__ == "__main__":
    main()
    a = input("press enter")