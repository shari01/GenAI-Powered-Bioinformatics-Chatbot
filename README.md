# GenAI-Powered-Bioinformatics-Chatbot
A full-stack LLM-powered chatbot designed for bioscience and clinical research queries — from pathway analysis to molecular Q&amp;A.


<h1 align="center">🧬 GenAI Bio-Clinical Chatbot</h1>
<p align="center"><b>Powered by Groq · LangChain · FastAPI · Streamlit</b></p>

<p align="center">
  A full-stack chatbot built to support bioscience and clinical research workflows.<br>
  Ask complex biological questions, search across the web, and soon, run pathway enrichment!
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
    <td>Groq-hosted LLaMA 3 models (70B, 8B)</td>
  </tr>
  <tr>
    <td><b>AI Agent</b></td>
    <td>LangChain + LangGraph</td>
  </tr>
  <tr>
    <td><b>Backend API</b></td>
    <td>FastAPI + Pydantic</td>
  </tr>
  <tr>
    <td><b>Search Tool</b></td>
    <td>Tavily Search API (optional real-time web lookup)</td>
  </tr>
  <tr>
    <td><b>Frontend UI</b></td>
    <td>Streamlit with custom CSS and DNA-themed design</td>
  </tr>
</table>

<hr>

<h2>🎯 Key Features</h2>

<ul>
  <li>📌 Streamlit interface with dynamic LLM selection</li>
  <li>🧠 System prompt customization to guide AI behavior</li>
  <li>🌐 Optional web search toggle using Tavily</li>
  <li>⚡ Backend logic using LangGraph-based reactive agent</li>
  <li>🎨 Beautiful DNA-themed styling for a research-focused UI</li>
</ul>

<hr>

<h2>🧪 Upcoming Features</h2>

<ul>
  <li>🧬 Biological pathway enrichment analysis</li>
  <li>Input gene lists and return GO, KEGG, or Reactome pathways</li>
  <li>Planned tools: <code>GSEApy</code>, <code>Enrichr API</code>, and <code>BioServices</code></li>
</ul>

<hr>

<h2>💻 Getting Started</h2>

<pre>
# Clone the repository
git clone https://github.com/your-username/genai-bio-chatbot.git
cd genai-bio-chatbot

# Install dependencies
pip install -r requirements.txt

# Run backend
python backend.py

# Run frontend
streamlit run frontend.py
</pre>

<hr>

<h2>🔬 Use Case Examples</h2>

<ul>
  <li>Ask for MAPK or JAK/STAT pathway mechanisms</li>
  <li>Get gene-disease associations</li>
  <li>Explain omics integration (e.g., phosphoproteomics + transcriptomics)</li>
  <li>Clinical biomarker Q&A and exploratory bioinformatics reasoning</li>
</ul>

<hr>

<h2>👤 Author</h2>

<p>
  <b>Sheryar Malik</b><br>
  MPhil Bioinformatics | Remote Bioinformatics Developer<br>
  <i>Focused on AI x Biomedical Data</i>
</p>

---

<h3 align="center">⭐ Star this repo if you like it · Contributions Welcome!</h3>
