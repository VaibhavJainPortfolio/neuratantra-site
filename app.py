import streamlit as st

# Page Configuration
st.set_page_config(page_title="Neuratantra AI", layout="wide", page_icon="🧠")

# --- Custom CSS ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            background-color: #0a0e17;
            color: #ffffff;
        }
        .stButton>button {
            background-color: #ffad46;
            color: black;
            border-radius: 10px;
            padding: 0.6em 1.4em;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #ffd480;
            box-shadow: 0 0 10px #ffd480;
        }
        .section {
            padding: 2rem 1rem;
        }
        .title {
            font-size: 48px;
            font-weight: 600;
            color: #ffffff;
        }
        .subtitle {
            font-size: 24px;
            font-weight: 300;
            color: #ccc;
        }
    </style>
""", unsafe_allow_html=True)

# --- Logo and Hero Section ---
st.image("neuratantra_logo.png", width=260)
st.markdown("<div class='title'>Neuratantra</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Building the Fabric of Future Intelligence.</div>", unsafe_allow_html=True)

# --- Navigation Sidebar ---
menu = st.sidebar.radio("🌐 Navigate", ["Home", "About", "Solutions", "Research", "Careers", "Contact"])

# --- Page Sections ---
if menu == "Home":
    st.markdown("### 🔮 Vision")
    st.write("To weave autonomous, conscious intelligence through the orchestration of neural and cosmic systems.")

    st.markdown("### 🚀 What We Do")
    st.write("""
    - Agentic AI Systems — Autonomous agents that learn and evolve
    - Workflow Orchestration Platforms
    - Quantum-inspired Decision Engines
    - Conscious Intelligence Frameworks
    """)

    st.markdown("### 🎯 Why Neuratantra?")
    st.write("""
    - Rooted in Sacred Systems (Tantra) + Neural Networks
    - Agentic AI aligned with Conscious Evolution
    - Quantum Intelligence + Deep AI
    """)

elif menu == "About":
    st.markdown("### 🧠 About Neuratantra")
    st.write("Neuratantra is building the conscious infrastructure of tomorrow — where intelligence is not just artificial, but orchestrated, autonomous, and aware. We are the fusion of cognitive neuroscience, quantum agency, and sacred systems design.")

elif menu == "Solutions":
    st.markdown("### 🔧 Our Solutions")
    st.write("""
    - Cognitive Workflow Automation
    - Intelligent Knowledge Agents
    - Quantum-Aware Decision Systems
    - AgentOS for Enterprise Operations
    - AI-based Autonomous Orchestration Networks
    """)

elif menu == "Research":
    st.markdown("### 📚 Research & Innovation")
    st.write("We explore the intersection of Agentic AI, Tantra Systems Thinking, and Quantum Cognition.")
    st.write("Coming soon: Whitepapers, Open Source Frameworks, and Vision Papers.")

elif menu == "Careers":
    st.markdown("### 🚀 Careers @ Neuratantra")
    st.write("We're not hiring yet — but if you're a believer in conscious intelligence and Agentic AI, drop us a line:")
    st.code("📧 talent@neuratantra.ai")

elif menu == "Contact":
    st.markdown("### 📞 Contact Us")
    st.write("""
    - 📧 Email: hello@neuratantra.ai
    - 🌐 Website: www.neuratantra.ai
    - 🔗 LinkedIn: /company/neuratantra
    - 🐦 Twitter: @neuratantra.ai
    """)

    st.markdown("---")
    st.markdown("### 🧘‍♂️ Founder's Note")
    st.write("> "We are not just building artificial minds. We are reviving consciousness into the digital fabric of reality."")

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 Neuratantra AI (OPC) Pvt Ltd")
