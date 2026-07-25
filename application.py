import streamlit as st
import streamlit.components.v1 as components

# 1. Force Page Configuration
st.set_page_config(
    page_title="HURIAN YAHYA TEBE — ITS 2026",
    page_icon="⛵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Inject Custom CSS for Editorial Dark Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800;900&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background-color: #080A0F !important;
    color: #FFFFFF !important;
    overflow-x: hidden;
}

.block-container {
    padding: 0rem !important;
    max-width: 100% !important;
}

#MainMenu, footer, header { visibility: hidden; }

.spline-bg-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 0;
}

.main-scroll-content {
    position: relative;
    z-index: 10;
    width: 100%;
}

.hero-section {
    min-height: 100vh;
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

.scroll-indicator {
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #71717A;
}

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

# 3. Fixed Full-Screen Spline 3D Background
components.html("""
<div class="spline-bg-container" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:0;">
    <iframe src="https://my.spline.design/animatedpaperboat-dT4G6ed1AwwVip0rKa99F5OV/" frameborder="0" width="100%" height="100%"></iframe>
</div>
""", height=0)

# 4. Unindented Raw HTML Layout Overlay
html_content = """
<div class="main-scroll-content">
<section class="hero-section">
<div>
<div class="hero-tag">PKKMB ITS 2026</div>
<h1 class="hero-title">HURIAN YAHYA<br>TEBE</h1>
<p class="hero-subtitle">Known as Nano / Navy. Mahasiswa Baru Perguruan Tinggi ITS 2026. Ready to navigate, adapt, and build the future.</p>
<div class="scroll-indicator">SCROLL TO EXPLORE &downarrow;</div>
</div>
</section>
<section class="editorial-section">
<div>
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
<section class="editorial-section" style="background: rgba(8,10,15,0.98);">
<div>
<div class="section-num">02 / VISION</div>
<h2 class="section-heading">PKKMB & FUTURE GOALS</h2>
<div class="grid-2">
<div class="content-block">
<h4>PKKMB TARGETS</h4>
<p>Comprehensive immersion into ITS campus culture, establishing meaningful networks with fellow freshmen, and understanding academic frameworks to excel from Day 1.</p>
</div>
<div class="content-block">
<h4>4-YEAR ACADEMIC ROADMAP</h4>
<p>Maintain top-tier academic performance, actively contribute to student organizations (UKM/Himpunan), and participate in national technology competitions and industry internships.</p>
</div>
</div>
</div>
</section>
<footer class="site-footer">
<div>HURIAN YAHYA TEBE &mdash; ITS 2026</div>
<div>STORYTELLING THROUGH CODE & 3D</div>
</footer>
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)