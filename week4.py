def next_states(s):
    allString = []
    if s[-1] == "I":
        allString.append(s + "U")
    if s[0] == "M":
        allString.append(s+s[1:])
    for i in range(len(s)-2):
        if s[i:i+3] == "III":
            allString.append(s[:i]+"U"+s[i+3:])
    for i in range(len(s)-1):
        if s[i:i+2] == "UU":
            allString.append(s[:i]+s[i+2:])
    return list(dict.fromkeys(allString))


def breadthfirstdictionarysearch(p):
    agenda = [["MI"]]
    visited = {"MI":["MII","MIU"]}
    agendaMaxLen = 1
    extendCount = 0
    while agenda:
        path = agenda.pop(0)
        currentState = path[-1]
        print("Current state:", currentState)
        print(visited)
        print("Agenda",agenda)
        if currentState == p:
            path = [currentState]
            while visited[currentState] is not None:
                currentState = visited[currentState]
                path.append(currentState)
            path.reverse()
            return path, extendCount, agendaMaxLen
        if extendCount >= 5000:
            return [0,0,0]
        nextStates = next_states(currentState)
        print("current state",currentState)
        print("Next states:", nextStates)
        for nextState in nextStates:
            if nextState not in visited:
                state = next_states(nextState)
                visited[nextState] = state
                agenda.extend(state)
                agendaMaxLen = max(agendaMaxLen, len(agenda))
                print("Added to agenda:", nextState)
        extendCount += 1
    return [0,0,0]

def estimate_steps(current, goal):
    if current == goal:
        return 0
    else:
        return 1

def astarsearch(goalString):
    visited = []


currentPath, extendCount, agendaMaxLen = breadthfirstdictionarysearch("MIUUIUUII")
print(currentPath)
print(agendaMaxLen)
print(extendCount)

print(next_states("MIUIU"))
print(next_states("MIIU"))
print(next_states("MIIII"))