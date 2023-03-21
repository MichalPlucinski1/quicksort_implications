startingNum = 16
tab = []


for i in range(0, startingNum , 2):
    tab.append(i)

for i in range(startingNum - 1, 0, -2):
    tab.append(i)
print(tab) 
print(len(tab))