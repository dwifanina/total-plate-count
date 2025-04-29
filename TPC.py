import streamlit as st

# Judul aplikasi
st.title("Perhitungan Total Plate Count (TPC)")

# Input jumlah koloni
jumlah_koloni = st.number_input("Masukkan Jumlah Koloni:", min_value=0, step=1)

# Input volume sampel
volume_sampel = st.number_input("Masukkan Volume Sampel (mL):", min_value=0.0, step=0.1)

# Tombol untuk menghitung TPC
if st.button("Hitung TPC"):
    if volume_sampel > 0:
        tpc = jumlah_koloni / volume_sampel
        st.success(f"Total Plate Count (TPC): {tpc:.2f} CFU/mL")
    else:
        st.error("Volume sampel harus lebih besar dari 0.")
