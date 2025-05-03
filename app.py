
import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Neuratantra AI", layout="wide", page_icon="🧠")

# --- Apply Custom Style ---
st.markdown("""
    <style>
        body {
            background-color: #0a0e17;
            color: #ffffff;
        }
        .main {
            background-color: #0a0e17;
        }
        header, footer, .css-1rs6os.edgvbvh3 { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# --- Logo ---
st.image("neuratantra_logo.png", width=250)

# --- Headline ---
st.markdown("<h1 style='color: white; font-size: 48px;'>Neuratantra</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #ccc;'>Building the Fabric of Future Intelligence</h3>", unsafe_allow_html=True)

# --- Menus ---
menu = st.sidebar.selectbox("Navigate", ["Home", "About", "Solutions", "Research", "Careers", "Contact"])

if menu == "Home":
    st.markdown("---")
    st.header("🔮 Vision")
    st.write("To weave autonomous, conscious intelligence through the orchestration of neural and cosmic systems.")

    st.header("🚀 What We Do")
    st.write("""
    - Agentic AI Systems — Autonomous agents that learn and evolve
    - Workflow Orchestration Platforms
    - Quantum-inspired Decision Engines
    - Conscious Intelligence Frameworks
    """)

    st.header("🎯 Why Neuratantra?")
    st.write("""
    - Rooted in Sacred Systems (Tantra) + Neural Networks
    - Agentic AI aligned with Conscious Evolution
    - Quantum Intelligence + Deep AI
    """)

elif menu == "About":
    st.header("🧠 About Neuratantra")
    st.write("Neuratantra is building the conscious infrastructure of tomorrow — where intelligence is not just artificial, but orchestrated, autonomous, and aware.")

elif menu == "Solutions":
    st.header("🔧 Our Solutions")
    st.write("""
    - Cognitive Workflow Automation
    - Intelligent Knowledge Agents
    - Quantum-Aware Decision Systems
    - AgentOS for Enterprise Operations
    """)

elif menu == "Research":
    st.header("📚 Research & Innovation")
    st.write("We explore the intersection of Agentic AI, Tantra Systems Thinking, and Quantum Cognition. Coming soon: Whitepapers, Tools, and Frameworks.")

elif menu == "Careers":
    st.header("🚀 Careers @ Neuratantra")
    st.write("We're not hiring yet — but if you're a believer in conscious intelligence and Agentic AI, email us: talent@neuratantra.ai")

elif menu == "Contact":
    st.header("📞 Contact Us")
    st.write("""
    - 📧 Email: hello@neuratantra.ai
    - 🌐 Website: www.neuratantra.ai
    - 🔗 LinkedIn: /company/neuratantra
    - 🐦 Twitter: @neuratantra.ai
    """)
