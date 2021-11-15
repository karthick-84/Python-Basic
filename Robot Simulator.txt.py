"""A robot simulator.
 
A robot factory's test facility needs a program to verify robot movements.
 
The robots have three possible movements:
 
- turn right
- turn left
- advance
 
Robots are placed on a hypothetical infinite grid, facing a particular
direction (north, east, south, or west) at a set of {x,y} coordinates,
e.g., {3,8}, with coordinates increasing to the north and east.
 
The robot then receives a number of instructions, at which point the
testing facility verifies the robot's new position, and in which
direction it is pointing.
 
- The letter-string "RAALAL" means:
  - Turn right
  - Advance twice
  - Turn left
  - Advance once
  - Turn left yet again
- Say a robot starts at {7, 3} facing north. Then running this stream
  of instructions should leave it at {9, 4} facing west.
 
"""
NORTH = complex(0, 1)
EAST = complex(1, 0)
SOUTH = complex(0, -1)
WEST = complex(-1, 0)
class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self._bearing = bearing
        self._coordinates = complex(x, y)
    @property
    def bearing(self):
        """Bearing is the direction the robot is facing"""
        return self._bearing
    @property
    def coordinates(self):
        """Current location of robot"""
        return (int(self._coordinates.real), int(self._coordinates.imag))
    def turn_left(self):
        """Make a left turn.
        In a complex number plain, multiplication by sqrt(-1) is
        equivalent to rotation by -90degrees
        """
        self._bearing *= complex(0, 1)
    def turn_right(self):
        """Make a right turn.
        A right turn is the opposite of a left turn.
        """
        self._bearing *= complex(0, -1)
    def advance(self):
        """Move robot 1 step in direction it is facing"""
        self._coordinates += self._bearing
    def simulate(self, command):
        """Make the robot perform a sequence of Left, Right, and
        Advance commands.
        """
        for c in command:
            {'L': self.turn_left,
             'R': self.turn_right,
             'A': self.advance}[c]()