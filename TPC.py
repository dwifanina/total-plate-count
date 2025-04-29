Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import streamlit as st
... 
... # Judul aplikasi
... st.title("Perhitungan Total Plate Count (TPC)")
... 
... # Input jumlah koloni
... jumlah_koloni = st.number_input("Masukkan Jumlah Koloni:", min_value=0, step=1)
... 
... # Input volume sampel
... volume_sampel = st.number_input("Masukkan Volume Sampel (mL):", min_value=0.0, step=0.1)
... 
... # Tombol untuk menghitung TPC
... if st.button("Hitung TPC"):
...     if volume_sampel > 0:
...         tpc = jumlah_koloni / volume_sampel
...         st.success(f"Total Plate Count (TPC): {tpc:.2f} CFU/mL")
...     else:
