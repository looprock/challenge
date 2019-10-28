#!/usr/bin/env python
import sys

gladiators = {
    0: 5,
    1: 4,
    2: 3,
    3: 0,
}

weapons = [3,2,5,1]
print(gladiators)
print(weapons)

def find_weapons(check_weapons):
    found_weapons = 0
    for i in check_weapons:
        if i in gladiators.values():
            found_weapons = found_weapons + 1
    return found_weapons
    
def defeat_gladiators(weapons):
    match = 0
    for i in range(len(gladiators.keys())):
        if gladiators[i] == weapons[i]:
            match = match + 1
    return match

num_gladiators = len(gladiators.keys())
finished = False
total_tries = 8
tries = 1
while not finished:
    if tries > total_tries:
        sys.exit("Max tries exceeded!")
    return_results = [find_weapons(weapons), defeat_gladiators(weapons)]
    print("try: %d" % (tries))
    if (return_results[0] == num_gladiators and return_results[1] == num_gladiators):
        finished = True
    else:
        print("[%d, %d]" % (return_results[0], return_results[1]))
    tries = tries + 1


