# **Gemini Image Analysis Using Streamlit**

This project is a **Streamlit-based AI-powered image analysis tool** utilizing Google's **Gemini API** (Generative AI) to analyze and generate insights from uploaded images. The chatbot provides a **user-friendly interface** for seamless interaction with AI-powered image interpretation.

---

## **Features**
✅ AI-powered image analysis using Google's Gemini API  
✅ User-friendly Streamlit UI  
✅ Supports multiple image formats (`JPG`, `JPEG`, `PNG`)  
✅ Real-time response generation  
✅ Secure API key management with `.env`  
✅ Efficient error handling and robust exception handling  

---

## **Installation and Setup**

### **1️⃣ Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Configure API Key**
1. **Create a `.env` file** in the project directory.
2. Add the following line and replace with your actual API key:
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
3️⃣ Click **Analyze Image** to get AI-generated insights.  

---

## **Project Structure**
```
📂 gemini-image-analysis
│-- 📜 app.py            # Main Streamlit App
│-- 📜 requirements.txt  # Project dependencies
│-- 📜 .env              # API Key (Not to be shared)
│-- 📜 README.md         # Documentation
```

---

## **Dependencies**
- **Streamlit** - Web UI framework  
- **Google Generative AI (Gemini API)** - AI model for image analysis  
- **Pillow** - Image processing  
- **dotenv** - Environment variable management  

Install them using:  
```bash
pip install streamlit google-generativeai pillow python-dotenv
```

---

## **Contributing**
Want to improve this project? Contributions are welcome!  
- Fork the repository  
- Create a new branch (`feature-new-feature`)  
- Commit changes and open a pull request  

---

## **License**
This project is open-source under the **MIT License**.

---

## **Author**
👨‍💻 Developed by **Deepak H R** 🚀

