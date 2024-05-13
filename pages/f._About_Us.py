import streamlit as st
import requests

from streamlit_lottie import st_lottie

st.title('PSB (Padang Sukabumi Bogor)')

st.header('Anggota Kelompok')
st.subheader('1. Muhammad Fadil Nugraha (2360178)')
st.subheader('2. Mutia Azatil ismah(2360191)')
st.subheader('3. Said Muhammad Iqbal (2360253)')
st.header('Contact Person')
st.subheader('Fadil (085624826410)')
st.subheader('Muti (083161993086)')
st.subheader('Iqbal (085771008112)')

# file json format (File path)
lottie_url="https://lottie.host/acebf761-e872-435e-b43f-1c19cac74529/1SAS32qZRd.json"

# Fungsi untuk momproses lottie url
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
# Memproses animasi lottie
lottie_json=load_lottie_url(lottie_url)

#pembuatan 2 kolom
col1,col2= st.columns([1,2])

#Menampilkan animasi lottie
with col2 :
    if lottie_json is not None:
        st_lottie(lottie_json)
    else:
        st.write("Failed to load Lottie animation.")