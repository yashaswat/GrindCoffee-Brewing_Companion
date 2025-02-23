from pprint import pprint
import json
import streamlit as st
from streamlit_lottie import st_lottie

col1, col2 = st.columns([0.25, 0.75])

with col1:
    with open("logo_anim.json", "r") as jsonfile:
        logo1 = json.load(jsonfile)
        
    st.lottie(logo1, loop=True, height=150, width=150, quality='medium')
    
with col2:
    st.title('Coffee Grinder Adjustment Tool')

st.divider()
st.write("Oh no! Can't make coffee because the companion app to your coffee grinder is down?")
st.write("No worries! _Use this, bitch!_")
st.divider()

dict = {}

for outer in [x * 0.25 for x in range(4, 45)]:
    
    for inner in range(0, 7):
                
        grind_pos = round(outer+(inner/6), 2)
        grind_neg = round(outer+((-inner)/6), 2)
        
        if grind_pos not in dict.keys():
            dict[grind_pos] = [inner, outer]
        if grind_neg not in dict.keys():
            dict[grind_neg] = [-inner, outer]
        else:
            continue

dict = {k: dict[k] for k in sorted(dict.keys())}

col1, col2, col3, col4, col5 = st.columns(5, vertical_alignment="center")
grind = 0

col1.button("Finer Grind")
col3.html(f"<h1 style='text-align: center; font-size: 48px;'>{grind}</h1>")
col5.button("Coarser Grind")


curr_inner = st.slider("**Inner Ring Value**", min_value=-6, max_value=6, step=1, value=-6)
curr_outer = st.slider("**Outer Ring Value**", min_value=1.0, max_value=12.0, step=0.25, value=0.0)
grind = round(curr_outer+(curr_inner/6), 2)

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
