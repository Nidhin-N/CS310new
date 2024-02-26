import math
import time

def minimax_prune(state):
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

                # Add to next states
                succ.append((temp_state, turn))

    # removing duplicates from list
    res = []
    for i in succ:
        if i not in res:
            res.append(i)

    # Return the list of successors, possible outcomes
    return (res)


def min_value_prune(state, alpha, beta):
    if terminalTest(state):
        return -1
    v = float('-inf')
    for s in nextstates(state):
        vD = max_value_prune(s, alpha, beta)
        if vD < v:
            v = vD
        if vD <= alpha:
            return v
        if vD < beta:
            beta = vD
    return v

def max_value_prune(state, alpha, beta):
    if terminalTest(state):
        return 1
    v = float('inf')
    for s in nextstates(state):
        vD = min_value_prune(s, alpha, beta)
        if vD > v:
            v = vD
        if vD >= beta:
            return v
        if vD > alpha:
            alpha = vD
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

output = (test_timing(([5,5,5],1)))
print("Time within limit", output[0])
print("Value returned", output[1])