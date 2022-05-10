import streamlit as st
import pickle
import pandas as pd

lst =list()
ifile = open("itemdf.pkl","rb")
itemdf = pickle.load(ifile)

for items in itemdf:
    lst.append(items)


def top_animes(anime_name):
    count = 1
    print('Users who watch {} also like:\n'.format(anime_name))
    for item in itemdf.sort_values(by = anime_name, ascending = False).index[1:6]:
        st.write('{}'.format( item))
        count +=1 

st.title("Anime Recommendation System")
option = st.selectbox(
     'Select Anime of your intrest',
     lst)

if st.button('Recommend'):
    top_animes(option)