input = open("Day2_PasswordPhilosohpy\input.txt")
inputList = input.readlines()
policies = []
valids = 0
for x in inputList:
    #policies.append(x.split(" "))
    policy = x.split(" ")
    letter = policy[1][0]
    limits = policy[0].split("-")
    #count = policy[2].count(letter)
    if((policy[2][int(limits[0])-1] == letter) ^ (policy[2][int(limits[1])-1] == letter)):
        valids = valids + 1
        #print(policy[2], limits, policy[2][int(limits[0])-1], policy[2][int(limits[1])-1], letter)
print(valids)