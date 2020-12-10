input = open("Day4_PassportProcessing\\input.txt")
data = input.read().splitlines()
#print(data)
counter = 0
passports = []
passports.append("")
for x in data:
    if len(x) != 0:
        passports[counter] += ' ' + x
    else:
        passports.append("")
        counter += 1
        
validPassports = 0
for passport in passports:
    fields = passport.split(' ')
    fields.pop(0)
    length = len(fields)
    if length == 8 or (length == 7 and ('cid' not in passport)):        
        print(fields, length)
        validPassports += 1
print("Amount of valid passports: ", validPassports)
