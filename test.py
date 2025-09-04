import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Aplikasi Data Pengunjung Mingguan")

# Simpan data sementara di session_state
if "data_pengunjung" not in st.session_state:
    st.session_state.data_pengunjung = []

# Form input data pengunjung
with st.form("form_pengunjung", clear_on_submit=True):
    st.subheader("Input Data Pengunjung")
    nama = st.text_input("Nama")
    nomor = st.text_input("Nomor HP")
    alamat = st.text_input("Alamat")
    kunjungan = st.number_input("Jumlah Kunjungan (per minggu)", min_value=1, max_value=20, step=1)

    submitted = st.form_submit_button("Tambah Data")

    if submitted:
        if nama and nomor and alamat:
            st.session_state.data_pengunjung.append({
                "Nama": nama,
                "Nomor HP": nomor,
                "Alamat": alamat,
                "Jumlah Kunjungan": kunjungan
            })
            st.success(f"Data untuk {nama} berhasil ditambahkan.")
        else:
            st.warning("Harap lengkapi semua kolom!")

# Jika ada data, tampilkan
if st.session_state.data_pengunjung:
    df = pd.DataFrame(st.session_state.data_pengunjung)
    
    st.subheader("Tabel Data Pengunjung")
    st.dataframe(df)

    st.subheader("Grafik Jumlah Kunjungan")
    fig = px.bar(df, x="Nama", y="Jumlah Kunjungan", color="Nama", title="Jumlah Kunjungan Pengunjung per Minggu")
    st.plotly_chart(fig)
else:
    st.info("Belum ada data pengunjung yang dimasukkan.")
