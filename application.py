import streamlit as st
import streamlit.components.v1 as components

# 1. Force Page Setup & Dark Theme Baseline
st.set_page_config(
    page_title="Hurian Yahya Tebe — PKKMB ITS 2026",
    page_icon="⛵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for Apple/Samsung Style Layout & Glassmorphism Theme
st.markdown("""
    <style>
    /* Hide Streamlit default headers & clean margins */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 1rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    
    /* Dark Theme Global Variables */
    .stApp {
        background-color: #0B0F19;
    }

    /* Headings */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
        margin-bottom: 0.5rem;
    }
    
    .gradient-text {
        background: linear-gradient(135deg, #67F3CE 0%, #4899EA 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .section-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }

    .section-subtitle {
        font-size: 1.1rem;
        color: #94A3B8;
        margin-bottom: 2rem;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.75rem;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        color: #E2E8F0;
        margin-bottom: 1.5rem;
    }

    .badge {
        display: inline-block;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        background: rgba(103, 243, 206, 0.1);
        border: 1px solid rgba(103, 243, 206, 0.3);
        color: #67F3CE;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# SECTION 1: HERO TITLE CARD (Apple Style)
# =========================================================
st.markdown('<div class="badge">✨ PKKMB ITS 2026</div>', unsafe_allow_html=True)

hero_col1, hero_col2 = st.columns([1.2, 1], gap="large")

with hero_col1:
    st.markdown("""
        <div style="padding-top: 2rem;">
            <h1 class="hero-title">
                Halo, Saya <br><span class="gradient-text">Hurian Yahya Tebe</span>
            </h1>
            <p style="font-size: 1.25rem; color: #64748B; font-weight: 500; margin-bottom: 1.5rem;">
                (dipanggil Nano / Navy)
            </p>
            <div class="glass-card">
                <p style="font-size: 1.05rem; line-height: 1.7; color: #CBD5E1; margin: 0;">
                    📍 <b>Status:</b> Mahasiswa Baru — ITS 2026<br>
                    ⛵ <b>Semangat:</b> Siap berlayar, beradaptasi, dan berkarya di kampus perjuangan.
                </p>
            </div>
            <p style="color: #94A3B8; font-size: 0.95rem;">
                👇 <i>Scroll ke bawah untuk mengenal saya lebih dekat</i>
            </p>
        </div>
    """, unsafe_allow_html=True)

with hero_col2:
    # Embedded 3D Spline Canvas
    spline_html = """
    <div style="width: 100%; height: 480px; border-radius: 20px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <iframe src='https://my.spline.design/animatedpaperboat-dT4G6ed1AwwVip0rKa99F5OV/' 
                frameborder='0' 
                width='100%' 
                height='100%'>
        </iframe>
    </div>
    """
    components.html(spline_html, height=500)

st.markdown("<br><hr style='border-color: rgba(255,255,255,0.08);'><br>", unsafe_allow_html=True)

# =========================================================
# SECTION 2: ACADEMIC & SKILLS (Scroll Down)
# =========================================================
st.markdown('<div class="section-title">📚 Background & Skills</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Pengalaman, Minat Utama, dan Keahlian Digital</div>', unsafe_allow_html=True)

sec2_col1, sec2_col2 = st.columns(2, gap="medium")

with sec2_col1:
    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #67F3CE; margin-top:0;">🛠️ Keahlian & Minat</h3>
            <ul style="color: #CBD5E1; line-height: 1.8; padding-left: 1.2rem;">
                <li><b>Teknologi:</b> Web Development, Python Programming, Digital Media</li>
                <li><b>Design & 3D:</b> Interactive UI/UX, Spline 3D Integration</li>
                <li><b>Soft Skills:</b> Problem Solving, Adaptabilitas, Teamwork</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with sec2_col2:
    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #4899EA; margin-top:0;">🏆 Pengalaman & Proyek</h3>
            <ul style="color: #CBD5E1; line-height: 1.8; padding-left: 1.2rem;">
                <li><b>Proyek Web PKKMB:</b> Mengembangkan website perkenalan interaktif berbasis Streamlit & Spline 3D.</li>
                <li><b>Aktivitas Organisasi:</b> Aktif berkolaborasi dalam kegiatan tim dan komunitas.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><hr style='border-color: rgba(255,255,255,0.08);'><br>", unsafe_allow_html=True)

# =========================================================
# SECTION 3: PKKMB GOALS & TARGETS (Scroll Down)
# =========================================================
st.markdown('<div class="section-title">🚀 PKKMB & Future Goals</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Target & Harapan Selama Perkuliahan di ITS</div>', unsafe_allow_html=True)

sec3_col1, sec3_col2 = st.columns(2, gap="medium")

with sec3_col1:
    st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #67F3CE;">
            <h3 style="color: #FFFFFF; margin-top:0;">🎯 Target PKKMB</h3>
            <ol style="color: #CBD5E1; line-height: 1.8; padding-left: 1.2rem;">
                <li>Mengenal budaya akademik dan nilai-nilai kampus ITS.</li>
                <li>Membangun jaringan relasi positif dengan sesama mahasiswa baru.</li>
                <li>Memahami fasilitas serta peluang pengembangan diri di perguruan tinggi.</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)

with sec3_col2:
    st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #4899EA;">
            <h3 style="color: #FFFFFF; margin-top:0;">📌 Target 4 Tahun Ke Depan</h3>
            <ol style="color: #CBD5E1; line-height: 1.8; padding-left: 1.2rem;">
                <li><b>Akademik:</b> Mempertahankan prestasi tinggi dan lulus tepat waktu.</li>
                <li><b>Organisasi:</b> Aktif dalam UKM / Himpunan Mahasiswa.</li>
                <li><b>Inovasi:</b> Mengikuti kompetisi teknologi & program magang nasional.</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <br><br>
    <div style="text-align: center; color: #475569; font-size: 0.85rem;">
        Created with Streamlit & Spline 3D • Hurian Yahya Tebe (PKKMB ITS 2026)
    </div>
""", unsafe_allow_html=True)