import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def splitdata():
    # Membaca data dari file CSV
    df = pd.read_csv("20172021.csv")
    df = df.drop_duplicates(subset=['Years', 'Track Name'])

    name_counts = df.groupby(["Genre", "Years"]).size().reset_index(name="Count")
    # Membuat Selectbox untuk memilih nama
    selected_name = st.selectbox("Pilih Nama", df["Genre"].unique())
    selected_name_counts = name_counts[name_counts["Genre"] == selected_name]

    plt.plot(selected_name_counts["Years"], selected_name_counts["Count"])
    plt.title("Jumlah Kemunculan Nama per Tahun")
    plt.xlabel("Tahun")
    plt.ylabel("Jumlah Kemunculan")
    st.pyplot(plt)
