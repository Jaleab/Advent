try:
    set
except NameError:
    from sets import Set as set

def checkFields(fields, startIndex):
    eclValues = ['amb','blu','brn','gry','grn','hzl','oth']
    hclValues = set('0123456789abcdef')
    pidValues = set('0123456789')
    valids = 0
    for x in fields:
        field = x.split(':')
        if field[0] != 'cid':
            if field[0] == 'byr' and (1920 <= int(field[1]) <= 2002):
                valids += 1
            elif field[0] == 'ecl' and field[1] in eclValues:
                valids += 1
            elif field[0] ==  'eyr' and (2020 <= int(field[1]) <= 2030):
                valids += 1
            elif field[0] == 'hcl' and len(field[1]) == 7 and set((field[1])[1:]).issubset(hclValues):
                valids += 1
            elif field[0] == 'hgt':
                if field[1].find('cm') > 0 and 150 <= int((field[1])[:-2]) <= 193: 
                    valids += 1
                elif field[1].find('in') > 0 and 59 <= int((field[1])[:-2]) <= 76: 
                    valids += 1
            elif field[0] == 'iyr' and 2010 <= int(field[1]) <= 2020:
                valids += 1
            elif field[0] == 'pid' and len(field[1]) == 9 and set(field[1]).issubset(pidValues):
                valids += 1
    return valids == 7


input = open("Day4_PassportProcessing\\input.txt")
data = input.read().splitlines()

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
    fields.sort() # Taking advantage of python's default sort (timsort)
    if (length == 8 or length == 7 and ('cid' not in passport)) and checkFields(fields,length):
        validPassports += 1
print("Amount of valid passports: ", validPassports)
