# Open the input file
with open('2024/1/input.txt', 'r') as file:
    first = []
    second = []

    for line in file:
        columns = line.split()
        if len(columns) >= 2:
            first.append(int(columns[0]))
            second.append(int(columns[1]))

first.sort()
second.sort()
difference = []
for i in range(len(first)):
    difference.append(abs(first[i] - second[i]))

rate = [] # 2 to len(first) set
# rate[0] will have the number from the first list and rate[1] will have the number of times that number appears in the second list
for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            if first[i] not in rate:
                rate.append([first[i], 1])
            else:
                rate[rate.index(first[i])][1] += 1

newrate = 0
for i in range(len(rate)):
    newrate += rate[i][0]*rate[i][1]

#print("First Column:", first)
#print("Second Column:", second)
#print("Difference:", difference)
print("Sum of differences:", sum(difference)) # part one
print("Rate:", rate)
print("sum of rate:", newrate) # part two