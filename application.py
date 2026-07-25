import streamlit as st
import base64
from io import BytesIO
from PIL import Image
import textwrap

st.set_page_config(
    page_title="Portfolio Website",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

def image_to_base64(img):
    """Converts PIL Image or byte array to base64 string for HTML embedding."""
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

st.sidebar.title("⚙️ Customization Panel")
st.sidebar.markdown("Update your portfolio information and photo here:")

# Live editable profile fields
user_name = st.sidebar.text_input("Full Name", value="Alex Morgan")
user_tagline = st.sidebar.text_input("Tagline / Headline", value="Creative Developer & UI/UX Specialist")

st.sidebar.markdown("---")
st.sidebar.subheader("📸 Profile Photo")
uploaded_photo = st.sidebar.file_uploader("Upload your photo (JPG/PNG)", type=["jpg", "jpeg", "png"])

st.sidebar.markdown("---")
st.sidebar.subheader("🎓 About Me Information")
user_campus = st.sidebar.text_input("Campus / University", value="Institute of Technology")
user_major = st.sidebar.text_input("Major / Field of Study", value="Computer Science & Interactive Media")
user_city = st.sidebar.text_input("City of Origin", value="Surabaya, Indonesia")
user_bio = st.sidebar.text_area(
    "About Me Bio", 
    value="Passionate developer dedicated to creating stunning, interactive, and modern digital experiences. Specializing in front-end aesthetics, 3D web graphics, and clean architecture.",
    height=120
)

if uploaded_photo is not None:
    try:
        pil_img = Image.open(uploaded_photo)
        img_b64 = image_to_base64(pil_img)
        photo_src = f"data:image/png;base64,{img_b64}"
    except Exception:
        photo_src = ""
else:
    try:
        # Opens default image saved in your repository folder
        pil_img = Image.open("profile.jpg")  # Change file name if using .png
        img_b64 = image_to_base64(pil_img)
        photo_src = f"data:image/png;base64,{img_b64}"
    except Exception:
        photo_src = ""  # Falls back to placeholder icon if file isn't found

custom_css = textwrap.dedent("""
<style>
    /* Reset default Streamlit layout padding and margins */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: transparent !important;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    div.block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }

    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=Space+Grotesk:wght@500;700&display=swap');

    html, body {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #ffffff;
        scroll-behavior: smooth;
        background: #090a0f;
    }

    /* Full-Screen Section Layouts */
    .section-container {
        position: relative;
        width: 100vw;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
        padding: 4rem 6rem;
    }

    /* Spline Background Wrapper */
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
        pointer-events: auto;
    }

    /* Floating Navigation Header */
    .nav-bar {
        position: fixed;
        top: 2rem;
        right: 4rem;
        z-index: 100;
        display: flex;
        gap: 2rem;
        background: rgba(15, 15, 25, 0.4);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        padding: 0.8rem 2rem;
        border-radius: 50px;
        border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .nav-link {
        color: rgba(255, 255, 255, 0.8);
        text-decoration: none;
        font-weight: 600;
        font-size: 0.95rem;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }

    .nav-link:hover {
        color: #ffffff;
        text-shadow: 0 0 10px rgba(255,255,255,0.5);
    }

    /* Left Aesthetic Sidebar Bar */
    .aesthetic-sidebar {
        position: fixed;
        left: 0;
        top: 0;
        height: 100vh;
        width: 70px;
        background: rgba(10, 10, 20, 0.35);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        padding: 3rem 0;
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
        border-radius: 2px;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(18, 18, 30, 0.55);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 24px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
        padding: 2.5rem;
    }

    /* Hero Layout Grid */
    .hero-grid {
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 3rem;
        width: 100%;
        max-width: 1300px;
        margin-left: 50px;
        align-items: center;
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 5rem;
        font-weight: 700;
        line-height: 1.05;
        text-transform: uppercase;
        background: linear-gradient(135deg, #ffffff 0%, rgba(255,255,255,0.7) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: rgba(255, 255, 255, 0.75);
        margin-bottom: 2.5rem;
        max-width: 540px;
        line-height: 1.6;
    }

    .cta-button {
        display: inline-block;
        padding: 1rem 2.5rem;
        background: linear-gradient(90deg, #3a7bd5 0%, #3a6073 100%);
        color: #ffffff;
        font-weight: 600;
        text-decoration: none;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(58, 123, 213, 0.3);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
    }

    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(58, 123, 213, 0.5);
    }

    /* Photo Upload Box */
    .photo-card {
        width: 100%;
        aspect-ratio: 4/5;
        max-width: 420px;
        border-radius: 24px;
        overflow: hidden;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border: 2px dashed rgba(255, 255, 255, 0.25);
        background: rgba(15, 15, 25, 0.6);
        backdrop-filter: blur(16px);
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
        transition: all 0.3s ease;
        margin: 0 auto;
    }

    .photo-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .photo-placeholder-text {
        text-align: center;
        color: rgba(255, 255, 255, 0.6);
        padding: 2rem;
    }

    .photo-placeholder-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }

    /* About Section Grid */
    .about-container {
        width: 100%;
        max-width: 1100px;
        margin-left: 50px;
        z-index: 10;
    }

    .about-header {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3.2rem;
        font-weight: 700;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #ffffff 0%, #a1c4fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }

    .info-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
    }

    .info-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #89f7fe;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }

    .info-value {
        font-size: 1.25rem;
        font-weight: 600;
        color: #ffffff;
    }

    .bio-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 2rem;
        line-height: 1.8;
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.9);
    }
</style>
""").strip()

st.markdown(custom_css, unsafe_allow_html=True)

nav_and_bg_html = textwrap.dedent("""
<div class="nav-bar">
    <a href="#hero" class="nav-link">HOME</a>
    <a href="#about" class="nav-link">ABOUT</a>
    <a href="#thankyou" class="nav-link">CONTACT</a>
</div>

<div class="aesthetic-sidebar">
    <div class="brand-logo">PORTFOLIO</div>
    <div class="vertical-accent-line"></div>
    <div style="font-size: 0.8rem; opacity: 0.6;">2026</div>
</div>

<div class="spline-bg-container">
    <iframe src="https://my.spline.design/animatedlightdesktop-dEHPT5RsJPdOAeEgIR3FbIiN/" 
            class="spline-iframe" frameborder="0"></iframe>
</div>
""").strip()

st.markdown(nav_and_bg_html, unsafe_allow_html=True)

if photo_src:
    photo_inner_html = f'<img src="{photo_src}" class="photo-img" alt="Profile Photo">'
    photo_border_style = "none"
else:
    photo_inner_html = '<div class="photo-placeholder-text"><span class="photo-placeholder-icon">📸</span><p><strong>Your Photo Here</strong></p><p style="font-size: 0.85rem; opacity: 0.7;">Upload a photo from the sidebar panel on the left</p></div>'
    photo_border_style = "dashed"

hero_html = textwrap.dedent(f"""
<section id="hero" class="section-container">
    <div class="hero-grid">
        <div>
            <div style="text-transform: uppercase; letter-spacing: 3px; font-weight: 600; color: #ff9966; margin-bottom: 1rem;">
                Welcome to my world
            </div>
            <h1 class="hero-title">{user_name}</h1>
            <p class="hero-subtitle">{user_tagline}</p>
            <a href="#about" class="cta-button">EXPLORE MORE &rarr;</a>
        </div>
        <div>
            <div class="photo-card" style="border-style: {photo_border_style};">
                {photo_inner_html}
            </div>
        </div>
    </div>
</section>
""").strip()

st.markdown(hero_html, unsafe_allow_html=True)

about_html = textwrap.dedent(f"""
<section id="about" class="section-container">
    <div class="about-container glass-card">
        <h2 class="about-header">About Me</h2>
        
        <div class="info-grid">
            <div class="info-card">
                <div class="info-label">🎓 Campus</div>
                <div class="info-value">{user_campus}</div>
            </div>
            
            <div class="info-card">
                <div class="info-label">📚 Major</div>
                <div class="info-value">{user_major}</div>
            </div>
            
            <div class="info-card">
                <div class="info-label">📍 City of Origin</div>
                <div class="info-value">{user_city}</div>
            </div>
        </div>
        
        <div class="info-label" style="margin-top: 1rem;">📝 Bio / Background</div>
        <div class="bio-box">
            {user_bio}
        </div>
    </div>
</section>
""").strip()

st.markdown(about_html, unsafe_allow_html=True)

thankyou_html = textwrap.dedent("""
<section id="thankyou" style="width: 100vw; height: 100vh; margin: 0; padding: 0; overflow: hidden; position: relative;">
    <iframe src="https://my.spline.design/drone-7OFa70Z6eWoG2HkoWXwWhTpl/" frameborder="0" width="100%" height="100%" style="width: 100%; height: 100%; border: none;"></iframe>
</section>
""").strip()

st.markdown(thankyou_html, unsafe_allow_html=True)