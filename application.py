import streamlit as st
import streamlit.components.v1 as components

# 1. Force Page Config
st.set_page_config(
    page_title="HURIAN YAHYA TEBE — ITS 2026",
    page_icon="⛵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for Full-Bleed 3D Background & High-Impact Typography (Nike Aesthetic)
st.markdown("""
    <style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800;900&display=swap');

    /* Reset Streamlit default container padding and backgrounds */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #080A0F !important;
        color: #FFFFFF;
        overflow-x: hidden;
    }
    
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }

    /* Hide Streamlit Chrome UI */
    #MainMenu, footer, header { visibility: hidden; }

    /* Fixed Full-Screen Background for Spline Canvas */
    .spline-bg-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 0;
        pointer-events: auto;
    }

    /* Content Overlay Container */
    .main-scroll-content {
        position: relative;
        z-index: 10;
        width: 100%;
        pointer-events: none; /* Allows mouse interactions to pass through to Spline 3D behind */
    }

    .interactive-element {
        pointer-events: auto; /* Re-enables clicking on text/buttons */
    }

    /* Section 1: Hero Typography (Nike-style Heavy Headings) */
    .hero-section {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding: 4rem 6%;
        box-sizing: border-box;
    }

    .hero-tag {
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        color: #67F3CE;
        margin-bottom: 0.75rem;
    }

    .hero-title {
        font-size: clamp(3.5rem, 8vw, 7rem);
        font-weight: 900;
        line-height: 0.95;
        letter-spacing: -0.03em;
        text-transform: uppercase;
        color: #FFFFFF;
        margin: 0 0 1rem 0;
        text-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }

    .hero-subtitle {
        font-size: clamp(1.1rem, 2vw, 1.5rem);
        font-weight: 400;
        color: #A1A1AA;
        max-width: 600px;
        margin-bottom: 2rem;
        line-height: 1.4;
    }

    /* Scroll Prompt Indicator */
    .scroll-indicator {
        font-size: 0.75rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #71717A;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Section 2 & 3: Editorial Content Layout */
    .editorial-section {
        min-height: 80vh;
        padding: 6rem 6%;
        background: linear-gradient(180deg, rgba(8,10,15,0) 0%, rgba(8,10,15,0.85) 30%, rgba(8,10,15,0.95) 100%);
        backdrop-filter: blur(8px);
    }

    .section-num {
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.2em;
        color: #4899EA;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }

    .section-heading {
        font-size: clamp(2rem, 4vw, 3.5rem);
        font-weight: 800;
        letter-spacing: -0.02em;
        margin-bottom: 3rem;
        text-transform: uppercase;
    }

    .grid-2 {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 3rem;
    }

    .content-block {
        border-top: 1px solid rgba(255, 255, 255, 0.15);
        padding-top: 1.5rem;
    }

    .content-block h4 {
        font-size: 1.25rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 0.75rem;
    }

    .content-block p, .content-block ul {
        font-size: 0.95rem;
        color: #A1A1AA;
        line-height: 1.7;
        margin: 0;
        padding-left: 0;
        list-style: none;
    }

    .content-block li {
        margin-bottom: 0.5rem;
    }

    /* Sleek Footer */
    .site-footer {
        padding: 3rem 6%;
        background: #080A0F;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        font-size: 0.8rem;
        color: #52525B;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 1. FIXED FULL-SCREEN SPLINE 3D BACKGROUND
# ---------------------------------------------------------
spline_fullscreen_html = """
<div class="spline-bg-container">
    <iframe src='https://my.spline.design/animatedpaperboat-dT4G6ed1AwwVip0rKa99F5OV/' 
            frameborder='0' 
            width='100%' 
            height='100%'>
    </iframe>
</div>
"""
components.html(spline_fullscreen_html, height=0)  # Rendered out-of-flow via CSS fixed positioning

# ---------------------------------------------------------
# 2. OVERLAY SCROLLING CONTENT
# ---------------------------------------------------------
st.markdown("""
<div class="main-scroll-content">
    
    <!-- HERO SECTION (FULL SCREEN 100VH) -->
    <section class="hero-section">
        <div class="interactive-element">
            <div class="hero-tag">PKKMB ITS 2026</div>
            <h1 class="hero-title">
                HURIAN YAHYA<br>TEBE
            </h1>
            <p class="hero-subtitle">
                Known as Nano / Navy. Mahasiswa Baru Perguruan Tinggi ITS 2026. Ready to navigate, adapt, and build the future.
            </p>
            <div class="scroll-indicator">
                <span>SCROLL TO EXPLORE</span> &downarrow;
            </div>
        </div>
    </section>

    <!-- SECTION 02: BACKGROUND & SKILLS -->
    <section class="editorial-section">
        <div class="interactive-element">
            <div class="section-num">01 / BACKGROUND</div>
            <h2 class="section-heading">SKILLS & EXPERIENCE</h2>
            
            <div class="grid-2">
                <div class="content-block">
                    <h4>CORE TECHNICAL SKILLS</h4>
                    <ul>
                        <li><b>Web Development:</b> Modern Frontend & Interactive UI Systems</li>
                        <li><b>Programming:</b> Python, Data Science & Algorithm Fundamentals</li>
                        <li><b>3D & Web Graphics:</b> Spline 3D Integration & Spatial Design</li>
                    </ul>
                </div>
                
                <div class="content-block">
                    <h4>EXPERIENCE & HIGHLIGHTS</h4>
                    <ul>
                        <li><b>Digital Projects:</b> Built interactive web experiences and prototypes.</li>
                        <li><b>Leadership:</b> Active collaborator in student organizations and tech communities.</li>
                        <li><b>Soft Skills:</b> Critical thinking, adaptive problem solving, and public speaking.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 03: GOALS & PKKMB -->
    <section class="editorial-section" style="background: rgba(8,10,15,0.98);">
        <div class="interactive-element">
            <div class="section-num">02 / VISION</div>
            <h2 class="section-heading">PKKMB & FUTURE GOALS</h2>
            
            <div class="grid-2">
                <div class="content-block">
                    <h4>PKKMB TARGETS</h4>
                    <p>
                        Comprehensive immersion into ITS campus culture, establishing meaningful networks with fellow freshmen, and understanding academic frameworks to excel from Day 1.
                    </p>
                </div>
                
                <div class="content-block">
                    <h4>4-YEAR ACADEMIC ROADMAP</h4>
                    <p>
                        Maintain top-tier academic performance, actively contribute to student organizations (UKM/Himpunan), and participate in national technology competitions and industry internships.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="site-footer interactive-element">
        <div>HURIAN YAHYA TEBE &mdash; ITS 2026</div>
        <div>STORYTELLING THROUGH CODE & 3D</div>
    </footer>

</div>
""", unsafe_allow_html=True)