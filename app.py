import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Grafik Pengujung Harian")

#input jumlah pengunjung
senin = st.slider("Senin", 0, 500, 150)
selasa = st.slider("Selasa", 0, 500, 130)
rabu = st.slider("Rabu", 0, 500, 120)
kamis = st.slider("Kamis", 0, 500, 110)
jumat = st.slider("Jumat", 0, 500, 200)

#simpan data ke dalam DataFrame
data = pd.DataFrame({
    "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
    "Pengunjung": [senin, selasa, rabu, kamis, jumat]
})

#tampilkan data dalam grafik bar
st.bar_chart(data.set_index("Hari"))

st.subheader("Jumlah Pengunjung Harian")
st.dataframe(data)

fig= px.bar(data, x="Hari", y="Pengunjung", title="Jumlah Pengunjung Harian")
st.plotly_chart(fig)