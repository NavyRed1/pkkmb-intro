import streamlit as st
import base64
from io import BytesIO
from PIL import Image

st.set_page_config(
    page_title="Interactive Portfolio Website",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper function to prevent Streamlit from interpreting indented HTML as markdown code blocks
def render_html(html_content):
    """Strips leading whitespace from every line so Markdown won't parse it as code."""
    cleaned = "\n".join([line.strip() for line in html_content.split("\n")])
    st.markdown(cleaned, unsafe_allow_html=True)

def image_to_base64(img):
    """Converts PIL Image to base64 string for embedding in HTML."""
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

st.sidebar.title("⚙️ Customization Panel")
st.sidebar.markdown("Update your portfolio details below:")

# Front page hero fields
st.sidebar.subheader("🏠 Hero Section")
user_name = st.sidebar.text_input("Full Name", value="Alex Morgan")
user_tagline = st.sidebar.text_input("Tagline / Headline", value="Creative Developer & UI/UX Specialist")
uploaded_hero_photo = st.sidebar.file_uploader("Hero Section Photo (JPG/PNG)", type=["jpg", "jpeg", "png"], key="hero_photo")

st.sidebar.markdown("---")
# About me page fields
st.sidebar.subheader("👤 About Me Section")
uploaded_about_photo = st.sidebar.file_uploader("About Me Photo (JPG/PNG)", type=["jpg", "jpeg", "png"], key="about_photo")
user_nickname = st.sidebar.text_input("Nickname (Top Left)", value="Alex")
user_city = st.sidebar.text_input("City of Origin (Middle Left)", value="Surabaya, Indonesia")
user_fav_food = st.sidebar.text_input("Favorite Food (Top Right)", value="Ramen & Matcha Latte")
user_fun_fact = st.sidebar.text_input("Fun Fact (Middle Right)", value="Can code for 12 hours straight with good music!")

# Process Hero Photo
hero_photo_src = ""
if uploaded_hero_photo is not None:
    try:
        pil_img = Image.open(uploaded_hero_photo)
        hero_photo_src = f"data:image/png;base64,{image_to_base64(pil_img)}"
    except Exception:
        hero_photo_src = ""
else:
    try:
        # 1st Fallback: Load hero.jpg from your GitHub repository
        pil_img = Image.open("hero.jpg")
        hero_photo_src = f"data:image/png;base64,{image_to_base64(pil_img)}"
    except Exception:
        hero_photo_src = ""  # Final fallback: placeholder icon

about_photo_src = ""
if uploaded_about_photo is not None:
    try:
        pil_img_about = Image.open(uploaded_about_photo)
        about_photo_src = f"data:image/png;base64,{image_to_base64(pil_img_about)}"
    except Exception:
        about_photo_src = hero_photo_src
else:
    try:
        # 1st Fallback: Load about.jpg from your GitHub repository
        pil_img_about = Image.open("about.jpg")
        about_photo_src = f"data:image/png;base64,{image_to_base64(pil_img_about)}"
    except Exception:
        # 2nd Fallback: If about.jpg isn't found in repo, reuse the Hero photo
        about_photo_src = hero_photo_src if provided

custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Plus+Jakarta+Sans:wght@300;400;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background-color: transparent !important;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    div.block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    html, body {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #ffffff;
        scroll-behavior: smooth;
        background: #090a0f;
    }

    /* Fixed Spline Background Wrapper */
    .spline-bg-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -2;
        overflow: hidden;
    }

    .spline-iframe {
        width: 100%;
        height: 100%;
        border: none;
    }

    /* Floating Navigation Header with Screenshots 6, 8, 10 button designs */
    .nav-bar {
        position: fixed;
        top: 1.5rem;
        right: 3rem;
        z-index: 100;
        display: flex;
        gap: 1.2rem;
        align-items: center;
    }

    /* Pill Button Style matching Screenshots 6 & 8 & 10 */
    .nav-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.5rem 1.4rem;
        background: #FF9F63;
        color: #FFFFFF !important;
        text-decoration: none !important;
        font-weight: 800;
        font-size: 0.95rem;
        border-radius: 40px;
        box-shadow: 0 6px 16px rgba(255, 159, 99, 0.4);
        border: 2px solid #FFAF7B;
        transition: all 0.3s ease;
    }

    .nav-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 22px rgba(255, 159, 99, 0.6);
        background: #FF8D47;
    }

    .nav-icon-badge {
        width: 30px;
        height: 30px;
        background: #FFFFFF;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #FF8A4C;
        font-size: 0.95rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }

    /* Left Sidebar Accent Bar */
    .aesthetic-sidebar {
        position: fixed;
        left: 0;
        top: 0;
        height: 100vh;
        width: 65px;
        background: rgba(10, 10, 20, 0.35);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        padding: 2.5rem 0;
        z-index: 50;
    }

    .brand-logo {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        letter-spacing: 2px;
        writing-mode: vertical-rl;
        transform: rotate(180deg);
        color: rgba(255, 255, 255, 0.9);
    }

    .vertical-accent-line {
        width: 2px;
        height: 80px;
        background: linear-gradient(to bottom, #ff5e62, #ff9966);
    }

    /* Section Container Layout */
    .section-container {
        position: relative;
        width: 100vw;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
        padding: 3rem 4rem 3rem 6rem;
    }

    /* Hero Section Layout */
    .hero-grid {
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 3rem;
        width: 100%;
        max-width: 1200px;
        align-items: center;
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 4.5rem;
        font-weight: 700;
        line-height: 1.05;
        text-transform: uppercase;
        background: linear-gradient(135deg, #ffffff 0%, rgba(255,255,255,0.7) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.2rem;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.8);
        margin-bottom: 2rem;
        max-width: 500px;
        line-height: 1.6;
    }

    /* Hero Yellow Capsule Button matching Screenshot 4 */
    .cta-yellow-button {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.85rem 2.8rem;
        background: #FFCA28;
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 1.1rem;
        text-decoration: none !important;
        border-radius: 50px;
        border: 2px solid rgba(255, 255, 255, 0.9);
        box-shadow: 0 10px 25px rgba(255, 202, 40, 0.5);
        transition: all 0.3s ease;
    }

    .cta-yellow-button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 14px 30px rgba(255, 202, 40, 0.7);
        background: #FFC107;
    }

    .hero-photo-card {
        width: 100%;
        aspect-ratio: 4/5;
        max-width: 380px;
        border-radius: 24px;
        overflow: hidden;
        border: 2px dashed rgba(255, 255, 255, 0.3);
        background: rgba(15, 15, 25, 0.6);
        backdrop-filter: blur(16px);
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
    }

    .photo-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    /* About Me Section Layout (Inspired by Screenshot 2) */
    .about-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 1100px;
        position: relative;
    }

    .about-script-title {
        font-family: 'Great Vibes', cursive;
        font-size: 5.5rem;
        color: #ffffff;
        text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        margin-bottom: -1.5rem;
        z-index: 10;
        text-align: center;
    }

    .about-content-grid {
        display: grid;
        grid-template-columns: 1fr 340px 1fr;
        gap: 2rem;
        align-items: center;
        width: 100%;
        margin-top: 1rem;
    }

    .about-column {
        display: flex;
        flex-direction: column;
        gap: 2.5rem;
    }

    .about-card-left {
        align-self: flex-end;
    }

    .about-card-right {
        align-self: flex-start;
    }

    .info-capsule {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 30px;
        padding: 0.9rem 1.6rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        color: #1a1a2e;
        max-width: 280px;
        transition: all 0.3s ease;
    }

    .info-capsule:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.35);
        background: #ffffff;
    }

    .capsule-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #ff7b54;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    .capsule-value {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1a1a2e;
        line-height: 1.3;
    }

    .about-photo-frame {
        width: 100%;
        height: 440px;
        border-radius: 32px;
        overflow: hidden;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        border: 4px solid rgba(255, 255, 255, 0.2);
        background: rgba(20, 20, 35, 0.7);
        backdrop-filter: blur(12px);
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
"""

render_html(custom_css)

nav_html = """
<div class="nav-bar">
    <a href="#hero" class="nav-btn">
        <div class="nav-icon-badge">🏠</div>
        HOME
    </a>
    <a href="#about" class="nav-btn">
        <div class="nav-icon-badge">👤</div>
        ABOUT
    </a>
    <a href="#thankyou" class="nav-btn">
        CONTACT
        <div class="nav-icon-badge">📞</div>
    </a>
</div>

<div class="aesthetic-sidebar">
    <div class="brand-logo">PORTFOLIO</div>
    <div class="vertical-accent-line"></div>
    <div style="font-size: 0.8rem; opacity: 0.6;">2026</div>
</div>

<div class="spline-bg-container">
    <iframe src="https://my.spline.design/animatedlightdesktop-dEHPT5RsJPdOAeEgIR3FbIiN/" class="spline-iframe"></iframe>
</div>
"""

render_html(nav_html)

if hero_photo_src:
    hero_photo_content = f'<img src="{hero_photo_src}" class="photo-img" alt="Hero Photo">'
    hero_border = "none"
else:
    hero_photo_content = '<div style="text-align:center; padding: 2rem; color: rgba(255,255,255,0.6);"><span style="font-size:3rem;">📸</span><p>Upload Photo in Sidebar</p></div>'
    hero_border = "dashed"

hero_section_html = f"""
<section id="hero" class="section-container">
    <div class="hero-grid">
        <div>
            <div style="text-transform: uppercase; letter-spacing: 3px; font-weight: 700; color: #ff9966; margin-bottom: 1rem;">
                WELCOME TO MY PORTFOLIO
            </div>
            <h1 class="hero-title">{user_name}</h1>
            <p class="hero-subtitle">{user_tagline}</p>
            <a href="#about" class="cta-yellow-button">About Me ➔</a>
        </div>
        <div>
            <div class="hero-photo-card" style="border-style: {hero_border};">
                {hero_photo_content}
            </div>
        </div>
    </div>
</section>
"""

render_html(hero_section_html)

if about_photo_src:
    about_photo_content = f'<img src="{about_photo_src}" class="photo-img" alt="About Me Photo">'
else:
    about_photo_content = '<div style="text-align:center; padding: 2rem; color: rgba(255,255,255,0.6);"><span style="font-size:3rem;">👤</span><p>Upload Photo in Sidebar</p></div>'

about_section_html = f"""
<section id="about" class="section-container">
    <div class="about-wrapper">
        <h2 class="about-script-title">About Me</h2>
        
        <div class="about-content-grid">
            <div class="about-column about-card-left">
                <div class="info-capsule">
                    <div class="capsule-label">✨ Nickname</div>
                    <div class="capsule-value">{user_nickname}</div>
                </div>
                <div class="info-capsule">
                    <div class="capsule-label">📍 City of Origin</div>
                    <div class="capsule-value">{user_city}</div>
                </div>
            </div>

            <div class="about-photo-frame">
                {about_photo_content}
            </div>

            <div class="about-column about-card-right">
                <div class="info-capsule">
                    <div class="capsule-label">🍕 Favorite Food</div>
                    <div class="capsule-value">{user_fav_food}</div>
                </div>
                <div class="info-capsule">
                    <div class="capsule-label">💡 Fun Fact</div>
                    <div class="capsule-value">{user_fun_fact}</div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

render_html(about_section_html)

thankyou_section_html = """
<section id="thankyou" style="width: 100vw; height: 100vh; margin: 0; padding: 0; overflow: hidden; position: relative;">
    <iframe src="https://my.spline.design/drone-7OFa70Z6eWoG2HkoWXwWhTpl/" frameborder="0" width="100%" height="100%" style="width: 100%; height: 100%; border: none;"></iframe>
</section>
"""

render_html(thankyou_section_html)