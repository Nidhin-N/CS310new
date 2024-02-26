import sys


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
    agenda = ["MI"]
    visited = {"MI":None}
    agendaMaxLen = 1
    extendCount = 0
    while agenda:
        currentState = agenda.pop(0)
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
        for nextState in nextStates:
            if nextState not in visited:
                visited[nextState] = currentState
                agenda.append(nextState)
        agendaMaxLen = max(agendaMaxLen, len(agenda))
        extendCount += 1
    return [0,0,0]

def estimate_steps(current, goal):
    if current == goal:
        return 0
    else:
        return 1

def astarsearch(goalString):
    bestState = 0
    visited = {"MI": None}
    agenda = ["MI"]
    currentState = agenda[0]
    lowestCost = estimate_steps(agenda[0], goalString)
    agendaMaxLen = 1
    extendCount = 0
    while agenda:
        for state in agenda:
            i=0
            if lowestCost < estimate_steps(state, goalString):
                lowestCost = estimate_steps(state, goalString)
                bestState = i
            i+=1
        currentState = agenda.pop(bestState)
        if currentState == goalString:
            path = [currentState]
            while visited[currentState] is not None:
                currentState = visited[currentState]
                path.append(currentState)
            path.reverse()
            return path, extendCount, agendaMaxLen
        if extendCount >= 5000:
            return [0, 0, 0]
        nextStates = next_states(currentState)
        for nextState in nextStates:
            if nextState not in visited:
                visited[nextState] = currentState
                agenda.append(nextState)
        agendaMaxLen = max(agendaMaxLen, len(agenda))
        extendCount += 1
    return [0, 0, 0]

currentPath, extendCount, agendaMaxLen = breadthfirstdictionarysearch("MIUUIUUII")
print(currentPath)
print(agendaMaxLen)
print(extendCount)


currentPath, extendCount, agendaMaxLen = astarsearch("MIUUIUUII")
print(currentPath)
print(agendaMaxLen)
print(extendCount)


currentPath, extendCount, agendaMaxLen = astarsearch("MUIU")
print(currentPath)
print(agendaMaxLen)
print(extendCount)
