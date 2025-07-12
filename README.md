# 🌾 Crop Recommendation System using Machine Learning

This project recommends the most suitable crop to grow based on soil and environmental parameters using a machine learning model. It is built with Python and deployed via a Streamlit web interface.

---

## 🚀 Features

- 🧠 Trained ML model on real crop yield dataset
- 🌱 Takes input for:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature (°C)
  - Humidity (%)
  - pH
  - Rainfall (mm)
- 🧮 Normalizes input using a pre-trained scaler
- 📊 Displays best crop suggestion
- 🖼 Beautiful UI with blurred background and glassmorphism input card

---

## 🚀 Live Demo

👉 [Click here to try the app!](https://crop-recommendation-systemgit.streamlit.app/)

---

## 📁 Project Structure

```
├── app.py                  # Main Streamlit app
├── model.pkl               # Trained machine learning model
├── model_scaler.pkl        # Scaler for input normalization
├── bg.jpg                  # Background image
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Shivam8320/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```

### 2. Create & Activate Virtual Environment *(optional but recommended)*
```bash
python -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate # For Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 📦 Dependencies

- streamlit
- numpy
- scikit-learn
- pickle-mixin

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Shivam Bhavsar**  
Connect on [LinkedIn](www.linkedin.com/in/shivam-bhavsar-b8ba91253) • [GitHub](https://github.com/Shivam8320)
