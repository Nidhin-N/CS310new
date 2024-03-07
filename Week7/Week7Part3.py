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
        node = select(root)
        result = playOut(node.state)
        backpropogate(node, result)
    best_next_state = best_child(root, 0)
    return best_next_state.state

def evaluate(state):
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


def select(node):
    while not node.state[0] == ():
        if len(node.children) < len(nextstates(node.state)):
            return expansion(node)
        else:
            node = best_child(node, 2)
    return node

def expansion(node):
    unplayed_states = []
    for s in nextstates(node.state):
        is_played = False
        for child in node.children:
            if s == child.state:
                is_played = True
                break
        if not is_played:
            unplayed_states.append(s)

    new_state = random.choice(unplayed_states)
    new_player = 1 if node.player == 2 else 2
    child_node = Node(new_state, new_player, parent=node)
    node.children.append(child_node)

    return child_node

def playOut(state):
    while state[0]:
        state = random.choice(nextstates(state))
    return state[1]

def backpropogate(node, v):
    while node is not None:
        node.visits += 1
        node.value += v
        node = node.parent

def best_child(node, exploration_weight):
    best_score = float('-inf')
    best_children = []
    for child in node.children:
        ucb_score = child.value / child.visits + exploration_weight * math.sqrt(2 * math.log(node.visits) / child.visits)
        if ucb_score == best_score:
            best_children.append(child)
        elif ucb_score > best_score:
            best_score = ucb_score
            best_children = [child]
    return random.choice(best_children)

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
