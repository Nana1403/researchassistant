## 🔎 Research Assistant

## 📌 Overview

Research Assistant is an AI-powered web application that helps users explore and learn about any topic through natural conversations. Users can ask questions, receive AI-generated responses, and organize their findings using the built-in note-taking editor.

Whether you're researching for school, work, or personal projects, Research Assistant provides a simple workspace for gathering information and keeping everything in one place.

## 🎯 Features

- 💬 AI-Powered Research – Ask questions and receive intelligent responses from the AI assistant.
- 📝 Rich Text Note Editor – Take notes while researching with formatting options such as:
- Bold
- Italic
- Underline
- Strikethrough
- Lists and more
- 📄 Export Notes to PDF – Save your research notes as a PDF document.
- 🌐 Simple Web Interface – Clean and easy-to-use interface built with - Flask.
- ⚡ Real-Time Responses – Quickly get information on topics you're researching.
- 
---

## 🛠 Tech Stack
- Python – Core application logic
- Flask – Backend web framework
- OpenAI API – Powers the AI research assistant
- HTML/CSS/JavaScript – Frontend user interface
- WeasyPrint (or your PDF library) – PDF generation

---

## 🧠 How It Works
1. Enter a research question into the assistant.
2. The application sends the question to the OpenAI API.
3. The AI generates a response based on the user's query.
4. Users can save important information in the built-in note editor.
5. Notes can be formatted and exported as a PDF for future reference.

## 📸 Demo

<img src="static/images/demo.gif" width="600"/>

<p><em> Live Demo</em></p>

## Future Improvements
📚 RAG (Retrieval-Augmented Generation) support for uploaded PDFs
🔍 Internet search integration for up-to-date research
📂 Save and manage multiple research projects
🏷️ Note categorization and tagging
📑 Automatic citation generation
🎙️ Voice input support
🌙 Dark mode

## ⚙️ Installation
``` bash
git clone https://github.com/Nana1403/researchassistant.git
cd researchassistsnt
pip install -r requirements.txt
python main.py

## 📄 License
This project is licensed under the MIT License.
