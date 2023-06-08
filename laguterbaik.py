import streamlit as st
import pandas as pd

def memilih():
    st.title("Data Selection")

    # Membaca file CSV
    df = pd.read_csv('20172021.csv')
    df = df.drop_duplicates(subset=['Years', 'Artist'])
    
    # Membuat slide bar untuk memilih tahun
    selected_year = st.slider("Pilih Tahun", 2017, 2021)

    # Membuat pilihan antara Nama atau Genre
    selection = st.radio("Pilih Kategori", options=["Nama", "Genre"])

    if selection == "Genre":
        # Mendapatkan genre yang unik dari data
        genres = pd.concat([df['Genre'], df['Genre2'], df['Genre3'],df['Genre4'],
                            df['Genre5'],df['Genre6'],df['Genre7'],df['Genre8'],
                            df['Genre9'],df['Genre10']])
        unique_genres = genres.unique()

        # Multiple select box untuk memilih genre
        selected_genres = st.multiselect("Pilih Genre", options=unique_genres)

        # Menampilkan hasil berdasarkan genre yang dipilih
        filtered_df = df[(df['Years'] == selected_year) & ((df['Genre'].isin(selected_genres))|(df['Genre2'].isin(selected_genres))
                                                           |(df['Genre3'].isin(selected_genres))|(df['Genre4'].isin(selected_genres))
                                                           |(df['Genre5'].isin(selected_genres))|(df['Genre6'].isin(selected_genres))
                                                           |(df['Genre7'].isin(selected_genres))|(df['Genre8'].isin(selected_genres))
                                                           |(df['Genre9'].isin(selected_genres))|(df['Genre10'].isin(selected_genres)))]
        result = filtered_df[['Track Name','Artist','Streams']]
        st.write(result)

    elif selection == "Nama":
        # Mendapatkan nama-nama yang unik dari data
        names = df['Artist'].unique()

        # Select box untuk memilih nama
        selected_name = st.selectbox("Pilih Artis ", options=names)

        # Menampilkan hasil berdasarkan nama yang dipilih
        filtered_df = df[(df['Years'] == selected_year) & (df['Artist'] == selected_name)]
        result = filtered_df[['Track Name','Artist','Streams']]
        st.write(result)

