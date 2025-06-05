

# 🧠🔍 Visual Question Answering Tool

A simple and powerful web app built with **Streamlit** that lets you ask questions about images using a transformer-based **Visual-Language model (ViLT)**. Powered by Hugging Face and `dandelin/vilt-b32-finetuned-vqa`.

---

## 🚀 Demo

Upload an image and type a question — for example:

- 🖼️ Upload: a picture of a cat  
- ❓ Ask: "What animal is this?"  
- ✅ Answer: "cat"

---

## ✨ Features

- 🖼️ Upload `.jpg`, `.jpeg`, or `.png` images
- ❓ Ask natural language questions
- 🤖 ViLT model from Hugging Face (VisualBERT-like architecture)
- ⚡ Fast response
- 🧪 Streamlit interface

---

## 📸 Screenshots

| Upload Image | Ask Question | Get Answer |
|--------------|---------------|-------------|
| ![Screenshot 2025-06-06 005209](https://github.com/user-attachments/assets/63e01885-1bb6-4670-a554-8ca6d454ba71)![Screenshot 2025-06-06 005223](https://github.com/user-attachments/assets/12f15c5c-6cf9-410a-8cbe-155553be0c74)
 |  ![Screenshot 2025-06-06 005234](https://github.com/user-attachments/assets/fe9f4265-4c9c-42ea-81b9-2bb40aaee056)

---

## 🧩 How It Works

1. **ViLTProcessor** converts the image and question into tensors.
2. **ViLTForQuestionAnswering** runs inference and selects the most likely answer.
3. The answer is decoded and displayed using Streamlit.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Junaid0-glitch/Visual-question-Answering-Tool.git
cd Visual-question-Answering-Tool
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Hugging Face Token

Create a `.env` file and add your token:

```env
HUGGINGFACE_TOKEN=your_token_here
```

You can get a token from: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📦 Dependencies

- `streamlit`
- `transformers`
- `Pillow`
- `python-dotenv`
- `torch` (if not in requirements.txt, make sure to install)

---

## 🧠 Model Info

Using pretrained model from:
[`dandelin/vilt-b32-finetuned-vqa`](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa)

---

## 🛡️ Safety & Privacy

- Your Hugging Face token is **stored securely** in `.env` (not uploaded to GitHub).
- `.gitignore` excludes sensitive files like `.env` and `venv/`.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for more information.

---

## 🙌 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io/)
- [ViLT: Vision-and-Language Transformer](https://arxiv.org/abs/2102.03334)

---

## 💡 Future Improvements

- Support for multiple questions
- Gradio / Hugging Face Spaces deployment
- Multi-language support
- Mobile optimization

---

## 💬 Feedback

Got suggestions or want to collaborate? Open an issue or connect via GitHub!
