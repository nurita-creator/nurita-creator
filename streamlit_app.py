import streamlit as st
from PIL import Image
import numpy as np

# Placeholder untuk model (bisa diganti dengan model sebenarnya)
def dummy_predict(image):
    # Contoh logika sederhana (harus diganti dengan model asli)
    # Misalnya: jika gambar terang = rapi, gelap = tidak rapi
    avg_brightness = np.array(image).mean()
    return "Rapi" if avg_brightness > 100 else "Tidak Rapi"

# Judul aplikasi
st.title("Deteksi Kerapian Seragam")

# Upload gambar
uploaded_file = st.file_uploader("Unggah gambar seragam", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_column_width=True)

    # Prediksi kerapian
    with st.spinner("Mendeteksi..."):
        result = dummy_predict(image)
    
    # Tampilkan hasil
    st.subheader("Hasil Deteksi:")
    st.success(f"Seragam terdeteksi: *{result}*")
