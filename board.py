# A Board class for the Eight Puzzle
#
# name: Sean Zhang
# email: zsean@bu.edu

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        self.digitstr = []
        for x in range(len(digitstr)):
            self.digitstr += digitstr[x]
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                position = 3*r + c
                self.tiles[r][c] = self.digitstr[position]
                if self.digitstr[position] == '0':
                    self.blank_r = r
                    self.blank_c = c
    
    def __repr__(self):
        """ returns a string representation of a Board object. """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    s += '_'+ ' '
                else:
                    s += self.tiles[r][c] + ' '
            s += '\n'
            
        return s
    
    def move_blank(self, direction):
        """ takes as input a string direction that specifies the direction 
        in which the blank should move, and that attempts to modify the 
        contents of the called Board object accordingly. """
        directions = ['up', 'down' , 'left', 'right']
        self.direction = direction
        if direction not in directions:
            return False
        else:
            if direction == 'up':
                if self.blank_r == 0:
                    return False
                else:
                    r = self.blank_r
                    c = self.blank_c
                    new = str(self.tiles[r-1][c])
                    self.tiles[r-1][c] = str(self.tiles[r][c])
                    self.tiles[r][c] = new
                    self.blank_r -= 1
                    return True
            elif direction == 'left':
                if self.blank_c == 0:
                    return False
                else: 
                    r = self.blank_r
                    c = self.blank_c
                    new = str(self.tiles[r][c-1])
                    self.tiles[r][c-1] = str(self.tiles[r][c])
                    self.tiles[r][c] = new
                    self.blank_c -= 1
                    return True
            elif direction == 'right':
                if self.blank_c == 2:
                    return False
                else: 
                    r = self.blank_r
                    c = self.blank_c
                    new = str(self.tiles[r][c+1])
                    self.tiles[r][c+1] = str(self.tiles[r][c])
                    self.tiles[r][c] = new
                    self.blank_c += 1
                    return True
            elif direction == 'down':
                if self.blank_r == 2:
                    return False
                else:
                    r = self.blank_r
                    c = self.blank_c
                    new = str(self.tiles[r+1][c])
                    self.tiles[r+1][c] = str(self.tiles[r][c])
                    self.tiles[r][c] = new
                    self.blank_r += 1
                    return True
    
    def digit_string(self):
        """ creates and returns a string of digits that corresponds to the 
        current contents of the called Board object’s tiles attribute. """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s += self.tiles[r][c]
        return s
    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy 
        of the called object. """
        new = Board(self.digit_string())
        return new
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board object 
        that are not in their respective goal state. """
        num = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != GOAL_TILES[r][c]:
                    if self.tiles[r][c] != '0':
                        num += 1
        return num
    
    def __eq__(self, other):
        """ changes when the == operator is used to compare two Board objects. """
        if self.digit_string() == other.digit_string():
            return True
        else:
            return False
