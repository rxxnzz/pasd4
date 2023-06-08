import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def grammychart():
    # Membaca file CSV
    df = pd.read_csv('grammySongs.csv')

    # Menampilkan slider untuk memilih tahun
    genres_ = pd.concat([df['Genre']])
    genres = genres_.unique()
    selected_year = st.slider('Pilih Tahun', 1999, 2018)
    selected_genre = st.selectbox('Pilih Genre', genres)

    # Filter dataframe berdasarkan tahun yang dipilih
    filtered_df = df[(df['GrammyYear'] == selected_year) & (df['Genre'] == selected_genre)]
    filtered_df_year = df[df['GrammyYear'] == selected_year]


    # Menghitung jumlah artist yang namanya berulang atau hanya muncul sekali
    artist_counts = filtered_df_year['Artist'].value_counts()

    # Membuat bar chart
    st.title("Chart Bar Grammy")
    plt.bar(artist_counts.index, artist_counts.values)
    plt.xlabel('Nama Artist')
    plt.ylabel('Jumlah')
    plt.title(f'Pemenang Grammy Award Tahun ({selected_year})')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Menampilkan bar chart menggunakan Streamlit
    st.pyplot(plt)
    st.write("Lagu yang dipilih berdasarkan genre dan tahun")
    st.write(filtered_df)
