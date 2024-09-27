# A State class for the Eight Puzzle
#
# name: Sean Zhang
# email: zsean@bu.edu

from board import *

MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    def __init__(self, board, predecessor, move):
        """ constructs a new State object by initializing a Board attribute by 
        registering an existing board, a predecessor attribute that stores a 
        reference to the State object that comes before this state in the 
        current sequence of moves, a move attribute that stores a string 
        representing the move that was needed to transition from the 
        predecessor state to this state, and a num-moves that stores an 
        integer value represening the number of moves it would take to get to 
        this state from the initial state. """
        self.board = board
        self.predecessor = predecessor
        self.move = move
        if self.predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = predecessor.num_moves + 1
        
    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        return True

    def is_goal(self):
        if self.board.tiles == GOAL_TILES:
            return True
        else:
            return False
    
    def generate_successors(self):
        """  creates and returns a list of State objects for all successor 
        states of the called State object. """
        successors = []
        for m in MOVES:
            b = self.board.copy()
            if b.move_blank(m) == True:
                s = State(b,self,m)
                successors += [s]
        return successors
    
    def print_moves_to(self):
        """ prints the sequence of moves that lead from the initial state to 
        the called State object.
        """
        if self.predecessor == None:
            print('initial state:')
            print(self.board)
        else:
            s = self.predecessor
            s.print_moves_to()
            print('move the blank ' + self.move + ':')
            print(self.board)
