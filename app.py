import streamlit as st
import pandas as pd
import pickle as pk 

# ---------- Page Config ----------
st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🎥", layout="centered")

# ---------- Custom CSS ----------
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: #FAFAFA;
    font-family: 'Poppins', sans-serif;
}
div.stButton > button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 1em;
}
div.stButton > button:hover {
    background-color: #FF1E1E;
}
h1, h2, h3 {
    text-align: center;
    color: #F9CB40;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("🎬 Movie Recommender System")
st.write("### Type a movie name and get similar recommendations!")

# ---------- Input ----------
movie_name = st.text_input("🎥 Enter Movie Name", placeholder="e.g. Inception")

# ---------- Loading the model  ----------
model = pk.load(open('movi_recomender.pkl','rb'))
all_vector = pk.load(open('all_vector.pkl','rb'))

# ---------- Processing ----------
def recommend(m):
    idx = model[model['title']==m].index[0]
    movie_sim = all_vector[idx]
    movie_list_idx = sorted(list(enumerate(movie_sim)),reverse=True,key=lambda x:x[1])[1:6]
    l = [i[0] for i in movie_list_idx]
    ans=[]
    for i in l:
        ans.append(model.iloc[i]['title'])
    return ans 

# ---------- Button ----------
if st.button("🔍 Recommend"):
    if movie_name.strip() == "":
        st.error("Please enter a movie name.")
    else:
        recommendations = recommend(movie_name)
        if not recommendations:
            st.warning("No similar movies found. Try another name!")
        else:
            st.subheader("✨ Top 5 Recommendations:")
            for i, m in enumerate(recommendations, 1):
                st.markdown(f"**{i}. {m}** 🎞️")

# ---------- Footer ----------
st.markdown("---")
