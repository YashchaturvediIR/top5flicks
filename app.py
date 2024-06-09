import streamlit as st
import  pickle
import pandas as pd
import  requests

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

st.title('Top5 Flicks')

st.image('bg_cinema.png',output_format="auto")
selected_movie_name = st.selectbox(
"This website only includes Hollywood movies released in 2016 or earlier. Please enter movie names accordingly",
(movies['title'].values))

similarity = pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=060721f51703478d2c2787d33d472137'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']
def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recomended_movies = []
        recomended_movies_posters = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recomended_movies.append(movies.iloc[i[0]].title)
            #fetch poster from API
            recomended_movies_posters.append(fetch_poster(movie_id))
        return recomended_movies, recomended_movies_posters

if st.button("Recommend"):
    name,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])




