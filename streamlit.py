import streamlit as st
import pandas as pd

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })
#
# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])
#
# 'You selected: ', option

df = pd.read_csv('games_of_all_time.csv')
df2 = df1.drop(['url'], 1)

option = st.selectbox(
    'What genre would you like to find games for?',
    df2[]
)