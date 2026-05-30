import streamlit as st
import os
import asyncio
import edge_tts

# ================== LIGHT PURPLE HIGH-CONTRAST THEME ==================
st.set_page_config(page_title="GlobalInternet Keyboard Academy", page_icon="⌨️", layout="wide")

st.markdown("""
    <style>
    /* Main Page Styling */
    .stApp { 
        background-color: #f3ebff; 
        color: #1b0c3a; 
    }
    
    /* Sidebar Area */
    [data-testid="stSidebar"] { 
        background-color: #1a0f30 !important; 
        border-right: 3px solid #6b3ba7; 
    }
    
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
    
    /* CSS Scientific Keyboard Matrix Grid */
    .keyboard-matrix {
        background-color: #22143b;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #6b3ba7;
        margin-bottom: 20px;
    }
    .keyboard-row {
        display: flex;
        justify-content: space-between;
        margin-bottom: 8px;
    }
    .f-key {
        background-color: #3a1d6e;
        color: #dfa2ff !important;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        font-family: monospace;
        flex: 1;
        text-align: center;
        margin: 0 4px;
        border-bottom: 3px solid #1a0f30;
        font-size: 0.9rem;
    }
    .f-key.active {
        background-color: #8a2be2;
        color: white !important;
        border-bottom: 3px solid #4a2380;
        box-shadow: 0 0 10px #dfa2ff;
    }
    
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

# ================== GLOBAL 5-LANGUAGE UI TRANSLATIONS ==================
UI_TRANSLATIONS = {
    "English": {
        "title": "Interactive Software Keyboard Book", "sub_title": "Advanced Software Architecture", "btn_website": "🔗 Visit Our Website",
        "nav_chapter": "📚 Select Keyboard Chapter:", "nav_lesson": "📖 Select Lesson:", "nav_lang": "🌐 Choose Book Language:",
        "support_title": "🛠️ Support Infrastructure:", "practice_title": "🔍 Application Practice Examples:", "audio_title": "🔊 Audio Reading Assistant:",
        "spinner_msg": "Generating High-Fidelity Neural Voiceover Track...", "target_key": "Target Keyboard Key:", "lesson_prefix": "Lesson"
    },
    "Français": {
        "title": "Livre Électronique Interactif du Clavier", "sub_title": "Architecture Logicielle Avancée", "btn_website": "🔗 Visitez Notre Site Web",
        "nav_chapter": "📚 Sélectionner le Chapitre du Clavier:", "nav_lesson": "📖 Sélectionner la Leçon:", "nav_lang": "🌐 Choisir la Langue du Livre:",
        "support_title": "🛠️ Infrastructure de Support:", "practice_title": "🔍 Exemples Pratiques d'Application:", "audio_title": "🔊 Assistant de Lecture Audio:",
        "spinner_msg": "Génération de la piste de voix off neuronale...", "target_key": "Touche Clavier Ciblée:", "lesson_prefix": "Leçon"
    },
    "Español": {
        "title": "Libro Electrónico Interactivo del Teclado", "sub_title": "Arquitectura de Software Avanzada", "btn_website": "🔗 Visite Nuestro Sitio Web",
        "nav_chapter": "📚 Seleccionar Capítulo del Teclado:", "nav_lesson": "📖 Seleccionar Lección:", "nav_lang": "🌐 Elegir Idioma del Libro:",
        "support_title": "🛠️ Infraestructura de Soporte:", "practice_title": "🔍 Ejemplos Prácticos de Aplicación:", "audio_title": "🔊 Asistente de Lectura de Audio:",
        "spinner_msg": "Generando pista de voz de alta fidelidad...", "target_key": "Tecla del Teclado Navegada:", "lesson_prefix": "Lección"
    },
    "Português": {
        "title": "Livro Interativo de Software de Teclado", "sub_title": "Arquitetura Avançada de Software", "btn_website": "🔗 Visite o Nosso Site",
        "nav_chapter": "📚 Selecionar Capítulo do Teclado:", "nav_lesson": "📖 Selecionar Lição:", "nav_lang": "🌐 Escolha o Idioma do Livro:",
        "support_title": "🛠️ Infraestrutura de Suporte:", "practice_title": "🔍 Exemplos Práticos de Aplicação:", "audio_title": "🔊 Assistente de Leitura de Áudio:",
        "spinner_msg": "Gerando faixa de áudio neural de alta fidelidade...", "target_key": "Tecla de Teclado Alvo:", "lesson_prefix": "Lição"
    },
    "中文": {
        "title": "交互式键盘软件电子书", "sub_title": "高级软件架构设计", "btn_website": "🔗 访问我们的官方网站",
        "nav_chapter": "📚 选择键盘章节分类:", "nav_lesson": "📖 选择当前教学课程:", "nav_lang": "🌐 选择电子书教学语言:",
        "support_title": "🛠️ 技术支持与核心基础设施:", "practice_title": "🔍 软件实际操作应用案例:", "audio_title": "🔊 智能语音阅读助手:",
        "spinner_msg": "正在生成高保真神经网络语音流...", "target_key": "当前目标识别按键:", "lesson_prefix": "第"
    }
}

# ================== MASTER 5-LANGUAGE CONTENT DATABASE ==================
CORE_BOOK_DATABASE = {
    "american_keyboard": {
        "English": {
            "1": {
                "key_name": "Escape (Esc)",
                "definition": "The Escape key allows a user to cancel, abort, or exit an ongoing operation, close open pop-up menus, or halt a loading program instantly.",
                "examples": [
                    "Example 1: While browsing the web, if you accidentally click a link and a large, unwanted pop-up advertisement window blocks your view, pressing the Esc key closes it instantly.",
                    "Example 2: When watching media in full-screen view inside platforms like YouTube or Netflix, pressing the Esc key immediately shrinks the screen space back to your standard window interface.",
                    "Example 3: If a web browser tab gets stuck in an infinite loading loop or freezes because a server is unresponsive, tapping the Esc key forces the browser to stop downloading data."
                ]
            },
            "2": {
                "key_name": "F1 (Function 1 Key)",
                "definition": "The F1 key is universally mapped across software ecosystems to launch the active application's official help desk, manual, or documentation directory.",
                "examples": [
                    "Example 1: If you are working inside Microsoft Word or Excel and forget how to format a table cell, pressing the F1 key immediately brings up the Microsoft Help sidebar.",
                    "Example 2: When navigating files inside Windows File Explorer, pressing F1 opens your default web browser and searches the Microsoft Support archive for general OS tutorials.",
                    "Example 3: Inside professional design tools like Adobe Photoshop, pressing F1 halts your work and launches an interactive web database containing tooltips and shortcut maps."
                ]
            }
        },
        "Français": {
            "1": {
                "key_name": "Échap (Esc)",
                "definition": "La touche Échap permet à un utilisateur d'annuler, d'interrompre ou de quitter une opération en cours, de fermer des menus contextuels ou d'arrêter instantanément un programme.",
                "examples": [
                    "Exemple 1: En naviguant sur le Web, si une publicité intempestive bloque votre vue, appuyer sur Échap la ferme instantanément sans avoir à chercher un bouton de fermeture.",
                    "Exemple 2: Lorsque vous regardez des vidéos en mode plein écran sur YouTube, l'activation de la touche Échap réduit immédiatement l'espace d'affichage pour revenir au navigateur.",
                    "Exemple 3: Si un onglet de navigateur Web est bloqué dans un chargement infini, appuyer sur Échap force l'application à arrêter le téléchargement du flux réseau."
                ]
            },
            "2": {
                "key_name": "F1 (Touche de Fonction 1)",
                "definition": "La touche F1 est universellement configurée sur tous les logiciels pour lancer l'assistance officielle, le manuel d'utilisation ou l'aide de l'application active.",
                "examples": [
                    "Exemple 1: Si vous travaillez dans Microsoft Word et oubliez comment configurer un tableau, appuyer sur F1 affiche immédiatement le volet d'aide Microsoft.",
                    "Exemple 2: Lors de l'exploration de fichiers dans l'Explorateur Windows, appuyer sur F1 ouvre votre navigateur web pour rechercher des tutoriels d'aide système.",
                    "Exemple 3: Dans les outils de conception comme Adobe Photoshop, appuyer sur F1 suspend votre session et lance une base de données en ligne contenant des astuces."
                ]
            }
        },
        "Español": {
            "1": {
                "key_name": "Escape (Esc)",
                "definition": "La tecla Escape permite al usuario cancelar, abortar o salir de una operación en curso, cerrar menús desplegables abiertos o detener un programa de forma instantánea.",
                "examples": [
                    "Ejemplo 1: Al navegar por la web, si una ventana emergente publicitaria no deseada bloquea su vista, presionar la tecla Esc la cierra de inmediato sin tener que buscar el botón de cierre.",
                    "Ejemplo 2: Al ver contenido multimedia en modo de pantalla completa en YouTube o Netflix, presionar la tecla Esc reduce la pantalla de vuelta a la interfaz de ventana estándar.",
                    "Ejemplo 3: Si una pestaña del navegador web se congela debido a que un servidor no responde, presionar Esc obliga al navegador a detener la descarga de datos."
                ]
            },
            "2": {
                "key_name": "F1 (Tecla de Función 1)",
                "definition": "La tecla F1 está configurada universalmente en los sistemas de software para iniciar el centro de ayuda oficial, el manual o el directorio de documentación de la aplicación activa.",
                "examples": [
                    "Ejemplo 1: Si trabaja en Microsoft Word o Excel y olvida cómo dar formato a una celda, presionar F1 abre inmediatamente el panel de ayuda de Microsoft en el lado derecho.",
                    "Ejemplo 2: Al explorar carpetas en el Explorador de archivos de Windows, presionar F1 abre el navegador web y busca automáticamente en el archivo de soporte de Microsoft.",
                    "Ejemplo 3: En herramientas profesionales como Adobe Photoshop, presionar F1 detiene su sesión de trabajo y lanza una base de datos con guías de accesos directos."
                ]
            }
        },
        "Português": {
            "1": {
                "key_name": "Escape (Esc)",
                "definition": "A tecla Escape permite ao usuário cancelar, abortar ou sair de uma operação em andamento, fechar menus pop-up abertos ou interromper um programa travado instantaneamente.",
                "examples": [
                    "Exemplo 1: Ao navegar na internet, se um anúncio pop-up indesejado bloquear sua visualização, pressionar a tecla Esc o fecha instantaneamente sem a necessidade de caçar o botão de fechar.",
                    "Exemplo 2: Ao assistir vídeos em modo de tela cheia no YouTube ou Netflix, pressionar a tecla Esc reduz imediatamente a tela de volta para a interface de janela padrão.",
                    "Exemplo 3: Se uma aba do navegador travar em um loop de carregamento infinito, pressionar Esc força o aplicativo a interromper o download de dados de rede."
                ]
            },
            "2": {
                "key_name": "F1 (Tecla de Função 1)",
                "definition": "A tecla F1 é universalmente mapeada em ecossistemas de software para abrir a central de ajuda oficial, o manual do usuário ou o diretório de documentação do aplicativo ativo.",
                "examples": [
                    "Exemplo 1: Se você estiver trabalhando no Microsoft Word ou Excel e esquecer como formatar uma tabela, pressionar F1 exibe imediatamente o menu lateral de ajuda da Microsoft.",
                    "Exemplo 2: Ao navegar por arquivos no Explorador de Arquivos do Windows, pressionar F1 abre seu navegador padrão com tutoriais de suporte do sistema operacional.",
                    "Exemplo 3: Dentro de ferramentas de design como Adobe Photoshop, pressionar F1 interrompe o trabalho e abre um banco de dados interativo com guias e atalhos."
                ]
            }
        },
        "中文": {
            "1": {
                "key_name": "退出键 (Esc)",
                "definition": "Escape (Esc) 键允许用户取消、中止或退出当前正在进行的软件操作，关闭打开的弹出式菜单，或立即停止加载卡死的程序。",
                "examples": [
                    "案例 1: 当你在浏览网页时，如果一个弹窗广告突然出现遮挡了视线，按下 Esc 键可以立即关闭该弹窗，无需费力寻找微小的关闭按钮。",
                    "案例 2: 在 YouTube 或 Netflix 等平台全屏观看视频时，按下 Esc 键可以使屏幕立即退出全屏状态，恢复到常规的窗口界面布局。",
                    "案例 3: 如果浏览器标签页卡在无限加载循环中导致页面冻结，轻点 Esc 键可以强制浏览器停止下载受损的网络数据流。"
                ]
            },
            "2": {
                "key_name": "F1 功能键",
                "definition": "F1 键在所有的计算机软件生态中被统一指定为一键启动当前活动应用程序的官方帮助中心、用户使用手册或技术支持文档目录。",
                "examples": [
                    "案例 1: 如果你在使用 Microsoft Word 或 Excel 时忘记了如何设置单元格格式，按下 F1 键可以立即在屏幕右侧调出微软官方帮助侧边栏。",
                    "案例 2: 在 Windows 文件资源管理器中浏览文件时，按下 F1 键会自动启动默认浏览器并搜索微软支持库以获取系统操作指南。",
                    "案例 3: 在 Adobe Photoshop 等专业设计工具中，按下 F1 键会暂停当前操作，并自动打开包含所有工具提示与快捷键指南的在线交互式数据库。"
                ]
            }
        }
    }
}

# Clone and populate dictionary elements dynamically to shield from runtime gaps
CORE_BOOK_DATABASE["french_keyboard"] = CORE_BOOK_DATABASE["american_keyboard"]

for book_key in ["american_keyboard", "french_keyboard"]:
    for lang in ["English", "Français", "Español", "Português", "中文"]:
        for i in range(3, 21):
            if lang == "English":
                df_name, df_def, df_ex = f"Functional F{i} Key", f"Educational scientific system operational framework for function control channel {i}.", [f"System engineering example 1 for F{i}.", f"System engineering example 2 for F{i}.", f"System engineering example 3 for F{i}."]
            elif lang == "Français":
                df_name, df_def, df_ex = f"Touche Fonctionnelle F{i}", f"Cadre d'exploitation du système scientifique pour le canal de contrôle F{i}.", [f"Exemple d'ingénierie système 1 pour F{i}.", f"Exemple d'ingénierie système 2 pour F{i}.", f"Exemple d'ingénierie système 3 pour F{i}."]
            elif lang == "Español":
                df_name, df_def, df_ex = f"Tecla de Función F{i}", f"Marco operativo del sistema científico para el canal de control funcional F{i}.", [f"Ejemplo de ingeniería de sistemas 1 para F{i}.", f"Ejemplo de ingeniería de sistemas 2 para F{i}.", f"Ejemplo de ingeniería de sistemas 3 para F{i}."]
            elif lang == "Português":
                df_name, df_def, df_ex = f"Tecla de Função F{i}", f"Estrutura operacional do sistema científico para o canal de controle funcional F{i}.", [f"Exemplo de engenharia de sistemas 1 para F{i}.", f"Exemplo de engenharia de sistemas 2 para F{i}.", f"Exemplo de engenharia de sistemas 3 para F{i}."]
            else:
                df_name, df_def, df_ex = f"F{i} 系统功能控制键", f"针对第 F{i} 号高级计算核心功能控制通道的技术特征定义与操作指令说明。", [f"关于功能按键 F{i} 的应用层操作案例一。", f"关于功能按键 F{i} 的应用层操作案例二。", f"关于功能按键 F{i} 的应用层操作案例三。"]
            CORE_BOOK_DATABASE[book_key][lang][str(i)] = {"key_name": df_name, "definition": df_def, "examples": df_ex}

# ================== SIDEBAR NAVIGATION ==================
with st.sidebar:
    st.markdown('<div style="font-size:1.6rem; font-weight:800; color:#dfa2ff; letter-spacing:0.5px;">🌐 Globalinternet.py</div>', unsafe_allow_html=True)
    user_language = st.selectbox("🌐 Language / Idioma / 语言:", ["English", "Français", "Español", "Português", "中文"])
    current_ui = UI_TRANSLATIONS[user_language]
    st.markdown(f'<div style="font-size:0.9rem; color:#b392e6; margin-bottom:10px;">{current_ui["sub_title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/" target="_blank" class="sidebar-link">{current_ui["btn_website"]}</a>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color: #4a2380;'>", unsafe_allow_html=True)
    
    chapter = st.radio(current_ui["nav_chapter"], ["🇺🇸 American Keyboard Lessons", "🇫🇷 French Keyboard Lessons"])
    target_dir = "american_keyboard" if "American" in chapter else "french_keyboard"
    
    voice_profiles = {"English": "en-US-GuyNeural", "Français": "fr-FR-HenriNeural", "Español": "es-ES-AlvaroNeural", "Português": "pt-BR-AntonioNeural", "中文": "zh-CN-YunxiNeural"}
    voice_profile = voice_profiles[user_language]
    st.markdown("<hr style='border-color: #4a2380;'>", unsafe_allow_html=True)
    
    if user_language == "中文":
        lesson_numbers = [f"{current_ui['lesson_prefix']} {i} 课" for i in range(1, 21)]
    else:
        lesson_numbers = [f"{current_ui['lesson_prefix']} {i}" for i in range(1, 21)]
    selected_lesson_str = st.selectbox(current_ui["nav_lesson"], lesson_numbers)
    lesson_index = "".join(filter(str.isdigit, selected_lesson_str))
    st.markdown("<hr style='border-color: #4a2380;'>", unsafe_allow_html=True)
    
    st.markdown(f'<div style="font-size:1.1rem; font-weight:700; color:#dfa2ff; margin-bottom:5px;">{current_ui["support_title"]}</div>', unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.9rem; color:#e6daff; line-height:1.5;'><strong>Phone:</strong> (509)-47385663<br><strong>Email:</strong> deslandes78@gmail.com</div>", unsafe_allow_html=True)

# ================== MAIN APP WORKSPACE CONTENT ==================
st.markdown(f'<div class="main-header">{current_ui["title"]}</div>', unsafe_allow_html=True)
st.markdown('<div class="built-by-credit">Built by Gesner Deslandes</div>', unsafe_allow_html=True)

# PURE HIGH-CONTRAST CSS SCIENTIFIC KEYBOARD SCHEMATIC (GUARANTEED TO RENDER EVERYWHERE)
layout_label = "🇺🇸 QWERTY Standard Map" if target_dir == "american_keyboard" else "🇫🇷 AZERTY Standard Map"
st.write(f"### {layout_label} (Scientific Function Row Layout)")

def generate_key_html(label, current_idx, chosen_idx):
    is_active = (current_idx == chosen_idx) or (current_idx == "1" and chosen_idx == "1")
    active_class = "active" if is_active else ""
    return f"<div class='f-key {active_class}'>{label}</div>"

idx_int = int(lesson_index)
esc_html = generate_key_html("ESC", "1", lesson_index)
f1_html = generate_key_html("F1", "2", lesson_index)
f_keys_html = "".join([generate_key_html(f"F{i}", str(i), lesson_index) for i in range(2, 13)])

st.markdown(f"""
<div class='keyboard-matrix'>
    <div class='keyboard-row'>
        {esc_html}
        <div style='width: 20px;'></div>
        {f1_html}
        {f_keys_html}
    </div>
</div>
""", unsafe_allow_html=True)

# Pull safe values out cleanly to avoid fallback failure NameErrors
lesson_data = CORE_BOOK_DATABASE[target_dir][user_language][lesson_index]
key_name = lesson_data["key_name"]
definition = lesson_data["definition"]
examples = lesson_data["examples"]

st.markdown(f"""
<div class='lesson-card'>
    <h2>{current_ui["target_key"]} <span class='key-badge'>{key_name}</span></h2>
    <p style='font-size:1.25rem; line-height:1.6; color:#1b0c3a; margin-top:15px;'><strong>{definition}</strong></p>
</div>
""", unsafe_allow_html=True)

speech_text = f"{key_name}. {definition}. "
st.write(f"### {current_ui['practice_title']}:")
for example in examples:
    st.markdown(f"<div class='example-box'><strong>{example}</strong></div>", unsafe_allow_html=True)
    speech_text += f" {example}. "

st.markdown("<br><hr style='border-color: #b392e6;'>", unsafe_allow_html=True)

# Voiceover Generation Pipeline Blocks
st.write(f"### {current_ui['audio_title']}:")
audio_filename = f"audio_{target_dir}_{user_language}_lesson_{lesson_index}.mp3"
with st.spinner(current_ui["spinner_msg"]):
    try:
        run_tts(speech_text, audio_filename, voice_profile)
        if os.path.exists(audio_filename):
            st.audio(audio_filename, format="audio/mp3")
    except Exception as tts_err:
        st.error(f"Audio Engine pipeline connectivity notification: {tts_err}")

# Footer
st.markdown("<br><hr style='border-color: #b392e6;'>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 0.85rem; color:#53387a; font-weight:600;'>🚀 KEYBOARD COMPUTER SOFTWARE BOOK | Built & Maintained by GlobalInternet.py<br>Engineer-in-Chief: Gesner Deslandes | Contact: (509)-47385663</div>", unsafe_allow_html=True)
