import streamlit as st

# Judul aplikasi
st.title("Perhitungan Total Plate Count (TPC)")

# Menampilkan gambar cara kerja
st.image("tpc_workflow.jpg", caption="Cara Kerja Perhitungan TPC", use_column_width=True)

# Deskripsi aplikasi
st.write("""
Aplikasi ini digunakan untuk menghitung Total Plate Count (TPC) berdasarkan jumlah koloni yang terhitung dan volume sampel.
Standar jumlah koloni yang valid untuk perhitungan TPC adalah antara 25 hingga 250 koloni.
Silakan masukkan nilai di bawah ini untuk melakukan perhitungan.
""")

# Input jumlah koloni
jumlah_koloni = st.number_input("Masukkan Jumlah Koloni (25-250):", min_value=0, step=1)

# Input volume sampel
volume_sampel = st.number_input("Masukkan Volume Sampel (mL):", min_value=0.0, step=0.1)

# Tombol untuk menghitung TPC
if st.button("Hitung TPC"):
    if 25 <= jumlah_koloni <= 250 and volume_sampel > 0:
        tpc = jumlah_koloni / volume_sampel
        st.success(f"Total Plate Count (TPC): {tpc:.2f} CFU/mL")
    else:
        if jumlah_koloni < 25 or jumlah_koloni > 250:
            st.error("Jumlah koloni harus antara 25 dan 250.")
        if volume_sampel <= 0:
            st.error("Volume sampel harus lebih besar dari 0.")
