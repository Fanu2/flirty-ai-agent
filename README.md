# ❤️ Flirty AI Agent

A simple AI-powered web application that generates charming, romantic, and flirty messages using the **Mistral AI API**.

Built with **Python** and **Streamlit**, the application allows users to enter a prompt and generate a personalized romantic message. Generated messages can also be copied to the clipboard and downloaded as a text file.

---

## ✨ Features

- ❤️ Generate romantic and flirty AI messages
- 🤖 Powered by the Mistral AI API
- 🧠 Uses the Mistral Agents and Conversations API
- 🔄 Automatic fallback model support
- 📝 Custom prompt input
- ⏳ Generation progress indicator
- 📋 Copy generated messages to the clipboard
- 💾 Download messages as `.txt` files
- 🌐 Simple Streamlit web interface

---

## 🤖 AI Models

The application first attempts to create an agent using:

```text
mistral-large
```

If that fails, it automatically falls back to:

```text
mistral-medium-latest
```

The agent is configured to generate charming and romantic text.

---

## 📁 Project Structure

A typical project structure is:

```text
flirty-ai-agent/
├── app.py
├── utils.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### Main Files

- `app.py` — Main Streamlit application
- `utils.py` — Utility functions for clipboard copying and file downloads
- `.env` — Stores the Mistral API key locally
- `requirements.txt` — Python dependencies

---

## ⚙️ Requirements

The application requires:

- Python 3
- Streamlit
- Mistral AI Python SDK
- python-dotenv

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🔑 Mistral API Key Setup

The application requires a Mistral API key.

Create a `.env` file in the project directory:

```text
MISTRAL_API_KEY=your_api_key_here
```

The application loads the key using:

```python
load_dotenv()
```

> **Important:** Never commit your `.env` file or API key to GitHub.

Add this to `.gitignore`:

```text
.env
```

---

## 🚀 Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

Streamlit will start a local web server and open the application in your browser.

---

## 📝 How to Use

1. Start the application.
2. Enter a prompt describing the message you want.
3. Click **Generate Message**.
4. Wait while the AI generates a response.
5. Copy the generated message to the clipboard.
6. Download the message as a text file if desired.

Example prompt:

```text
Write a charming and romantic message to woo someone special.
```

---

## 🧠 How It Works

The application:

1. Loads the Mistral API key from the `.env` file.
2. Creates a Mistral AI client.
3. Creates a Flirty Text Agent.
4. Uses `mistral-large` as the primary model.
5. Falls back to `mistral-medium-latest` if necessary.
6. Sends the user's prompt through a Mistral conversation.
7. Extracts the generated text from the response.
8. Displays the message in the Streamlit interface.
9. Provides options to copy or download the generated message.

---

## 🔧 Agent Configuration

The AI agent is configured with instructions similar to:

```text
Generate charming romantic texts.
```

Generation settings include:

```text
Temperature: 0.7
Top P: 0.95
```

These settings help produce creative and varied responses.

---

## 📦 Example `requirements.txt`

```text
streamlit
mistralai
python-dotenv
```

Additional dependencies may be required depending on how `utils.py` implements clipboard functionality.

---

## 🛡️ Security

Keep your API key private.

Your `.gitignore` should include:

```text
.env
__pycache__/
*.pyc
.venv/
venv/
```

Never upload your Mistral API key to a public repository.

---

## 🚧 Development Status

This project is a simple experimental AI message generator built around:

- Streamlit
- Mistral AI
- AI Agents
- AI Conversations

Possible future improvements include:

- Different message styles
- Tone selection
- Message history
- Multiple AI provider support
- Local Ollama model support
- Model selection
- Dark mode
- Saved conversations
- Improved prompt templates

---

## 👤 Author

Jasvir Singh Sidhu

GitHub: Fanu2

---

## 📄 License

This project is intended for personal, educational, and experimental use.

---

# ❤️ Flirty AI Agent

*Generate charming messages. Add your personal touch.*
