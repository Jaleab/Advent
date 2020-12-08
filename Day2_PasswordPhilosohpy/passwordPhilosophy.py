input = open("Day2_PasswordPhilosohpy\inputPassword.txt")
inputList = input.readlines()
policies = []
valids = 0
for x in inputList:
    #policies.append(x.split(" "))
    policy = x.split(" ")
    letter = policy[1][0]
    limits = policy[0].split("-")
    count = policy[2].count(letter)
    if(int(limits[0]) <= count and int(limits[1]) >= count):
        valids = valids + 1
    #print(letter, policy[2], count, valids, limits)
    #print(limits)

    #print(letter)
#print(policies)
