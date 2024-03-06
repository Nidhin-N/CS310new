import random
import time
import math

class Node:
    def __init__(self, state, player, parent=None):
        self.state = state
        self.player = player
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

# Main function to run game
def Nim():
    # initial variables
    initialState = []
    state = ()

    print("Let's play Nim")

    # Add try catch to ensure only valid values are accepted
    valid = False
    while not valid:
        try:
            # Get piles and sticks
            numPiles = input("How many piles initially? ")
            maxSticks = input("Maximum number of sticks? ")

            # Create initial state
            for i in range(int(numPiles)):
                # Use random numbers to generate random number of sticks
                sticks = random.randint(1,int(maxSticks))
                initialState.append(sticks)

            # set first or second go and create state
            print("The initial state is " + str(initialState))
            print("Do you want to play a) first or b) second")
            turn = input("Enter a or b")
            if(str(turn).lower() ==  "a"):
                state = (initialState,1) #user is always MAX player
                valid = True

            elif(str(turn).lower() == "b"):
                state = (initialState,2) #AI is always MIN player
                valid = True

            else:
                raise ValueError("Invalid Input")
        except ValueError:
            print("invalid input, please re-enter")

    # Return state so we can start game
    return state


# THe user turn, let them choose
def userturn(state):
    # Next states called here (import from your own code)
    succ = nextstates(state)

    # if only an empty state left, pick the stick and return
    if(len(succ)==1 and succ[0][0] ==[1]):    
        print("Only one stick left, and you picked it up")
        return succ[0]
    if(len(succ)==1 and succ[0][0] ==[]):    
        print("You picked up the last stick!")
        return succ[0]
    # Print list of moves
    print("Next move options:")
    for i in range(len(succ)):
        print(str(i) + ".    " + str(succ[i][0]))
    moveIndex = input("Enter next move option number ")
    print("You moved to state " + str(succ[int(moveIndex)][0]))

    # Set new state and return
    state = succ[int(moveIndex)]
    return state

history = {}


# Given a state, start the game
def game_begin(state):

    game_state = state

    print("game start ", game_state)
    # while no winner, keep alternating
    while game_state[0] != []:

        # You will need to create your own AI function
        if game_state[1] == 1:
             game_state = userturn(game_state)
        else:
             game_state = AI_player_mcts(game_state)
        print("state is", game_state)

    # if final state is 1, 2 wins
    if(game_state[1] == 2):
        print("You lost!")
    else:
        print("You won!")



def AI_player_mcts(state):
    root = Node(state, state[1])
    for _ in range(1000):
        while not terminalTest(root):
            node = select(root)
            result = rollout(node)
            backpropagation(node, result)
    return select(root)

def eval(state):
    total = 0
    count = 0
    #Check if state is not a terminalState
    while not terminalTest(state):
        #Generate successors
        successors = nextstates(state)
        #Choose random state from successors
        state = random.choice(successors)
        #Test the state to find if terminal
        total += terminalTest(state)    #total == t (total rewards)
        count += 1  #count == n
    return total / count    #value estimate (v)

def ucb(state):
    c = 2
    vi = eval(state)
    ni = state.visits
    print("Hello")
    return vi + c * math.sqrt((math.log(ni)/ni))

def select(root):
    max_ucb = float('-inf')
    selected_child = []
    print("Hey")
    if len(root.children) < len(nextstates(root.state)):
        expansion(root)
    else:
        for i in root.children:
            curr_ucb = ucb(i)
            if curr_ucb > max_ucb:
                max_ucb = curr_ucb
                selected_child = i
        return selected_child

def rollout(node):
    while not terminalTest(node):
        successors = nextstates(node)
        node = random.choice(successors)
    return node[1]

def expansion(node):
    if not node.children:
        return state
    max_ucb = float('-inf')
    selected_child = None
    for i in node.children:
        curr_ucb = ucb(i)
        if curr_ucb > max_ucb:
            max_ucb = curr_ucb
            selected_child = i
    return expansion(selected_child)

def backpropagation(node, v):
    while node.parent is not None:
        node.parent += v
        node = node.parent
    return node

def terminalTest(state):
    if state == ([], 1):
        return 1
    elif state == ([], 2):
        return -1
    else:
        return 0

def nextstates(state):
    # Function to get all next states
    # Need to change turn and generate possible options

    succ = []  # the next states
    # Successor state is the next player, so change turn
    turn = state[1]
    if (turn == 1):
        turn = 2
    else:
        turn = 1

    # Sort piles, i.e. state [3,2]
    piles = state[0]
    # Go through each pile and generate possible options
    for i in range(len(piles)):

        # Try removing 1, 2, or 3 sticks
        for rem in range(1, 4):
            # Remove rem sticks from a pile
            if piles[i] >= rem:
                next_state = piles.copy()
                next_state[i] = next_state[i] - rem

                # Check for any zeros and remove
                temp_state = []
                for zerocheck in range(len(next_state)):
                    if next_state[zerocheck] != 0:
                        temp_state.append(next_state[zerocheck])
                        temp_state.sort()

                # Add to next states
                succ.append((temp_state, turn))

    # removing duplicates from list
    res = []
    for i in succ:
        if i not in res:
            res.append(i)

    # Return the list of successors, possible outcomes
    return (res)

# Game, get state
init_state = Nim()
game_begin(init_state)
