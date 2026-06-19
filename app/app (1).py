
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Crop Disease Detection",
    page_icon="🌱",
    layout="centered"
)

# -----------------------------------
# Load Model
# -----------------------------------
model = tf.keras.models.load_model("crop_disease_model.h5")

# -----------------------------------
# Load Class Names
# -----------------------------------
with open("class_names.json", "r") as f:
    classes = json.load(f)

# Convert dictionary to list if needed
if isinstance(classes, dict):
    classes = list(classes.keys())

# -----------------------------------
# Disease Solutions
# -----------------------------------
solutions = {
    "Tomato___Early_blight":
    "Use fungicide and remove infected leaves.",

    "Tomato___Late_blight":
    "Avoid overwatering and apply fungicide.",

    "Tomato___healthy":
    "Plant is healthy.",

    "Potato___Early_blight":
    "Use disease-free seeds and fungicide spray.",

    "Potato___Late_blight":
    "Remove infected plants and improve air circulation."
}

# -----------------------------------
# Title
# -----------------------------------
st.title("🌱 Crop Disease Detection System")

st.write(
    "Upload a leaf image to detect crop disease."
)

# -----------------------------------
# Upload Image
# -----------------------------------
uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------------
# Prediction
# -----------------------------------
if uploaded_file is not None:

    # Open Image
    image = Image.open(uploaded_file).convert("RGB")

    # Show Image
    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Resize
    img = image.resize((224, 224))

    # Convert to Array
    img_array = np.array(img)

    # Normalize
    img_array = img_array / 255.0

    # Expand Dimensions
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)

    # Get Predicted Index
    predicted_index = int(np.argmax(prediction))

    # Get Disease Name
    result = classes[predicted_index]

    # Clean Name
    result_display = result.replace("___", " - ")
    result_display = result_display.replace("_", " ")

    # Confidence
    confidence = float(np.max(prediction) * 100)

    # -----------------------------------
    # Display Result
    # -----------------------------------
    st.success(f"Detected Disease: {result_display}")

    st.info(f"Confidence: {confidence:.2f}%")

    # -----------------------------------
    # Treatment Suggestion
    # -----------------------------------
    if result in solutions:
        st.warning(
            f"Treatment Suggestion: {solutions[result]}"
        )
    else:
        st.warning(
            "No treatment information available."
        )

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
st.markdown(
    "Developed using Deep Learning and Streamlit 🚀"
)
