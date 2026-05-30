import streamlit as st
import os
import asyncio
import edge_tts

# ================== DESIGN & LAYOUT THEME ==================
st.set_page_config(page_title="GlobalInternet Keyboard Academy", page_icon="⌨️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b071a; color: #e2d9f3; }
    [data-testid="stSidebar"] { background-color: #130c26 !important; border-right: 2px solid #3a1f5d; }
    .main-header {
        font-size: 2.8rem !important;
        font-weight: 800;
        background: linear-gradient(45deg, #dfa2ff, #8a2be2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .lesson-card { background-color: #160f2e; border: 2px solid #3a1f5d; padding: 25px; border-radius: 12px; margin-bottom: 20px; }
    .example-box { background-color: #1f143d; border-left: 4px solid #bf80ff; padding: 15px; border-radius: 4px; margin-top: 10px; }
    .key-badge { background-color: #8a2be2; color: white; padding: 4px 12px; border-radius: 6px; font-family: monospace; font-size: 1.3rem; }
    </style>
""", unsafe_allow_html=True)

# ================== ASYNCHRONOUS TTS CORE ==================
async def generate_voiceover(text_to_speak, output_audio_path, voice_name):
    """Generates a high-quality neural voiceover dynamically."""
    communicate = edge_tts.Communicate(text_to_speak, voice_name)
    await communicate.save(output_audio_path)

def run_tts(text, file_path, voice):
    asyncio.run(generate_voiceover(text, file_path, voice))

# ================== DATA DIRECTORY SAFEGUARD ==================
# Create dummy demonstration files if directories are empty at initialization
for folder in ["american_keyboard", "french_keyboard"]:
    if not os.path.exists(folder):
        os.makedirs(folder)
        # Seed Lesson 1 for fallback demonstration purposes
        sample_text = "Key: Escape (Esc)\nDefinition: Test key definition details.\n---\nExample 1: Detail 1\n---\nExample 2: Detail 2\n---\nExample 3: Detail 3"
        with open(f"{folder}/lesson1.txt", "w", encoding="utf-8") as f:
            f.write(sample_text)

# ================== SIDEBAR NAVIGATION MATRIX ==================
with st.sidebar:
    st.markdown('<div style="font-size:1.5rem; font-weight:bold; color:#bf80ff;">⌨️ Keyboard Academy</div>', unsafe_allow_html=True)
    st.write("GlobalInternet.py Core Software Book")
    st.markdown("<hr style='border-color: #3a1f5d;'>", unsafe_allow_html=True)
    
    # 1. Select the Chapter / Keyboard Type
    chapter = st.radio(
        "📚 Select Keyboard Chapter:",
        ["🇺🇸 American Keyboard Lessons", "🇫🇷 French Keyboard Lessons"]
    )
    
    # Map selection to directory and set correct language profile voices
    if "American" in chapter:
        target_dir = "american_keyboard"
        voice_profile = "en-US-GuyNeural"
        lang_code = "English"
    else:
        target_dir = "french_keyboard"
        voice_profile = "fr-FR-HenriNeural"
        lang_code = "French"
        
    st.markdown("<hr style='border-color: #3a1f5d;'>", unsafe_allow_html=True)
    
    # 2. Select Lesson Number (1 to 20)
    lesson_numbers = [f"Lesson {i}" for i in range(1, 21)]
    selected_lesson_str = st.selectbox("📖 Select Lesson:", lesson_numbers)
    lesson_index = selected_lesson_str.split(" ")[1]
    
# ================== MAIN CONTENT ENGINE ==================
st.markdown('<div class="main-header">Interactive Software Keyboard Book</div>', unsafe_allow_html=True)
st.write(f"### Chapter: {chapter} | `{selected_lesson_str}`")

file_target_path = f"{target_dir}/lesson{lesson_index}.txt"

if os.path.exists(file_target_path):
    # Read and parse text file data blocks safely
    with open(file_target_path, "utf-8") as file:
        raw_content = file.read()
        
    try:
        # Split using our triple dash marker
        parts = raw_content.split("---")
        header_lines = parts[0].strip().split("\n")
        
        key_name = header_lines[0].replace("Key:", "").strip()
        definition = header_lines[1].replace("Definition:", "").strip()
        
        examples = [ex.strip() for ex in parts[1:] if ex.strip()]
    except Exception as parse_err:
        st.error("Text structure parsing anomaly detected. Verify triple dash separation rules.")
        st.stop()

    # --- UI DISPLAY CONSTRUCTION ---
    st.markdown(f"<div class='lesson-card'><h2>Target Key: <span class='key-badge'>{key_name}</span></h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:1.15rem; line-height:1.6;'>{definition}</p></div>", unsafe_allow_html=True)
    
    # Assemble complete speech text parameters
    speech_text = f"Key: {key_name}. Definition: {definition}. "
    
    st.write("### 🔍 Application Practice Examples:")
    for idx, example in enumerate(examples):
        st.markdown(f"<div class='example-box'><strong>{example}</strong></div>", unsafe_allow_html=True)
        speech_text += f" {example}. "

    st.markdown("<hr style='border-color: #3a1f5d;'>", unsafe_allow_html=True)
    
    # --- AUDIO SYNTHESIS PIPELINE CONTROL ---
    st.write("### 🔊 Audio Reading Assistant:")
    audio_filename = f"audio_{target_dir}_lesson_{lesson_index}.mp3"
    
    with st.spinner("Generating Neural Voiceover Stream..."):
        try:
            run_tts(speech_text, audio_filename, voice_profile)
            if os.path.exists(audio_filename):
                st.audio(audio_filename, format="audio/mp3")
        except Exception as tts_err:
            st.error(f"Audio Engine pipeline timeout: {tts_err}")

else:
    st.info(f"💾 File configuration placeholder needed! Create file path `{file_target_path}` inside your repository to automatically load its lessons.")

# ================== CORPORATE FOOTER ==================
st.markdown("<br><hr style='border-color: #3a1f5d;'>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; font-size: 0.85rem; color:#aaa2bc;">
        🚀 <strong>KEYBOARD CORE SOFTWARE BOOK v1.0</strong> | Developed by <strong>GlobalInternet.py</strong><br>
        Architect-in-Chief: <strong>Gesner Deslandes</strong> | Support Desk Contact: <strong>(509)-47385663</strong>
    </div>
    """,
    unsafe_allow_html=True
)
