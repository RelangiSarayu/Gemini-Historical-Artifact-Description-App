
# -----------------------------------
# Import Required Libraries
# -----------------------------------
import streamlit as st
import os
from google import genai
from google.genai import types
from PIL import Image

# -----------------------------------
# Configure API Key
# -----------------------------------
api_key = "Place_your_api_here"
client = genai.Client(api_key=api_key)

# -----------------------------------
# Streamlit Page
# -----------------------------------
st.set_page_config(
    page_title="Gemini Historical Artifact Description App",
    page_icon="🏺"
)

st.header("🏺 Gemini Historical Artifact Description App")

input_text = st.text_input("Input Prompt:")
uploaded_file = st.file_uploader(
    "Choose an image of an artifact...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width="stretch")

submit = st.button("Generate Artifact Description")

# -----------------------------------
# When Button Clicked
# -----------------------------------
if submit:

    try:
        prompt = f"""
        You are a historian.
        Describe the artifact in detail.
        Topic: {input_text}
        Include origin, historical context, cultural significance,
        and artistic details.
        """

        if uploaded_file:
            image_bytes = uploaded_file.getvalue()

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    prompt,
                    types.Part.from_bytes(
                        data=image_bytes,
                        mime_type=uploaded_file.type,
                    ),
                ],
            )
        else:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

        st.subheader("Description of the Artifact:")
        st.write(response.text)

    except Exception as e:
        st.error(f"Error: {str(e)}")
