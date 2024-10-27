# Level 1: Installing and Running a Chat Interface with an LLM
---
## Steps
1. Install [Ollama](https://ollama.com/download) ([Video](https://www.youtube.com/shorts/XGlK4bBAzcg))
2. Install/run llama3.2: ```ollama run llama3.2```
3. Done, you should have a simple chat interface on your terminal. (type ```/bye``` to exit)
---
## Steps for creating a web interface
1. Install streamlit: ```pip install streamlit```
2. Create a ```.py``` file with the code from ```web_ui.py```
3. Run ```ollama serve``` in your terminal.
4. Finally run ```streamlit run <your file name>``` in your terminal.
5. This will open a tab on your web browser with the "Chat Bot"
---
## Technical difficulties
Make sure to check the path that was specified in ```.py``` file (line 19 in the provided file), if your getting an error stating ```Error: 404 ...```

---