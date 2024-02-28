import math
import time

visited = {}
def minimax_prune(state):
    global visited
    visited = {}
    alpha = float('-inf')
    beta = float('inf')
    if state[1] == 1:
        return max_value_prune(state, alpha, beta)
    else:
        return min_value_prune(state, alpha, beta)


def nextstates(state):
    # Function to get all next states
    # Need to change turn and generate possible options

    succ = []  # the next states

    # Successor state is the next player, so change turn
    turn = state[1]
    if turn == 1:
        turn = 2
    else:
        turn = 1

    # Sort piles, i.e. state [3,2]
    # Go through each pile and generate possible options
    for i in range(len(state[0])):

        # Try removing 1, 2, or 3 sticks
        for rem in range(1, 4):
            # Remove rem sticks from a pile
            if state[0][i] >= rem:
                new_piles = state[0][:i] + [state[0][i] - rem] + state[0][i + 1:]

                temp_state = []
                for zerocheck in range(len(new_piles)):
                    if new_piles[zerocheck] != 0:
                        temp_state.append(new_piles[zerocheck])
                        temp_state.sort()

                succ.append((temp_state, turn))

                # Add to next states

    # removing duplicates from list
    res = []
    for i in succ:
        if i not in res:
            res.append(i)
    # Return the list of successors, possible outcomes
    return res


def min_value_prune(state, alpha, beta):
    if terminalTest(state):
        return -1

    state_tuple = (tuple(state[0]), state[1])

    if state_tuple in visited:
        return visited[state_tuple]

    v = float('inf')
    for s in nextstates(state):
        vD = max_value_prune(s,alpha,beta)
        if vD < v:
            v = vD
        if vD <= alpha:
            return v
        if vD < beta:
            beta = vD
    visited[state_tuple] = v
    return v

def max_value_prune(state, alpha, beta):
    if terminalTest(state):
        return 1
    state_tuple = (tuple(state[0]), state[1])

    if state_tuple in visited:
        return visited[state_tuple]

    v = float('-inf')
    for s in nextstates(state):
        vD = min_value_prune(s, alpha, beta)
        if vD > v:
            v = vD
        if vD >= beta:
            return v
        if vD > alpha:
            alpha = vD
    visited[state_tuple] = v
    return v

def terminalTest(state):
    # Function to test if goal has been met
    # True if met, false if not
    if state == ([], 1):
        return 1
    elif state == ([], 2):
        return -1
    else:
        return 0

def test_timing(state):
    # Start a timer
    start = time.time()
    # Call minimax function
    value = minimax_prune(state)
    end = time.time()
    #calculate and return
    duration = end-start
    #print('Time taken:', duration)
    return duration, value



output = (test_timing(([6,4,2,3,5,5,5],1)))
print("Time within limit", output[0])
print("Value returned", output[1])