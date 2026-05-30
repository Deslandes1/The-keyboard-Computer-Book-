import streamlit as st
import os
import asyncio
import edge_tts

# ================== BRAND NEW LIGHT PURPLE HIGH-CONTRAST THEME ==================
st.set_page_config(page_title="GlobalInternet Keyboard Academy", page_icon="⌨️", layout="wide")

st.markdown("""
    <style>
    /* Main Page Styling - Light Purple and High Contrast Deep Purple Text */
    .stApp { 
        background-color: #f3ebff; 
        color: #1b0c3a; 
    }
    
    /* Sidebar Area - Dark Royal Slate for structural separation */
    [data-testid="stSidebar"] { 
        background-color: #1a0f30 !important; 
        border-right: 3px solid #6b3ba7; 
    }
    
    /* Sidebar text colors */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
        color: #e6daff !important;
    }
    
    /* Elegant Gradient Main Header */
    .main-header {
        font-size: 2.8rem !important;
        font-weight: 800;
        background: linear-gradient(45deg, #6b3ba7, #8a2be2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    
    /* Title Credit Text styling */
    .built-by-credit {
        font-size: 1.2rem;
        font-weight: 600;
        color: #4a2380;
        margin-bottom: 1.5rem;
        font-style: italic;
    }
    
    /* Lesson Card Box */
    .lesson-card { 
        background-color: #ffffff; 
        border: 2px solid #b392e6; 
        padding: 25px; 
        border-radius: 12px; 
        margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(107, 59, 167, 0.05);
    }
    
    .lesson-card h2 {
        color: #31145a !important;
    }
    
    /* Practice Example Boxes */
    .example-box { 
        background-color: #fdfbff; 
        border-left: 5px solid #8a2be2; 
        padding: 15px; 
        border-radius: 6px; 
        margin-top: 12px;
        color: #220b45 !important;
        font-size: 1.1rem;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.02);
    }
    
    /* Visual Keyboard Key Badge */
    .key-badge { 
        background-color: #8a2be2; 
        color: white !important; 
        padding: 5px 14px; 
        border-radius: 6px; 
        font-family: monospace; 
        font-size: 1.4rem; 
        box-shadow: 0px 2px 4px rgba(0,0,0,0.15);
    }
    
    /* High Contrast Text overrides for markdown strings */
    h3 {
        color: #31145a !important;
    }
    
    /* Sidebar Link Button styling */
    .sidebar-link {
        display: inline-block;
        background-color: #6b3ba7;
        color: white !important;
        padding: 8px 15px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        margin-top: 5px;
        margin-bottom: 10px;
        width: 100%;
    }
    .sidebar-link:hover {
        background-color: #8a2be2;
    }
    </style>
""", unsafe_allow_html=True)

# ================== ASYNCHRONOUS TTS CORE ==================
async def generate_voiceover(text_to_speak, output_audio_path, voice_name):
    communicate = edge_tts.Communicate(text_to_speak, voice_name)
    await communicate.save(output_audio_path)

def run_tts(text, file_path, voice):
    asyncio.run(generate_voiceover(text, file_path, voice))

# ================== DATA DIRECTORY SAFEGUARD ==================
for folder in ["american_keyboard", "french_keyboard"]:
    if not os.path.exists(folder):
        os.makedirs(folder)
        sample_text = "Key: Escape (Esc)\nDefinition: The Escape key allows a user to cancel or abort an ongoing operation.\n---\nExample 1: Close a pop-up window.\n---\nExample 2: Exit full screen view.\n---\nExample 3: Stop a web page from loading."
        with open(f"{folder}/lesson1.txt", "w", encoding="utf-8") as f:
            f.write(sample_text)

# ================== SIDEBAR NAVIGATION & COMPANY METADATA ==================
with st.sidebar:
    # Company Name Header
    st.markdown('<div style="font-size:1.6rem; font-weight:800; color:#dfa2ff; letter-spacing:0.5px;">🌐 Globalinternet.py</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.9rem; color:#b392e6; margin-bottom:10px;">Advanced Software Architecture</div>', unsafe_allow_html=True)
    
    # Official Website Link Button
    st.markdown('<a href="https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/" target="_blank" class="sidebar-link">🔗 Visit Our Website</a>', unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color: #4a2380;'>", unsafe_allow_html=True)
    
    # Navigation Matrix
    chapter = st.radio(
        "📚 Select Keyboard Chapter / Chapitre:",
        ["🇺🇸 American Keyboard Lessons", "🇫🇷 French Keyboard Lessons"]
    )
    
    if "American" in chapter:
        target_dir = "american_keyboard"
        voice_profile = "en-US-GuyNeural"
    else:
        target_dir = "french_keyboard"
        voice_profile = "fr-FR-HenriNeural"
        
    st.markdown("<hr style='border-color: #4a2380;'>", unsafe_allow_html=True)
    
    lesson_numbers = [f"Lesson {i}" for i in range(1, 21)]
    selected_lesson_str = st.selectbox("📖 Select Lesson / Choisir une leçon:", lesson_numbers)
    lesson_index = selected_lesson_str.split(" ")[1]
    
    st.markdown("<hr style='border-color: #4a2380;'>", unsafe_allow_html=True)
    
    # Infrastructure Core Support Contacts
    st.markdown('<div style="font-size:1.1rem; font-weight:700; color:#dfa2ff; margin-bottom:5px;">🛠️ Support Infrastructure:</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.9rem; color:#e6daff; line-height:1.5;">
        <strong>Phone:</strong> (509)-47385663<br>
        <strong>Email:</strong> deslandes78@gmail.com
    </div>
    """, unsafe_allow_html=True)

# ================== MAIN APP WORKSPACE CONTENT ==================
st.markdown('<div class="main-header">Interactive Software Keyboard Book</div>', unsafe_allow_html=True)
st.markdown('<div class="built-by-credit">Built by Gesner Deslandes</div>', unsafe_allow_html=True)

st.write(f"### `{chapter}` — **{selected_lesson_str}**")

file_target_path = f"{target_dir}/lesson{lesson_index}.txt"

if os.path.exists(file_target_path):
    # Safe open patch to fix encoding ValueErrors across differing operating systems
    with open(file_target_path, "r", encoding="utf-8", errors="ignore") as file:
        raw_content = file.read()
        
    try:
        parts = raw_content.split("---")
        header_lines = parts[0].strip().split("\n")
        
        key_name = header_lines[0].replace("Key:", "").strip()
        definition = header_lines[1].replace("Definition:", "").strip()
        
        examples = [ex.strip() for ex in parts[1:] if ex.strip()]
    except Exception as parse_err:
        st.error("Text file parsing issue detected. Please check that your fields match formatting rules separated by triple dashes (---).")
        st.stop()

    # Render High-Contrast Clean Layout
    st.markdown(f"""
    <div class='lesson-card'>
        <h2>Target Keyboard Key: <span class='key-badge'>{key_name}</span></h2>
        <p style='font-size:1.25rem; line-height:1.6; color:#1b0c3a; margin-top:15px;'><strong>Definition:</strong> {definition}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Build complete text stream for text-to-speech engine
    speech_text = f"Key: {key_name}. Definition: {definition}. "
    
    st.write("### 🔍 Application Practice Examples:")
    for idx, example in enumerate(examples):
        st.markdown(f"<div class='example-box'><strong>{example}</strong></div>", unsafe_allow_html=True)
        speech_text += f" {example}. "

    st.markdown("<br><hr style='border-color: #b392e6;'>", unsafe_allow_html=True)
    
    # Asynchronous Dynamic Audio Voiceover Engine
    st.write("### 🔊 Audio Reading Assistant:")
    audio_filename = f"audio_{target_dir}_lesson_{lesson_index}.mp3"
    
    with st.spinner("Generating High-Fidelity Neural Voiceover Track..."):
        try:
            run_tts(speech_text, audio_filename, voice_profile)
            if os.path.exists(audio_filename):
                st.audio(audio_filename, format="audio/mp3")
        except Exception as tts_err:
            st.error(f"Audio Engine connection alert: {tts_err}")

else:
    st.info(f"💾 File not found yet! Please make sure a text file named `lesson{lesson_index}.txt` exists in your `{target_dir}` directory.")

# ================== SYSTEM PRODUCTION FOOTER ==================
st.markdown("<br><hr style='border-color: #b392e6;'>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; font-size: 0.85rem; color:#53387a; font-weight:600;">
        🚀 KEYBOARD COMPUTER SOFTWARE BOOK | Built & Maintained by GlobalInternet.py<br>
        Engineer-in-Chief: Gesner Deslandes | Contact: (509)-47385663
    </div>
    """,
    unsafe_allow_html=True
)
