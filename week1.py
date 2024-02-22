def collatz(n):
    seq = []
    seq.append(n)
    while n != 1:
        if n%2==0:
            n = n/2
            seq.append(n)
        else:
            n = n*3+1
            seq.append(n)
    return len(seq)

def biggest_seq(end):
    seqN = 1
    seqL = 1
    for i in range(1, end):
        if collatz(i) > seqL:
            seqN = i
            seqL = collatz(i)
    return seqN, seqL

def has_aaa(string):
    chars = list(string.lower())
    for i in range(len(chars)-2):
        if chars[i] == chars[i + 1] == chars[i + 2] == 'a':
            return True
    return False

def make_bunch(high, low, green, budget):
    highValue = 4
    lowValue = 2
    greenValue = 0.5
    hFlower = 0
    lFlower = 0
    greenery = 0
    if green >= 4 and budget > 0:
        total = 2
        greenery += 4
        maxHigh = 4
        if high < 4:
            maxHigh = high

        for i in range(maxHigh):
            if total + 4 <= budget:
                total += 4
                hFlower += 1
            else:
                break

        for i in range(low):
            if total + 2 <= budget:
                total += 2
                lFlower += 1
            else:
                break

        if green > 4:
            for i in range(green-4):
                if total + 0.5 <= budget:
                    total += 0.5
                    greenery += 1
                else:
                    break
        if total == budget:
            bunch = [hFlower, lFlower, greenery]
            return bunch
    return []


#Test cases
print(collatz(12))
print(collatz(100))
print(collatz(50))
print(collatz(1))
print(collatz(5))
print(collatz(7))
print(collatz(18))

seqN, seqL = biggest_seq(100000)
print("Value of N = " + str(seqN))
print("Length = " + str(seqL))

seqN, seqL = biggest_seq(35000)
print("Value of N = " + str(seqN))
print("Length = " + str(seqL))

print(has_aaa("testString"))
print(has_aaa("teststraaang"))
print(has_aaa("teststrAAAng"))
print(has_aaa("teststraang"))


print(make_bunch(4, 8, 10, 15)) #[3,0,6]
print(make_bunch(3, 8, 10, 19)) #[3,2,6]
print(make_bunch(4, 8, 2, 15)) #[]
print(make_bunch(4, 1, 6, 23)) #[]
print(make_bunch(0, 0, 0, 25)) #[]
print(make_bunch(5, 5, 8, 22))
print(make_bunch(3, 4, 2, 44))
print(make_bunch(5, 1, 4, 20)) #[4,1,4]
print(make_bunch(4, 100, 100, 25)) #[4,3,6]
print(make_bunch(6, 0, 4, 24)) #[4,0,4]
