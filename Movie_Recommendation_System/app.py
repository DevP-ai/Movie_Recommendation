import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
st.header("Movie Recommendation System", divider="rainbow")

selected_movie_name = st.selectbox("Movie Name", movies['title'].values)

if st.button('Recommend'):
    st.write(selected_movie_name)
