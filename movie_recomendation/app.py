import streamlit as st
import pickle
import pandas as pd
import requests


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')


selected_movie_name = st. selectbox(
'Choose a movie u watched recently ',
movies['title'].values)

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(names[0])
    
    with col2:
        st.header(names[1])
        
    with col3:
        st.header(names[2])
       
    with col4:
        st.header(names[3])
        
    with col5:
        st.header(names[4])    
