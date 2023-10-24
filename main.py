import pickle
import streamlit as st
import requests
import pandas as pd
print('working')

def recommend(song):
    index = songs[songs['track_name'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_song_names = []
    for i in distances[0:6]:
        # fetch the movie poster
        song_id = songs.iloc[i[0]].id
        recommended_song_names.append(songs.iloc[i[0]].track_name)

    return recommended_song_names

st.header('Song Recommendation System')
song1 = pickle.load(open('new1.pkl','rb'))
songs=pd.DataFrame(song1)
similarity = pickle.load(open('simi.pkl','rb'))

song_list = songs['track_name'].values
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    song_list
)
if st.button('Show Recommendation'):
    recommended_song_names = recommend(selected_song)
    for i in range(6):
        st.write(recommended_song_names[i], unsafe_allow_html=True)
        