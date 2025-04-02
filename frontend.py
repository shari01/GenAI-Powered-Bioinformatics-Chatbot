from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import requests

# ✅ Set page config (must be first Streamlit command)
st.set_page_config(page_title="GenAI Chatbot Agents", layout="centered", page_icon="🧬")

# ✅ Inject DNA background and custom CSS styling
st.markdown("""
<style>
/* DNA Helix Background */
body {
    background-image: url('https://www.genome.gov/sites/default/files/tg/en/illustration/DNA_helix_hero.jpg');
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
}

/* Style headings and layout */
h1, h2, h3 {
    color: #ffffff;
    text-align: center;
}

/* Widget hover and buttons */
textarea:hover, .stTextInput>div:hover {
    border: 2px solid #FF5733 !important;
    box-shadow: 0 0 10px rgba(255,87,51,0.6);
}

.stButton>button:hover {
    background-color: #FF5733 !important;
    color: white !important;
    transform: scale(1.05);
}

.stSelectbox:hover, .stRadio:hover {
    background-color: rgba(255, 255, 255, 0.07) !important;
}

/* Response Output */
.response-box {
    background-color: rgba(255, 255, 255, 0.92);
    padding: 20px;
    border-radius: 10px;
    color: #000000;
    font-size: 1rem;
    line-height: 1.5;
    margin-top: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# ✅ App title and intro
st.markdown("<h1>🧬 GenAI Chatbot Agents</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #e0e0e0;'>Interact with Smart AI Agents for Bio + Clinical Tasks</p>", unsafe_allow_html=True)
st.markdown("---")

# 🧠 Agent Behavior
st.subheader("🧠 Customize Agent Behavior")
system_prompt = st.text_area(
    "Define how your AI should behave",
    height=70,
    placeholder="e.g. Act as a helpful assistant for clinical bioinformatics"
)

# 🤖 Model Selection
st.subheader("🤖 Select LLM Model")
provider = st.radio("", ("Groq",), horizontal=True)

GROQ_MODELS = {
    "llama-3.3-70b-versatile": "🟣 llama-3.3-70b-versatile – Best for chat, summaries, coding",
    "llama3-70b-8192": "🔵 llama3-70b-8192 – Great for reasoning, research, and logic"
}

# 🧬 Select Groq model
groq_labels = list(GROQ_MODELS.values())
groq_keys = list(GROQ_MODELS.keys())
selected_label = st.selectbox("Choose Groq Model:", groq_labels)
selected_model = groq_keys[groq_labels.index(selected_label)]

# 🌐 Web Search Toggle
st.subheader("🌐 Enable Web Search")
allow_web_search = st.checkbox("Allow AI for web searches")

# 💬 User Input
st.subheader("💬 Enter Your Query")
user_query = st.text_area("Ask Your Question:", height=150, placeholder="Describe how to integrate phosphoproteomics and transcriptomics to assess MAPK pathway activation status....")

# 🔗 API Backend
API_URL = "http://127.0.0.1:9999/chat"

# 🛰️ Send to Backend
if st.button("🛰️ Ask Agent!"):
    if user_query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    st.subheader("✅ Agent Response")
                    st.markdown(f"<div class='response-box'>{response_data}</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ Error: {response.status_code} {response.text}")
        except Exception as e:
            st.error(f"⚠️ Connection error: {e}")
