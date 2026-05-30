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

# ================== HARDCODED MASTER LESSON DATA MATRIX ==================
# Providing exhaustive, production examples directly in code for instant operational stability
CORE_BOOK_DATABASE = {
    "american_keyboard": {
        "1": {
            "key_name": "Escape (Esc)",
            "definition": "The Escape key allows a user to cancel, abort, or exit an ongoing operation, close open pop-up menus, or halt a loading program instantly.",
            "examples": [
                "Example 1: While browsing the web, if you accidentally click a link and a large, unwanted pop-up advertisement or modal window blocks your view, pressing the Esc key closes the modal instantly without forcing you to hunt for a tiny 'X' close button.",
                "Example 2: When watching media or presentations in full-screen view inside platforms like YouTube, Netflix, or PowerPoint, pressing the Esc key immediately shrinks the screen space back to your standard desktop window interface.",
                "Example 3: If a web browser tab gets stuck in an infinite loading loop or freezes because a server is unresponsive, tapping the Esc key forces the application to stop downloading the broken incoming network stream."
            ]
        },
        "2": {
            "key_name": "F1 (Function 1 Key)",
            "definition": "The F1 key is universally mapped across software ecosystems to launch the active application's official help desk, manual, or documentation directory.",
            "examples": [
                "Example 1: If you are working inside Microsoft Word or Excel and forget how to format a table cell, pressing the F1 key immediately brings up the Microsoft Help sidebar on the right side of your document screen.",
                "Example 2: When navigating files inside Windows File Explorer, pressing F1 opens your default web browser and automatically searches the Microsoft Support archive for general operating system tutorials.",
                "Example 3: Inside professional design tools like Adobe Photoshop, pressing F1 halts your work and launches an interactive web database containing tooltips and keyboard shortcut documentation for the application."
            ]
        }
    },
    "french_keyboard": {
        "1": {
            "key_name": "Échap (Echap)",
            "definition": "La touche Échap permet à un utilisateur d'annuler, d'interrompre ou de quitter une opération en cours, de fermer des menus contextuels ou d'arrêter un programme.",
            "examples": [
                "Example 1: Pendant la navigation sur le Web, si une fenêtre contextuelle ou une publicité intrusive s'affiche à l'écran, appuyer sur la touche Échap la ferme instantanément sans avoir à chercher le petit bouton de fermeture 'X'.",
                "Example 2: Lorsque vous regardez une vidéo ou une présentation en mode plein écran sur YouTube ou PowerPoint, appuyer sur Échap réduit immédiatement l'affichage pour revenir à l'interface standard du bureau.",
                "Example 3: Si un onglet de navigateur Web est bloqué dans une boucle de chargement infinie, appuyer sur la touche Échap force l'application à arrêter immédiatement le téléchargement des données réseau corrompues."
            ]
        },
        "2": {
            "key_name": "F1 (Touche de Fonction 1)",
            "definition": "La touche F1 est universellement configurée pour ouvrir instantanément le menu d'aide, le manuel d'utilisation ou l'assistance technique du logiciel actif.",
            "examples": [
                "Example 1: Si vous travaillez dans Microsoft Word et ne savez plus comment insérer un tableau, appuyer sur F1 ouvre automatiquement le volet d'assistance Microsoft à droite de votre document.",
                "Example 2: Lors de la navigation dans l'Explorateur de fichiers de Windows, appuyer sur F1 ouvre votre navigateur Web par défaut avec une recherche automatique d'aide pour le système d'exploitation.",
                "Example 3: Dans un logiciel complexe comme Adobe Photoshop, appuyer sur la touche F1 interrompt l'action actuelle et lance un guide interactif décrivant toutes les fonctionnalités de l'outil."
            ]
        }
    }
}

# Generate placeholder entries dynamically for lessons 3 through 20
for book_key in ["american_keyboard", "french_keyboard"]:
    is_fr = (book_key == "french_keyboard")
    for i in range(3, 21):
        CORE_BOOK_DATABASE[book_key][str(i)] = {
            "key_name": f"Key Placeholder #{i}" if not is_fr else f"Touche Clé #{i}",
            "definition": f"Educational definition string for advanced key layout index {i} under development." if not is_fr else f"Définition éducative pour la touche index {i} en cours de développement.",
            "examples": [
                f"Example 1: Execution scenario option A for key {i}." if not is_fr else f"Exemple 1: Scénario d'exécution option A pour la touche {i}.",
                f"Example 2: Spatial execution command behavior tracking context B." if not is_fr else f"Exemple 2: Comportement de la commande spatiale B.",
                f"Example 3: Interface deployment utility function case validation C." if not is_fr else f"Exemple 3: Validation de la fonction utilitaire C."
            ]
        }

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

# Pull content metrics from local runtime database dictionary container safely
lesson_data = CORE_BOOK_DATABASE[target_dir].get(lesson_index)

key_name = lesson_data["key_name"]
definition = lesson_data["definition"]
examples = lesson_data["examples"]

# Render High-Contrast Clean Layout Card
st.markdown(f"""
<div class='lesson-card'>
    <h2>Target Keyboard Key: <span class='key-badge'>{key_name}</span></h2>
    <p style='font-size:1.25rem; line-height:1.6; color:#1b0c3a; margin-top:15px;'><strong>Definition:</strong> {definition}</p>
</div>
""", unsafe_allow_html=True)

# Build text stream strictly intended for the TTS synthesis pipeline engine
speech_text = f"Key: {key_name}. Definition: {definition}. "

st.write("### 🔍 Application Practice Examples:")
for example in examples:
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
