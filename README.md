# 🧠 NexLens – Image Analysis

This project leverages **API KEY** to perform AI-powered image analysis within a **Streamlit** web application. Users can upload images and receive AI-generated insights based on their queries.

🌐 **Live Demo:** [Click here to try NexLens Image Analysis](https://ai-nexlens.onrender.com/)

---

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 📌 Project Overview

The **NexLens Image Analysis System** integrates Google's **Generative AI (Gemini API)** to analyze images and generate insights based on user prompts. The application provides a seamless UI through **Streamlit**, making AI-powered image interpretation accessible and intuitive.

---

## ✨ Features

- 🧠 **AI-Powered Image Analysis** – Uses Gemini API for advanced image understanding.
- 🖼️ **Supports JPG, JPEG, PNG** – Upload and analyze popular image formats.
- ⚡ **Real-Time AI Responses** – Get instant, insightful feedback.
- 💡 **User-Friendly Interface** – Clean and interactive UI with Streamlit.
- 🔐 **Secure API Management** – API keys managed safely using `.env`.
- 🛡️ **Robust Error Handling** – Smooth user experience with clean failure handling.

---

## 🛠️ Technology Stack

**Frontend:**
- Streamlit (UI & interaction)
- Pillow (image processing)

**Backend:**
- Google Generative AI (Gemini API)
- Python
- dotenv (for secure environment variables)

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/iamDeepakHR/AI-Powered-Image-Analysis-Using-Python.git
cd AI-Powered-Image-Analysis-Using-Python
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Mac/Linux
venv\Scripts\activate         # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Key

Create a `.env` file in the project directory and add:

```
GENAI_API_KEY=your_google_gemini_api_key
```

---

## ▶️ Usage

### Run the App

```bash
streamlit run app.py
```

### How to Use

1. Upload an image (JPG, JPEG, or PNG).
2. Enter a query or description related to the image.
3. Click **"Analyze Image"** and get AI-generated insights instantly!

---

## 📁 Project Structure

```
📂 NexLens-Image-Analysis
│-- 📜 app.py             # Main Streamlit app
│-- 📜 requirements.txt   # Project dependencies
│-- 📜 Procfile           # For deployment on platforms like Render/Heroku
│-- 📜 .env               # API key (keep secret)
│-- 📜 README.md          # Project documentation
```

---

## 🤝 Contributing

We welcome contributions to improve the project!
To contribute:

1. Fork the repo.
2. Create a new branch: `git checkout -b feature-name`
3. Make changes and commit: `git commit -m "Add feature"`
4. Push: `git push origin feature-name`
5. Submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

👨‍💻 Developed by **Deepak H R**

* 🌐 [GitHub](https://github.com/iamDeepakHR)
* 🔗 [LinkedIn](https://linkedin.com/in/iamdeepakhr)

---
