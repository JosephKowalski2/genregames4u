import streamlit as st
import pandas as pd
from PIL import Image

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

image = Image.open('Genre games4u.png')
st.image(image, width=1000)

def recommender(searched_genre):
    games = df2[df2['genre'].str.contains(searched_genre, case=False)]
    # games = temp.reset_index()
    st.dataframe(games.query('((meta_score + user_score) / 2) > 50.0').sample(10).style.format({'user_score': '{:.2f}', 'meta_score': '{:.2f}'}))
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

recommender(searched_genre)