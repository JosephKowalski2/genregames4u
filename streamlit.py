import streamlit as st
import pandas as pd
from PIL import Image

#Loading data into Dataframe and cleaning data
df = pd.read_csv('games_of_all_time.csv')
df2 = df.drop(['url', 'developer'], 1)
df2.fillna('No Data', inplace=True)
df2['genre'] = df2['genre'].str.replace('[', '', regex=True)
df2['genre'] = df2['genre'].str.replace(']', '', regex=True)
df2['genre'] = df2['genre'].str.replace("'", '', regex=True)
df2['genre'] = df2['genre'].str.replace("'", '', regex=True)
df2['platform'] = df2['platform'].str.replace('[', '', regex=True)
df2['platform'] = df2['platform'].str.replace(']', '', regex=True)
df2['platform'] = df2['platform'].str.replace("'", '', regex=True)
df2['platform'] = df2['platform'].str.replace("'", '', regex=True)

#Banner image
image = st.container()
with image:
    banner =Image.open('Genre games4u.png')
    st.image(banner, width=800)

with st.sidebar:
    score_average = st.slider('Average MetaScore and UserScore', 0, 100, 0)
    score_meta = st.slider('Meta score', 0, 100, 0)
    score_user = st.slider('User score', 0, 100, 0)
    video_game = st.text_input('Search for video game name')


#Game recommender
def recommender(searched_genre):
    games = df2[df2['genre'].str.contains(searched_genre, case=False)]
    # games = temp.reset_index()
    st.dataframe(games.query(f'((meta_score + user_score) / 2) >= {score_average}').sample(10).style.format({'user_score': '{:.2f}', 'meta_score': '{:.2f}'}))
    return games.query('((meta_score + user_score) / 2) > 50.0').sample(10)


searched_genre = st.selectbox('Genre Select', ['Beat-Em-Up',
                              '2D',
                              '3D',
                              'Action',
                              'Action Adventure',
                              'Action RPG',
                              'Adventure',
                              'Arcade',
                              'Breeding/Constructing',
                              'Card Battle',
                              'City Building',
                              'Compilation',
                              'Console-style RPG',
                              'Dancing',
                              'Driving',
                              'Fantasy',
                              'Fighting',
                              'First-Person',
                              'Futuristic',
                              'GT / Street',
                              'General',
                              'Government',
                              'Historic',
                              'Horror',
                              'Ice Hockey',
                              'Japanese-Style',
                              'Massively Multiplayer',
                              'Massively Multiplayer Online',
                              'Military',
                              'Miscellaneous',
                              'Modern',
                              'Music',
                              'No Data',
                              'Olympic Sports',
                              'Other',
                              'PC-style RPG',
                              'Party',
                              'Pinball',
                              'Platformer',
                              'Puzzle',
                              'Racing',
                              'Rally / Offroad',
                              'Role-Playing',
                              'Sci-Fi',
                              'Scrolling',
                              'Shooter',
                              'Simulation',
                              'Sports',
                              'Strategy',
                              'Third-Person',
                              'Traditional',
                              'Turn-Based',
                              'Tycoon',
                              'WWI'])
try:
    recommender(searched_genre)
except:
        # st.text('No games available in this range')
        st.markdown("<h1 style='text-align: center; color: blue;'>No games available in this range </h1>",
                    unsafe_allow_html=True)

text = st.container()
with text:
    st.caption('All data gathered from Kaggle')
    st.caption('All scores are based on https://www.metacritic.com')
    st.caption('Dataset gathered from https://www.kaggle.com/datasets/xcherry/games-of-all-time-from-metacritic')