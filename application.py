import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="PKKMB Introduction",
    page_icon="⛵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS styling for modern layout & cards
st.markdown("""
    <style>
    /* Remove default top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    /* Typography */
    .slide-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.2rem;
    }
    .slide-subtitle {
        font-size: 1.1rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
    /* Card Component */
    .info-card {
        background-color: #F8FAFC;
        border-left: 4px solid #4899EA;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Slide Navigation
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 1

def set_slide(slide_number):
    st.session_state.current_slide = slide_number

# Navigation Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("1️⃣ Slide 1: About Me", use_container_width=True):
        set_slide(1)
with col2:
    if st.button("2️⃣ Slide 2: Academic & Skills", use_container_width=True):
        set_slide(2)
with col3:
    if st.button("3️⃣ Slide 3: PKKMB Goals", use_container_width=True):
        set_slide(3)

st.divider()

# Layout: 2 Columns (Left: Slide Content | Right: Animated Spline Paper Boat)
left_col, right_col = st.columns([1.1, 1], gap="large")

# ---------------------------------------------------------
# LEFT COLUMN: SLIDE CONTENT
# ---------------------------------------------------------
with left_col:
    if st.session_state.current_slide == 1:
        st.markdown('<div class="slide-title">👋 Halo, Saya Hurian Yahya Tebe (dipanggil Nano/Navy)!</div>', unsafe_allow_html=True)
        st.markdown('<div class="slide-subtitle">Mahasiswa Baru — PKKMB ITS 2026</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <b>📍 Asal Daerah:</b> Makassar<br>
            <b>🏫 Program Studi:</b> Sistem Informasi<br>
            <b>✨ Motto:</b> "Berlayar menuju masa depan dengan semangat baru."
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        Selamat datang di halaman perkenalan resmi saya! Saya sangat antusias untuk menjadi 
        bagian dari civitas akademika dan berlayar bersama kawan-kawan baru di PKKMB tahun ini.
        """)

    elif st.session_state.current_slide == 2:
        st.markdown('<div class="slide-title">📚 Background & Skills</div>', unsafe_allow_html=True)
        st.markdown('<div class="slide-subtitle">Pengalaman & Minat Utama</div>', unsafe_allow_html=True)
        
        st.markdown("### 🛠️ Keahlian & Minat")
        st.write("- **Teknologi:** Web Development, Python, Digital Media")
        st.write("- **Soft Skills:** Problem Solving, Teamwork, Adaptabilitas")
        
        st.markdown("### 🏆 Pengalaman")
        st.markdown("""
        <div class="info-card">
            <ul>
                <li><b>Organisasi Sekolah:</b> Aktif mengelola kegiatan siswa.</li>
                <li><b>Proyek Perkenalan:</b> Mengembangkan website interaktif PKKMB ini dengan Streamlit & Spline.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.current_slide == 3:
        st.markdown('<div class="slide-title">🚀 PKKMB & Target Perguruan Tinggi</div>', unsafe_allow_html=True)
        st.markdown('<div class="slide-subtitle">Harapan & Target 4 Tahun Ke Depan</div>', unsafe_allow_html=True)
        
        st.markdown("### 🎯 Target PKKMB")
        st.write("1. Mengenal budaya kampus dan sistem perkuliahan.")
        st.write("2. Membangun jaringan relasi dengan sesama mahasiswa baru.")

        st.markdown("### 📌 Target Perkuliahan")
        st.markdown("""
        <div class="info-card">
            <b>1. Akademik:</b> Mempertahankan prestasi dan lulus tepat waktu.<br>
            <b>2. Organisasi:</b> Aktif di UKM / Himpunan Mahasiswa.<br>
            <b>3. Pengembangan Diri:</b> Mengikuti kompetisi & magang nasional.
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# RIGHT COLUMN: SPLINE paper boat WITH GRADIENT WRAPPER
# ---------------------------------------------------------
with right_col:
    # Embedded iframe inside CSS Linear Gradient wrapper (#67F3CE to #4899EA)
    spline_code_with_gradient = """
    <div style="
        background: linear-gradient(135deg, #67F3CE 0%, #4899EA 100%);
        width: 100%;
        height: 520px;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 10px 25px rgba(72, 153, 234, 0.3);
    ">
        <iframe src='https://my.spline.design/animatedpaperboat-dT4G6ed1AwwVip0rKa99F5OV/' 
                frameborder='0' 
                width='100%' 
                height='100%'>
        </iframe>
    </div>
    """
    
    # Render component
    components.html(spline_code_with_gradient, height=540)