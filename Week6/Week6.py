import time

def minimax_prune(state):
    alpha = -1
    beta = 1
    if state[1] == 1:
        return max_value_prune(state, alpha, beta)
    else:
        return min_value_prune(state, alpha, beta)

def successors(state):
    next_states = []
    piles, player = state

    for i, pile in enumerate(piles):
        for taken in range(1, min(4, pile + 1)):
            new_piles = list(piles)  # Create a copy of piles
            new_piles[i] -= taken
            # Toggle player correctly for the next turn
            next_player = 2 if player == 1 else 1
            next_states.append((tuple(new_piles), next_player))

    return next_states


def min_value_prune(state, alpha, beta):
    if terminalTest(state):
        return -1
    v = float('inf')
    for s in successors(state):
        vD = max_value_prune(state, alpha, beta)
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
    v = float('-inf')
    for s in successors(state):
        vD = min_value_prune(state, alpha, beta)
        if vD > v:
            v = vD
        if vD >= beta:
            return v
        if vD > alpha:
            alpha = vD
    return v

def terminalTest(state):
    piles, player = state
    return sum(piles) == 0


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

output = (test_timing(([8,8],2)))
print("Time within limit", output[0])
print("Value returned", output[1])