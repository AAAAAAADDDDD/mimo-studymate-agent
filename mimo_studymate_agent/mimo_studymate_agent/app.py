import os
import streamlit as st
from dotenv import load_dotenv

from src.agents import StudyMateAgent
from src.storage import save_run_log, load_recent_logs

load_dotenv()

st.set_page_config(
    page_title="MiMo StudyMate Agent",
    page_icon="📚",
    layout="wide"
)

st.title("MiMo StudyMate Agent")
st.caption("AI-powered bilingual lecture notes, case analysis, quiz generation, and token tracking.")

with st.sidebar:
    st.header("Settings")
    model = st.text_input(
        "Model",
        value=os.getenv("MIMO_MODEL", "xiaomi_mimo/mimo-v2-flash")
    )

    task_type = st.selectbox(
        "Task Type",
        [
            "Bilingual Lecture Notes",
            "Case-to-Concept Mapping",
            "Assessment Writing Support",
            "Quiz Generator",
            "Full Study Pack"
        ]
    )

    output_language = st.selectbox(
        "Output Language",
        ["Chinese with English key terms", "English with Chinese support", "Bilingual"]
    )

    temperature = st.slider("Temperature", 0.0, 1.0, 0.3, 0.1)
    max_tokens = st.slider("Max Output Tokens", 512, 4096, 1800, 256)

st.subheader("Input Material")
input_text = st.text_area(
    "Paste lecture transcript, PPT OCR text, case material, or notes here:",
    height=280,
    placeholder="Example: Paste your lecture transcript or PPT text here..."
)

col1, col2 = st.columns([1, 1])
with col1:
    generate = st.button("Generate", type="primary", use_container_width=True)
with col2:
    show_logs = st.button("Show Recent Logs", use_container_width=True)

if generate:
    if not input_text.strip():
        st.warning("Please paste some input material first.")
    elif not os.getenv("XIAOMI_MIMO_API_KEY"):
        st.error("XIAOMI_MIMO_API_KEY is missing. Please set it in your environment or .env file.")
    else:
        agent = StudyMateAgent(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens
        )

        with st.spinner("Agent is reading, structuring, reasoning, and generating output..."):
            result = agent.run(
                task_type=task_type,
                input_text=input_text,
                output_language=output_language
            )

        st.subheader("Agent Output")
        st.markdown(result["content"])

        st.subheader("Run Metadata")
        st.json(result["metadata"])

        save_run_log(result)
        st.success("Run log saved locally.")

if show_logs:
    st.subheader("Recent Local Run Logs")
    logs = load_recent_logs(limit=5)
    if not logs:
        st.info("No logs yet.")
    else:
        for item in logs:
            with st.expander(f'{item["metadata"]["task_type"]} | {item["metadata"]["created_at"]}'):
                st.json(item["metadata"])
                preview = item["content"][:1200]
                if len(item["content"]) > 1200:
                    preview += "..."
                st.markdown(preview)
