def minimax_value(state):
    if state[1] == 1:
        return maxValue(state)
    else:
        return minValue(state)

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

def maxValue(state):
    if terminalTest(state):
        return 1
    v = float('-inf')
    for s in successors(state):
        v = max(v, minimax_value(s))
    return v

def minValue(state):
    if terminalTest(state):
        return -1
    v = float('inf')
    for s in successors(state):
        v = min(v, minimax_value(s))
    return v

def terminalTest(state):
    piles, player = state
    return sum(piles) == 0


print(minimax_value(([4],1)))       # Example Play: [([4], 1), ([1], 2), ([], 1)]                       1
print(minimax_value(([2,3],1)))     # Example Play: [([2, 3], 1)([2, 2], 2)([1, 2], 1)([1], 2)([], 1)]  1
print(minimax_value(([9,9],1)))
print(minimax_value(([5,5,5],1)))   # Example Play: [([5, 5, 5], 1)([4, 5, 5], 2)([1, 5, 5], 1)([5, 5], 2)([4, 5], 1)([3, 5], 2)([5], 1)([4], 2)([1], 1)([], 2)] -1
print(minimax_value(([1,2],2)))     # Example Play [([1, 2], 2)([1], 1)([], 2)] -1
