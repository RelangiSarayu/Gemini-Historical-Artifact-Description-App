🏺 Gemini Historical Artifact Description App

📌 Overview

The Gemini Historical Artifact Description App is a Streamlit-based web application that leverages Google's Gemini generative AI model to create detailed, engaging descriptions of historical artifacts.

🚀 Features

📝 Text-based artifact description generation

🖼 Image + prompt-based multimodal generation

⚡ Powered by Gemini 2.5 Flash

🎨 Interactive UI built with Streamlit

📜 Structured historian-style output

📂 Project Structure

Gemini-Historical-Artifact-Description-App/
app.py

test_models.py

requirements.txt

README.md

.gitignore

⚙️ Installation & Setup

1️⃣ Clone the Repository : 
cd your-repo-name

2️⃣ Create Virtual Environment (Recommended) : 
python -m venv venv

venv\Scripts\activate   

3️⃣ Install Dependencies : 
pip install -r requirements.txt

4️⃣ Add Your API Key : 
GOOGLE_API_KEY=your_api_key_here

5️⃣ Run the Application : 
streamlit run app.py

🏗 How It Works

User enters artifact topic and uploads an image.

The prompt is structured as a historian-style instruction.

The Gemini 2.5 Flash model processes the input.

The model generates a detailed artifact description.

The result is displayed in the Streamlit interface.


⭐ If you found this project interesting, consider giving it a star!

