import streamlit as st
from grammy import grammychart
from laguterbaik import memilih
from eksis import splitdata
import datetime

def greeting():
    current_time = datetime.datetime.now()
    current_hour = current_time.hour

    if current_hour < 11:
        waktu = "Pagi"
    elif current_hour < 15:
        waktu = "Siang"
    elif current_hour < 18 :
        waktu = "Sore"
    else:
        waktu = "Malam"

    st.title("Selamat " + waktu +" Pendengar Musik")
    st.write("Selamat datang di aplikasi musik.")

def main():
    greeting()
    pilihan = st.selectbox("Pilih Opsi:", ["","Lagu Terbaik", "Artist Terbaik yang Memenangkan Grammy", "Top Genre 2017 sampai 2021"])
    if pilihan == "Lagu Terbaik":
        memilih()
    elif pilihan == "Artist Terbaik yang Memenangkan Grammy":
        grammychart()
    elif pilihan == "Top Genre 2017 sampai 2021":
        splitdata()

main()