def next_states(s):
    allString = []
    if s.endswith("I"):
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

def extend_path(s1):
    path = []
    states = next_states(s1[-1])
    for i in range(len(states)):
        path.append(s1 + [states[i]])
    return path

def breadth_first_search(goalString):
    agenda = [["MI"]]
    agendaMaxLen = 1
    extendCount = 0
    while agenda:
        path = agenda.pop(0)
        currentState = path[-1]
        if currentState == goalString:
            return path, extendCount, agendaMaxLen
        if extendCount >= 5000:
            return [0,0,0]
        nextStates = extend_path(path)
        extendCount += 1
        agenda.extend(nextStates)
        agendaMaxLen = max(agendaMaxLen, len(agenda))

    return [0,0,0]

agendaMax = 0

def depthlimited_dfs(goalString, limit):
    agenda = [["MI"]]
    global agendaMax
    extendCount = 0
    while agenda:
        path = agenda.pop(0)
        currentState = path[-1]
        if currentState == goalString:
            return path, extendCount, agendaMax
        if len(path) <= limit:
            nextStates = extend_path(path)
            extendCount += 1
            agenda = nextStates + agenda
            agendaMax = max(agendaMax, len(agenda))
    return [0,0,0]


def dfs_iter(goalString):
    global agendaMax
    agendaMax = 0
    limit = 2
    extendCount = 0
    agendaMaxLen = 1
    while depthlimited_dfs(goalString, limit) == [0, 0, 0] and limit < 50:
        currentPath, extendC, agendaMax = depthlimited_dfs(goalString, limit+1)
        extendCount += extendC
        agendaMaxLen = max(agendaMaxLen, agendaMax)
        limit += 1
    return currentPath, extendCount, agendaMax

currentPath, extendCount, agendaMaxLen = depthlimited_dfs("MIU",8)
print(currentPath)
print(agendaMaxLen)
print(extendCount)

currentPath, extendCount, agendaMaxLen  = dfs_iter("MUIIU")
print(currentPath)
print(agendaMaxLen)
print(extendCount)


currentPath, extendCount, agendaMaxLen  = dfs_iter("MIUIUIUIU")
print(currentPath)
print(agendaMaxLen)
print(extendCount)



"""
currentPath, extendCount, agendaMaxLen  = breadth_first_search("MUIU")
print(currentPath)
print(agendaMaxLen)
print(extendCount)
#Number of Expansions: 15
#Max Agenda: 20
#Solution Length: 5
#Solution: ['MI', 'MII', 'MIIII', 'MIIIIU', 'MUIU']

currentPath, extendCount, agendaMaxLen = breadth_first_search("MIUIUIUIU")
print(currentPath)
print(agendaMaxLen)
print(extendCount)
#Number of Expansions: 6
#Max Agenda: 6
#Solution Length: 4
#Solution: ['MI', 'MIU', 'MIUIU', 'MIUIUIUIU']
print(extend_path(["MI","MII"]))    #[["MI","MII","MIIU"], ["MI","MII","MIIII"]]
print(extend_path(["MI","MUI"]))    #[["MI","MUI","MUIU"], ["MI","MUI","MUIUI"]]


print(next_states("MI"))    # ["MIU","MII"]
print(next_states("MIU"))   # ["MIUIU"]
print(next_states("MUI"))   # ["MUIU","MUIUI"]
print(next_states("MIIII")) # ["MIIIIU","MIIIIIIII","MUI","MIU"]
print(next_states("MUUII")) # ["MUUIIU","MUUIIUUII","MII"]
print(next_states("MUUUI")) # ["MUUUIU","MUUUIUUUI","MUI"]
"""
