from pprint import pprint
import json

dict = {}

for outer in [x * 0.25 for x in range(4, 45)]:
    for inner in range(-6, 7):
        grind = round(outer+(inner/6), 2)
        
        if grind not in dict.keys():
            dict[grind] = [inner, outer]
        else:
            continue

dict = {k: dict[k] for k in sorted(dict.keys())}

curr_inner = float(input('Enter current inner value: '))
curr_outer = float(input('Enter current outer value: '))
curr_grind = round(curr_outer+(curr_inner/6), 2)


while True:
    
    print('\nCurrent grind:', curr_grind)
    action = input('Press +/- to increase/decrease grind or (q) to exit: ')

    if action == '+':
        index = list(dict.keys()).index(curr_grind) + 1
        next_grind = list(dict.keys())[index]
        
        print('\nNext grind:', next_grind)
        print('\nInner change:', dict[next_grind][0] - curr_inner, f' (set to {dict[next_grind][0]})')
        print('Outer change:', dict[next_grind][1] - curr_outer, f' (set to {dict[next_grind][1]})')
        
        curr_grind = next_grind
        curr_inner = dict[next_grind][0]
        curr_outer = dict[next_grind][1]
        
    elif action == '-':
        index = list(dict.keys()).index(curr_grind) - 1
        next_grind = list(dict.keys())[index]
        
        print('\nNext grind:', next_grind)
        print('\nInner change:', dict[next_grind][0] - curr_inner, f' (set to {dict[next_grind][0]})')
        print('Outer change:', dict[next_grind][1] - curr_outer, f' (set to {dict[next_grind][1]})')
        
        curr_grind = next_grind
        curr_inner = dict[next_grind][0]
        curr_outer = dict[next_grind][1]
        
    elif action == 'q':
        print('Exiting...\n')
        break
    
    else:
        print('Invalid input! Try again.')
        continue
        
# with open('C:/Users/YASHASWAT/Desktop/grind_dict.json', 'w') as jsonfile:
#     json.dump(dict, jsonfile, indent=4)
