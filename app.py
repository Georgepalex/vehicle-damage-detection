import streamlit as st
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if uploaded_file is not None:

    image_path = "temp_file.jpg"

    # Save uploaded image
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display image
    st.image(uploaded_file, caption="Uploaded File", use_container_width=True)

    # Predict
    prediction = predict(image_path)

    st.info(f"Predicted Class: {prediction}")
