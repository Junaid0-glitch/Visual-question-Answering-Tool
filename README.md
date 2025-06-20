
# 🧠🔍 Visual Question Answering Tool

A simple and powerful web app built with **Streamlit** that lets you ask questions about images using a transformer-based **Visual-Language model (ViLT)**. Powered by Hugging Face and `dandelin/vilt-b32-finetuned-vqa`.

---

## 🚀 Live Demo

👉 [Click here to try the live app](https://visual-question-answering-tool-fgf38kh3m3l8n5yea4oq9l.streamlit.app/)

---

## ✨ Features

- 🖼️ Upload `.jpg`, `.jpeg`, or `.png` images
- ❓ Ask natural language questions about the image
- 🤖 Uses ViLT model from Hugging Face
- ⚡ Fast and responsive answers
- 🧪 Clean UI built with Streamlit

---

## 📸 Screenshots

| Upload & Ask |
|--------------|
![Screenshot 2025-06-20 172440](https://github.com/user-attachments/assets/0d5bc396-40cc-46a6-b628-59a0b932c9f5)


---

## 🧩 How It Works

1. **ViLTProcessor** encodes both image and text into tensor format.
2. **ViLTForQuestionAnswering** predicts the most likely answer.
3. The result is shown instantly on the web app.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Junaid0-glitch/Visual-question-Answering-Tool.git
cd Visual-question-Answering-Tool
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Hugging Face Token

Create a `.env` file in the root folder and add:

```env
HUGGINGFACE_TOKEN=your_token_here
```

Get your token from: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## ▶️ Run the App Locally

```bash
streamlit run app.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📦 Requirements

- `streamlit`
- `transformers`
- `Pillow`
- `python-dotenv`
- `torch`

---

## 🧠 Model Used

Model: [`dandelin/vilt-b32-finetuned-vqa`](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa)  
Task: Visual Question Answering (VQA)

---

## 🛡️ Security Notes

- The Hugging Face token is stored in `.env`, which is excluded via `.gitignore`.
- Do **not** commit your token or secrets to GitHub.

---

