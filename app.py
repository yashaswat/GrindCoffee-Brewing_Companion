import json
import time

import streamlit as st
from streamlit_lottie import st_lottie


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

# Uncomment to save the dictionary to a JSON file
# with open('C:/Users/YASHASWAT/Desktop/grind_dict.json', 'w') as jsonfile:
#     json.dump(grind_dict, jsonfile, indent=4)


col1, col2 = st.columns([0.25, 0.75])

with col1:
    with open("Media/logo_anim.json", "r") as jsonfile:
        logo1 = json.load(jsonfile)
        
    st.lottie(logo1, loop=True, height=150, width=150, quality='medium')
    
with col2:
    st.title('GrindCoffee: Your Brewing Companion')

st.divider()
st.write("Oh no! Can't make coffee because the companion app to your coffee grinder is down?")
st.write("No worries! _Use this bad boy!_")
st.divider()
st.write('\n')


def recipe(brew_type):

    with open('recipes.json', 'r', encoding='utf-8') as f:
        recipes = json.load(f)['recipes']
        
        for user_brew in recipes:
            if user_brew['name'] == brew_type:
                recipe_box.markdown(f"### :coffee: {user_brew['name']}")
                recipe_box.image(user_brew['image'], use_container_width=True)
                recipe_box.markdown(f"**Grind Size:** {user_brew['grind_size']}")
            
                recipe_box.markdown("#### Ingredients:")
                for ingredient, amount in user_brew["ingredients"].items():
                    recipe_box.markdown(f"- **{ingredient.capitalize()}**: {amount}")
                
                recipe_box.markdown("#### Equipment:")
                for item in user_brew["equipment"]:
                    recipe_box.markdown(f"- {item}")
                
                recipe_box.markdown("#### Steps:")
                for i, step in enumerate(user_brew["steps"], start=1):
                    recipe_box.markdown(f"{i}. {step}")
                
                break


st.subheader('Brewing Recipes', anchor=False)
st.write('\n')

brew_type = st.segmented_control('**Select your preferred home brewing method:**',
                     options=['French Press', 'Pour-Over', 'AeroPress', 'Moka Pot', 'Cold Brew'])
if brew_type:
    recipe_box = st.container(border=True)
    recipe(brew_type)
    
st.divider()
st.write('\n')


# Initialize session state variables
if 'curr_inner' not in st.session_state:
    st.session_state.curr_inner = -6
if 'curr_outer' not in st.session_state:
    st.session_state.curr_outer = 1.0
if 'curr_grind' not in st.session_state:
    st.session_state.curr_grind = round(st.session_state.curr_outer + (st.session_state.curr_inner / 6), 2)


def update_grind():
    st.session_state.curr_grind = round(st.session_state.curr_outer + (st.session_state.curr_inner / 6), 2)


def adjust_grind(direction):
    next_index = list(grind_dict.keys()).index(st.session_state.curr_grind) + direction
    if 0 <= next_index < len(grind_dict):
        next_grind = list(grind_dict.keys())[next_index]
        st.session_state.curr_grind = next_grind
        st.session_state.curr_inner = grind_dict[next_grind][0]
        st.session_state.curr_outer = grind_dict[next_grind][1]


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


st.subheader('Grind Size Assistant', anchor=False)
st.write('\n')

with st.container(border=True):
    col1, col2, col3, col4, col5 = st.columns(5, vertical_alignment="center")

    col1.image('Media/fine_grind.png')
    col2.button("Finer Grind", type='primary', on_click=lambda: adjust_grind(-1), use_container_width=True)
    
    col3.html(f"<h1 style='text-align: center; font-size: 48px;'>{st.session_state.curr_grind}</h1>")
    
    col4.button("Coarser Grind", type='primary', on_click=lambda: adjust_grind(1), use_container_width=True)
    col5.image('Media/coarse_grind.png')

toggle = st.toggle('Show slider adjust buttons')
st.write('\n')

with st.container(border=True):
    inner_col1, inner_col2, inner_col3 = st.columns([0.1, 0.8, 0.1])
    inner_col2.slider("**Inner Ring Value**", min_value=-6, max_value=6, step=1, on_change=update_grind, key='curr_inner')

    outer_col1, outer_col2, outer_col3 = st.columns([0.1, 0.8, 0.1])
    outer_col2.slider("**Outer Ring Value**", min_value=1.0, max_value=11.0, step=0.25, on_change=update_grind, key='curr_outer')

if toggle:
    inner_col1.button("\-", key='in\-', on_click=change_inner_slider, args=('minus',), use_container_width=True)
    inner_col3.button("\+", key='in\+', on_click=change_inner_slider, args=('plus',), use_container_width=True)
    
    outer_col1.button('\-', key='out\-', on_click=change_outer_slider, args=('minus',), use_container_width=True)
    outer_col3.button('\+', key='out\+', on_click=change_outer_slider, args=('plus',), use_container_width=True)

st.divider()
st.write('\n')


# initialize timer session states
if 'bloom' not in st.session_state:
    st.session_state.bloom = 30
if 'brew' not in st.session_state:
    st.session_state.brew = 180
if 'stir' not in st.session_state:
    st.session_state.stir = 10
if 'timer_active' not in st.session_state:
    st.session_state.timer_active = False
if 'audio_playing' not in st.session_state:
    st.session_state.audio_playing = False

def set_timers(bloom, brew, stir, timer_start):

    st.session_state.audio_playing = False
    st.session_state.bloom = bloom
    st.session_state.brew = brew
    st.session_state.stir = stir
    
    if timer_start:
        st.session_state.timer_active = True


def reset_timer():
    
    st.session_state.timer_active = False
    st.session_state.audio_playing = False
    
    set_timers(bloom, brew, stir, False)


def play_pause_timer():
    if st.session_state.timer_active:
        st.session_state.timer_active = False
    else:
        st.session_state.timer_active = True
    

def play_audio(path):
    sound = st.empty()
    audio_file = st.audio("Media/timer_alarm.mp3", autoplay=True, format="audio/mp3", end_time=0.20)

    hide_audio_style = """
    <style>
    .stAudio {
        display: none;
    }
    </style>
    """
    sound.markdown(hide_audio_style, unsafe_allow_html=True)


st.subheader('Brew Timer', anchor=False)
st.write('\n')

timer_col1, timer_col2 = st.columns([0.3, 0.7], gap='medium', border=True, vertical_alignment='center')

with timer_col1:

    bloom = st.number_input('Bloom Stage: ', min_value=15, value=30, step=15)
    brew = st.number_input('Brew Stage: ', min_value=15, value=180, step=15)
    stir = st.number_input('Stir & Pour Stage: ', min_value=0, value=10, step=5)
    st.write('\n')
    
    start_timer = st.button('Start Timer', type='primary', on_click=set_timers, args=(bloom, brew, stir, True), use_container_width=True)
        
    play_pause_col, reset_col = st.columns([0.65, 0.35], gap='small')
    play_pause_col.button('▶️/⏸️', type='primary', on_click=play_pause_timer, use_container_width=True)
    reset_col.button(':repeat:', type='primary', on_click=reset_timer, use_container_width=True)
    
    if start_timer:
        st.info('Timer started...') 
    
with timer_col2:
    
    st.image('Media/brew_banner.png')
    
    timer1, timer2, timer3 = st.columns(3, border=True)
    
    timer1.metric('Bloom', st.session_state.bloom)
    timer2.metric('Brew', st.session_state.brew)
    timer3.metric('Stir', st.session_state.stir)

while st.session_state.timer_active: 
    
    for stage in ['bloom', 'brew', 'stir']:
                
        while st.session_state[stage] > 0:
            
            progress_percent = (globals()[stage] - st.session_state[stage]) / globals()[stage]
            progress_bar = timer_col2.progress(progress_percent)

            st.session_state[stage] -= 1
            time.sleep(1)
            st.rerun()
    
    success_message = timer_col2.success('All Stages Complete! Enjoy your Coffee ☕️', icon="✅")
    st.session_state.audio_playing = True
    
    if st.session_state.audio_playing:
        play_audio('Media/timer_alarm.mp3')

    time.sleep(30)
    success_message.empty()
    
    st.session_state.timer_active = False

st.divider()
st.write('\n')
