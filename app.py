from pprint import pprint
import json
import streamlit as st
from streamlit_lottie import st_lottie

# Initialize session state variables
if 'curr_inner' not in st.session_state:
    st.session_state.curr_inner = -6
if 'curr_outer' not in st.session_state:
    st.session_state.curr_outer = 1.0
if 'curr_grind' not in st.session_state:
    st.session_state.curr_grind = round(st.session_state.curr_outer + (st.session_state.curr_inner / 6), 2)

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

# Create the grind dictionary
grind_dict = {}

for outer in [x * 0.25 for x in range(4, 45)]:
    
    for inner in range(-6, 7):
                
        grind = round(outer+(inner/6), 2)        
        
        if grind not in grind_dict.keys():
            grind_dict[grind] = [inner, outer]
        else:
            if abs(inner) < abs(grind_dict[grind][0]):
                grind_dict[grind] = [inner, outer]

grind_dict = {k: grind_dict[k] for k in sorted(grind_dict.keys())}

col1, col2, col3, col4, col5 = st.columns(5, vertical_alignment="center")

def update_grind():
    st.session_state.curr_grind = round(st.session_state.curr_outer + (st.session_state.curr_inner / 6), 2)

def adjust_grind(direction):
    index = list(grind_dict.keys()).index(st.session_state.curr_grind) + direction
    if 0 <= index < len(grind_dict):
        next_grind = list(grind_dict.keys())[index]
        st.session_state.curr_grind = next_grind
        st.session_state.curr_inner = grind_dict[next_grind][0]
        st.session_state.curr_outer = grind_dict[next_grind][1]

col2.button("Finer Grind", on_click=lambda: adjust_grind(-1), use_container_width=True)
col4.button("Coarser Grind", on_click=lambda: adjust_grind(1), use_container_width=True)

col3.markdown(f"<h1 style='text-align: center; font-size: 48px;'>{st.session_state.curr_grind}</h1>", unsafe_allow_html=True)

def change_inner_slider(direction):
    if direction=='minus' and st.session_state.curr_inner!=-6:
        st.session_state.curr_inner -= 1
        update_grind()
    elif direction=='plus' and st.session_state.curr_inner!=6:
        st.session_state.curr_inner += 1
        update_grind()

def change_outer_slider(direction):
    if direction=='minus' and st.session_state.curr_outer!=1.00:
        st.session_state.curr_outer -= 0.25
        update_grind()
    elif direction=='plus' and st.session_state.curr_outer!=11.00:
        st.session_state.curr_outer += 0.25
        update_grind()

inner_col1, inner_col2, inner_col3 = st.columns([0.1, 0.8, 0.1])
inner_col1.button("\-", key='in\-', on_click=change_inner_slider, args=('minus',))
inner_col2.slider("**Inner Ring Value**", min_value=-6, max_value=6, step=1, value=st.session_state.curr_inner, on_change=update_grind, key='curr_inner')
inner_col3.button("\+", key='in\+', on_click=change_inner_slider, args=('plus',))

outer_col1, outer_col2, outer_col3 = st.columns([0.1, 0.8, 0.1])
outer_col1.button('\-', key='out\-', on_click=change_outer_slider, args=('minus',))
outer_col2.slider("**Outer Ring Value**", min_value=1.0, max_value=11.0, step=0.25, value=st.session_state.curr_outer, on_change=update_grind, key='curr_outer')
outer_col3.button('\+', key='out\+', on_click=change_outer_slider, args=('plus',))

# Uncomment to save the dictionary to a JSON file
# with open('C:/Users/YASHASWAT/Desktop/grind_dict.json', 'w') as jsonfile:
#     json.dump(grind_dict, jsonfile, indent=4)
