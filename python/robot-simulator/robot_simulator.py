NORTH = 0
EAST = 1
SOUTH = 3
WEST = 4

class Robot(object):
    def __init__(self, direction = NORTH, x = 0, y = 0):
        self.bearing = direction
        self.coordinates = (x, y)

    def turn_right(self):
        if self.bearing == NORTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = WEST
        else:
            self.bearing = NORTH

    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = EAST
        else:
            self.bearing = NORTH

    def advance(self):
        (x, y) = self.coordinates
        if self.bearing == NORTH:
            self.coordinates = (x, y+1)
        elif self.bearing == EAST:
            self.coordinates = (x+1, y)
        elif self.bearing == SOUTH:
            self.coordinates = (x, y-1)
        else:
            self.coordinates = (x-1, y)

    def simulate(self, string):
        for char in string:
            if char == 'L':
                self.turn_left()
            elif char == 'R':
                self.turn_right()
            elif char == 'A':
                self.advance()
