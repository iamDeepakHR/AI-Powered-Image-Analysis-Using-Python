# **Gemini Image Analysis Using Streamlit**

This project leverages **Google's Gemini API** to perform **AI-powered image analysis** within a **Streamlit** web application. Users can upload images and receive AI-generated insights based on their queries.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

---

## **Project Overview**

The **Gemini Image Analysis System** integrates **Google's Generative AI** to analyze images and generate insights based on user prompts. The application provides a seamless **user interface** through **Streamlit**, making AI-powered image interpretation **accessible and intuitive**.

---

## **Features**

- **AI-Powered Image Analysis**: Uses Google's **Gemini API** for advanced image insights.
- **Multiple Image Formats Supported**: Works with `JPG`, `JPEG`, and `PNG`.
- **Real-Time AI Responses**: Generates instant insights based on user queries.
- **Interactive and User-Friendly UI**: Streamlit-based interface for seamless interaction.
- **Secure API Key Management**: Uses `.env` files to store API keys securely.
- **Error Handling and Robust Processing**: Ensures smooth operation with efficient exception handling.

---

## **Technology Stack**

- **Frontend**:
  - **Streamlit** (for UI and interaction)
  - **Pillow** (for image processing)
  
- **Backend**:
  - **Google Generative AI (Gemini API)** (for AI-driven insights)
  - **Python** (for processing and integration)
  - **dotenv** (for environment variable management)

---

## **Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/iamDeepakHR/AI-Powered-Image-Analysis-Using-Python.git
cd AI-Powered-Image-Analysis-Using-Python
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure API Key**
1. **Create a `.env` file** in the project directory.
2. Add the following line and replace it with your actual API key:
   ```
   GENAI_API_KEY=YOUR_API_KEY
   ```

---

## **Usage**

### **Run the Application**
```bash
streamlit run app.py
```

### **How to Use**
1️⃣ Upload an image (`JPG`, `JPEG`, or `PNG`).  
2️⃣ Enter a description or query about the image.  
3️⃣ Click **Analyze Image** to receive AI-generated insights.  

---

## **Project Structure**
```
📂 Gemini-Image-Analysis
│-- 📜 app.py            # Main Streamlit App
│-- 📜 requirements.txt  # Project dependencies
│-- 📜 .env              # API Key (Not to be shared)
│-- 📜 README.md         # Documentation
```

---

## **Contributing**
We welcome contributions to enhance the project. If you would like to contribute:

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-name`).
3. **Make your changes and commit them** (`git commit -m 'Add feature'`).
4. **Push to your forked repository** (`git push origin feature-name`).
5. **Submit a pull request** for review.

---

## **License**
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details..

---

## **Author**
👨‍💻 Developed by **Deepak H R** 🚀

