# GenAI-Powered-Bioinformatics-Chatbot
A full-stack LLM-powered chatbot designed for bioscience and clinical research queries — from pathway analysis to molecular Q&amp;A.

<h1 align="center">🧬 GenAI-Powered Bioinformatics Chatbot</h1>
<p align="center"><b>Built with Groq · LangGraph · FastAPI · Streamlit</b></p>

<p align="center">
  A full-stack GenAI chatbot designed for real-time bioscience and clinical research queries.<br>
  Powered by Groq-hosted LLaMA models with agent-based logic and biological use-case support.
</p>

<hr>

<h2>🚀 Tech Stack</h2>

<table>
  <tr>
    <th>Layer</th>
    <th>Tools Used</th>
  </tr>
  <tr>
    <td><b>LLMs</b></td>
    <td>Groq-hosted LLaMA 3 models (70B)</td>
  </tr>
  <tr>
    <td><b>Agent Framework</b></td>
    <td>LangChain + LangGraph</td>
  </tr>
  <tr>
    <td><b>Backend</b></td>
    <td>FastAPI + Pydantic</td>
  </tr>
  <tr>
    <td><b>Search Integration</b></td>
    <td>Tavily (Optional web search)</td>
  </tr>
  <tr>
    <td><b>Frontend</b></td>
    <td>Streamlit + Custom UI + DNA-themed design</td>
  </tr>
</table>

<hr>

<h2>✨ Key Features</h2>

<ul>
  <li><b>🧠 Custom system prompt:</b> Define agent behavior for each session</li>
  <li><b>⚡ LLM selection:</b> Use Groq’s ultra-fast LLaMA models</li>
  <li><b>🔍 Web search option:</b> Enable real-time info lookup via Tavily</li>
  <li><b>🎨 Themed UI:</b> Stylish DNA-background UI built with Streamlit</li>
  <li><b>🔌 FastAPI backend:</b> Flexible API with model routing & validation</li>
</ul>

<hr>

<h2>🧬 Upcoming Features</h2>

<ul>
  <li><b>Biological Pathway Enrichment Analysis</b></li>
  <li>Users can submit gene lists and receive enriched GO/KEGG/Reactome pathways</li>
  <li>Planned libraries: <code>gseapy</code>, <code>Enrichr API</code>, <code>BioServices</code></li>
</ul>

<hr>

<h2>💻 How to Run Locally</h2>

<pre>
# Clone the repository
git clone https://github.com/shari01/GenAI-Powered-Bioinformatics-Chatbot.git
cd GenAI-Powered-Bioinformatics-Chatbot

# Install dependencies
pip install -r requirements.txt

# Start backend
python backend.py

# Start frontend
streamlit run frontend.py
</pre>

<hr>

<h2>🔬 Use Cases</h2>

<ul>
  <li>Ask for biological pathway mechanisms (e.g. MAPK, JAK/STAT)</li>
  <li>Query gene-disease associations</li>
  <li>Explain transcriptomics or proteomics workflows</li>
  <li>Assist in hypothesis generation or experimental design</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
  <b>Sheryar Malik</b><br>
  MPhil Bioinformatics | Remote Bioinformatics Developer<br>
  <i>Building AI-first tools for translational bioinformatics</i>
</p>

<h3 align="center">⭐ Star this repo · Clone · Explore · Suggest Features</h3>
