import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Konfigurasi halaman
st.set_page_config(
    page_title="COBIT Framework Management System",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS untuk styling
st.markdown("""
<style>
    /* Global styling untuk semua teks menjadi putih */
    .stApp {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    
    /* Override semua teks menjadi putih */
    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6,
    .stMarkdown li, .stMarkdown span, .stMarkdown div, .stText, .stSelectbox label, .stSlider label, .stTextArea label,
    .stCheckbox label, .stRadio label, .stMetric label, .stMetric div {
        color: #ffffff !important;
    }
    
    .main-header {
        font-size: 3rem;
        color: #ffffff;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }
    .menu-header {
        font-size: 2rem;
        color: #ffffff;
        margin-bottom: 1rem;
        border-bottom: 2px solid #ffffff;
        padding-bottom: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }
    .info-box {
        background-color: #2d2d2d;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 6px solid #4a9eff;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        border: 1px solid #444444;
    }
    .info-box h3 {
        color: #ffffff;
        margin-top: 0;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    .info-box p {
        color: #ffffff;
        line-height: 1.6;
        margin-bottom: 0;
        font-size: 1rem;
    }
    .info-box ul {
        color: #ffffff;
        line-height: 1.8;
        margin-bottom: 0;
    }
    .info-box li {
        margin-bottom: 0.5rem;
        color: #ffffff;
    }
    .info-box strong {
        color: #4a9eff;
        font-weight: 600;
    }
    .metric-card {
        background-color: #2d2d2d;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        text-align: center;
        color: #ffffff;
    }
    
    /* Styling untuk teks yang lebih jelas */
    .positive-finding {
        background-color: #1a4d3a;
        border: 1px solid #28a745;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        color: #ffffff;
        font-weight: 500;
    }
    
    .improvement-area {
        background-color: #4d3a1a;
        border: 1px solid #ffc107;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        color: #ffffff;
        font-weight: 500;
    }
    
    .finding-title {
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
        display: block;
        color: #ffffff;
    }
    
    .finding-item {
        margin: 0.3rem 0;
        padding-left: 1rem;
        line-height: 1.5;
        color: #ffffff;
    }
    
    /* Styling khusus untuk emoji dan teks */
    .emoji-text {
        font-size: 1rem;
        line-height: 1.6;
        color: #ffffff;
        font-weight: 500;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #2d2d2d;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #2d2d2d;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #ffffff;
        background-color: #404040;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #4a9eff;
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header utama
    st.markdown('<h1 class="main-header">🏢 COBIT Framework Management System</h1>', unsafe_allow_html=True)
    
    # Sidebar untuk navigasi
    st.sidebar.title("📋 Menu COBIT")
    st.sidebar.markdown("---")
    
    menu_options = {
        "🏠 Beranda": "home",
        "👔 Dashboard Eksekutif": "executive",
        "📊 EDM - Evaluate, Direct and Monitor": "edm",
        "🎯 APO - Align, Plan and Organize": "apo", 
        "🔧 BAI - Build, Acquire and Implement": "bai",
        "🚀 DSS - Deliver, Service and Support": "dss",
        "📈 MEA - Monitor, Evaluate and Assess": "mea"
    }
    
    selected_menu = st.sidebar.selectbox("Pilih Menu:", list(menu_options.keys()))
    
    # Informasi tentang COBIT
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### ℹ️ Tentang COBIT
    COBIT (Control Objectives for Information and Related Technologies) adalah framework untuk tata kelola dan manajemen TI perusahaan.
    """)
    
    # Routing berdasarkan menu yang dipilih
    menu_key = menu_options[selected_menu]
    
    if menu_key == "home":
        show_home()
    elif menu_key == "executive":
        show_executive_dashboard()
    elif menu_key == "edm":
        show_edm()
    elif menu_key == "apo":
        show_apo()
    elif menu_key == "bai":
        show_bai()
    elif menu_key == "dss":
        show_dss()
    elif menu_key == "mea":
        show_mea()

def show_home():
    """Halaman beranda dengan overview COBIT"""
    st.markdown('<h2 class="menu-header">🏠 Selamat Datang di COBIT Management System</h2>', unsafe_allow_html=True)
    
    # Overview COBIT
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h3>🎯 Apa itu COBIT?</h3>
        <p>COBIT adalah framework komprehensif yang membantu perusahaan mencapai tujuan mereka untuk tata kelola dan manajemen TI perusahaan.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
        <h3>🔧 5 Domain Utama COBIT</h3>
        <ul>
        <li><strong>EDM:</strong> Evaluasi, Pengarahan dan Pemantauan</li>
        <li><strong>APO:</strong> Penyelarasan, Perencanaan dan Pengorganisasian</li>
        <li><strong>BAI:</strong> Pembangunan, Akuisisi dan Implementasi</li>
        <li><strong>DSS:</strong> Penyampaian, Layanan dan Dukungan</li>
        <li><strong>MEA:</strong> Pemantauan, Evaluasi dan Penilaian</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Grafik distribusi domain
        domains = ['EDM', 'APO', 'BAI', 'DSS', 'MEA']
        processes = [5, 13, 10, 6, 3]
        
        fig = px.pie(values=processes, names=domains, title="Distribusi Proses per Domain COBIT")
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
        
        # Metrics cards
        col2_1, col2_2 = st.columns(2)
        with col2_1:
            st.metric("Total Domain", "5", "100%")
        with col2_2:
            st.metric("Total Proses", "37", "Lengkap")

def show_edm():
    """Menu EDM - Evaluate, Direct and Monitor dengan Subdomain Lengkap"""
    st.markdown('<h2 class="menu-header">📊 EDM - Evaluate, Direct and Monitor</h2>', unsafe_allow_html=True)
    st.markdown("**Evaluasi, Pengarahan dan Pemantauan Tata Kelola TI**")
    
    # Tab untuk subdomain EDM
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["EDM01", "EDM02", "EDM03", "EDM04", "EDM05"])
    
    with tab1:
        st.subheader("EDM01 - Memastikan Penetapan dan Pemeliharaan Framework Tata Kelola")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="info-box">
            <h3>🎯 Tujuan EDM01</h3>
            <p>Menyediakan pendekatan yang konsisten dan terintegrasi untuk memenuhi persyaratan tata kelola.</p>
            <ul>
            <li>Penetapan framework tata kelola TI</li>
            <li>Definisi struktur organisasi TI</li>
            <li>Penetapan peran dan tanggung jawab</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            maturity_edm01 = st.slider("Kematangan EDM01 (1-5)", 1, 5, 3, key="edm01_maturity")
            audit_notes_edm01 = st.text_area("Catatan Audit EDM01", key="edm01_notes")
        
        with col2:
            st.markdown("### ✅ Checklist EDM01")
            edm01_items = [
                "Framework tata kelola TI sudah ditetapkan",
                "Struktur organisasi TI terdefinisi",
                "Peran dan tanggung jawab jelas",
                "Kebijakan TI sudah ada",
                "Prosedur tata kelola terdokumentasi"
            ]
            
            edm01_compliance = 0
            for i, item in enumerate(edm01_items):
                if st.checkbox(item, key=f"edm01_check_{i}"):
                    edm01_compliance += 1
            
            compliance_pct = (edm01_compliance / len(edm01_items)) * 100
            st.metric("Kepatuhan EDM01", f"{compliance_pct:.0f}%")
            st.progress(compliance_pct / 100)
    
    with tab2:
        st.subheader("EDM02 - Memastikan Penyampaian Manfaat")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="info-box">
            <h3>🎯 Tujuan EDM02</h3>
            <p>Mengoptimalkan pencapaian nilai dari investasi TI dan portofolio layanan.</p>
            <ul>
            <li>Evaluasi proposal investasi TI</li>
            <li>Monitoring realisasi manfaat</li>
            <li>Optimalisasi portofolio TI</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            maturity_edm02 = st.slider("Kematangan EDM02 (1-5)", 1, 5, 3, key="edm02_maturity")
            audit_notes_edm02 = st.text_area("Catatan Audit EDM02", key="edm02_notes")
        
        with col2:
            st.markdown("### ✅ Checklist EDM02")
            edm02_items = [
                "Proses evaluasi investasi TI ada",
                "Business case untuk proyek TI",
                "Monitoring realisasi manfaat",
                "Portfolio management TI",
                "ROI measurement tersedia"
            ]
            
            edm02_compliance = 0
            for i, item in enumerate(edm02_items):
                if st.checkbox(item, key=f"edm02_check_{i}"):
                    edm02_compliance += 1
            
            compliance_pct = (edm02_compliance / len(edm02_items)) * 100
            st.metric("Kepatuhan EDM02", f"{compliance_pct:.0f}%")
            st.progress(compliance_pct / 100)
    
    with tab3:
        st.subheader("EDM03 - Memastikan Optimalisasi Risiko")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="info-box">
            <h3>🎯 Tujuan EDM03</h3>
            <p>Memastikan bahwa risiko TI tidak melebihi toleransi risiko organisasi.</p>
            <ul>
            <li>Penetapan toleransi risiko TI</li>
            <li>Monitoring profil risiko TI</li>
            <li>Mitigasi risiko yang efektif</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            maturity_edm03 = st.slider("Kematangan EDM03 (1-5)", 1, 5, 3, key="edm03_maturity")
            audit_notes_edm03 = st.text_area("Catatan Audit EDM03", key="edm03_notes")
        
        with col2:
            st.markdown("### ✅ Checklist EDM03")
            edm03_items = [
                "Risk appetite TI sudah ditetapkan",
                "Risk assessment rutin dilakukan",
                "Risk register TI tersedia",
                "Mitigasi risiko terdokumentasi",
                "Monitoring risiko berkelanjutan"
            ]
            
            edm03_compliance = 0
            for i, item in enumerate(edm03_items):
                if st.checkbox(item, key=f"edm03_check_{i}"):
                    edm03_compliance += 1
            
            compliance_pct = (edm03_compliance / len(edm03_items)) * 100
            st.metric("Kepatuhan EDM03", f"{compliance_pct:.0f}%")
            st.progress(compliance_pct / 100)
    
    with tab4:
        st.subheader("EDM04 - Memastikan Optimalisasi Sumber Daya")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="info-box">
            <h3>🎯 Tujuan EDM04</h3>
            <p>Memastikan bahwa kapabilitas TI yang memadai tersedia untuk mendukung tujuan organisasi.</p>
            <ul>
            <li>Perencanaan kapasitas TI</li>
            <li>Optimalisasi penggunaan sumber daya</li>
            <li>Manajemen kinerja TI</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            maturity_edm04 = st.slider("Kematangan EDM04 (1-5)", 1, 5, 3, key="edm04_maturity")
            audit_notes_edm04 = st.text_area("Catatan Audit EDM04", key="edm04_notes")
        
        with col2:
            st.markdown("### ✅ Checklist EDM04")
            edm04_items = [
                "Capacity planning TI tersedia",
                "Resource optimization dilakukan",
                "Performance monitoring aktif",
                "Budget allocation yang efektif",
                "Skill gap analysis rutin"
            ]
            
            edm04_compliance = 0
            for i, item in enumerate(edm04_items):
                if st.checkbox(item, key=f"edm04_check_{i}"):
                    edm04_compliance += 1
            
            compliance_pct = (edm04_compliance / len(edm04_items)) * 100
            st.metric("Kepatuhan EDM04", f"{compliance_pct:.0f}%")
            st.progress(compliance_pct / 100)
    
    with tab5:
        st.subheader("EDM05 - Memastikan Transparansi Stakeholder")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="info-box">
            <h3>🎯 Tujuan EDM05</h3>
            <p>Memastikan bahwa pelaporan TI memberikan transparansi yang memadai kepada stakeholder.</p>
            <ul>
            <li>Pelaporan kinerja TI yang akurat</li>
            <li>Komunikasi yang efektif dengan stakeholder</li>
            <li>Transparansi dalam pengambilan keputusan</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            maturity_edm05 = st.slider("Kematangan EDM05 (1-5)", 1, 5, 3, key="edm05_maturity")
            audit_notes_edm05 = st.text_area("Catatan Audit EDM05", key="edm05_notes")
        
        with col2:
            st.markdown("### ✅ Checklist EDM05")
            edm05_items = [
                "Dashboard TI untuk stakeholder",
                "Laporan kinerja TI rutin",
                "Komunikasi risiko yang jelas",
                "Transparansi dalam investasi TI",
                "Feedback mechanism tersedia"
            ]
            
            edm05_compliance = 0
            for i, item in enumerate(edm05_items):
                if st.checkbox(item, key=f"edm05_check_{i}"):
                    edm05_compliance += 1
            
            compliance_pct = (edm05_compliance / len(edm05_items)) * 100
            st.metric("Kepatuhan EDM05", f"{compliance_pct:.0f}%")
            st.progress(compliance_pct / 100)

def show_apo():
    """Menu APO - Align, Plan and Organize dengan Subdomain Lengkap"""
    st.markdown('<h2 class="menu-header">🎯 APO - Align, Plan and Organize</h2>', unsafe_allow_html=True)
    st.markdown("**Penyelarasan, Perencanaan dan Pengorganisasian TI**")
    
    # Tab untuk subdomain APO (dikelompokkan untuk efisiensi)
    tab1, tab2, tab3, tab4 = st.tabs(["APO01-03", "APO04-06", "APO07-09", "APO10-13"])
    
    with tab1:
        st.markdown("### APO01-03: Framework & Strategi")
        
        # APO01
        with st.expander("APO01 - Mengelola Framework Manajemen TI"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Menyediakan pendekatan yang konsisten untuk manajemen TI")
                maturity_apo01 = st.slider("Kematangan APO01", 1, 5, 3, key="apo01_maturity")
                audit_notes_apo01 = st.text_area("Catatan Audit APO01", key="apo01_notes")
            with col2:
                apo01_items = ["Framework manajemen TI", "Struktur organisasi", "Peran & tanggung jawab"]
                apo01_compliance = sum([st.checkbox(item, key=f"apo01_{i}") for i, item in enumerate(apo01_items)])
                st.metric("Kepatuhan APO01", f"{(apo01_compliance/len(apo01_items)*100):.0f}%")
        
        # APO02
        with st.expander("APO02 - Mengelola Strategi"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Menyediakan visi strategis TI yang selaras dengan bisnis")
                maturity_apo02 = st.slider("Kematangan APO02", 1, 5, 3, key="apo02_maturity")
                audit_notes_apo02 = st.text_area("Catatan Audit APO02", key="apo02_notes")
            with col2:
                apo02_items = ["Strategi TI", "Roadmap TI", "Alignment bisnis-TI"]
                apo02_compliance = sum([st.checkbox(item, key=f"apo02_{i}") for i, item in enumerate(apo02_items)])
                st.metric("Kepatuhan APO02", f"{(apo02_compliance/len(apo02_items)*100):.0f}%")
        
        # APO03
        with st.expander("APO03 - Mengelola Arsitektur Enterprise"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Menyediakan arsitektur yang konsisten dan terintegrasi")
                maturity_apo03 = st.slider("Kematangan APO03", 1, 5, 3, key="apo03_maturity")
                audit_notes_apo03 = st.text_area("Catatan Audit APO03", key="apo03_notes")
            with col2:
                apo03_items = ["Arsitektur enterprise", "Standar teknologi", "Governance arsitektur"]
                apo03_compliance = sum([st.checkbox(item, key=f"apo03_{i}") for i, item in enumerate(apo03_items)])
                st.metric("Kepatuhan APO03", f"{(apo03_compliance/len(apo03_items)*100):.0f}%")
    
    with tab2:
        st.markdown("### APO04-06: Inovasi & Portfolio")
        
        # APO04
        with st.expander("APO04 - Mengelola Inovasi"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memelihara kesadaran akan teknologi baru dan inovasi")
                maturity_apo04 = st.slider("Kematangan APO04", 1, 5, 3, key="apo04_maturity")
                audit_notes_apo04 = st.text_area("Catatan Audit APO04", key="apo04_notes")
            with col2:
                apo04_items = ["Monitoring teknologi baru", "Evaluasi inovasi", "Implementasi teknologi"]
                apo04_compliance = sum([st.checkbox(item, key=f"apo04_{i}") for i, item in enumerate(apo04_items)])
                st.metric("Kepatuhan APO04", f"{(apo04_compliance/len(apo04_items)*100):.0f}%")
        
        # APO05
        with st.expander("APO05 - Mengelola Portfolio"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Mengelola portfolio investasi TI untuk mencapai tujuan strategis")
                maturity_apo05 = st.slider("Kematangan APO05", 1, 5, 3, key="apo05_maturity")
                audit_notes_apo05 = st.text_area("Catatan Audit APO05", key="apo05_notes")
            with col2:
                apo05_items = ["Portfolio management", "Prioritas investasi", "Resource allocation"]
                apo05_compliance = sum([st.checkbox(item, key=f"apo05_{i}") for i, item in enumerate(apo05_items)])
                st.metric("Kepatuhan APO05", f"{(apo05_compliance/len(apo05_items)*100):.0f}%")
        
        # APO06
        with st.expander("APO06 - Mengelola Budget dan Biaya"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Mengelola biaya TI sesuai dengan strategi dan anggaran")
                maturity_apo06 = st.slider("Kematangan APO06", 1, 5, 3, key="apo06_maturity")
                audit_notes_apo06 = st.text_area("Catatan Audit APO06", key="apo06_notes")
            with col2:
                apo06_items = ["Budget planning", "Cost management", "Financial reporting"]
                apo06_compliance = sum([st.checkbox(item, key=f"apo06_{i}") for i, item in enumerate(apo06_items)])
                st.metric("Kepatuhan APO06", f"{(apo06_compliance/len(apo06_items)*100):.0f}%")
    
    with tab3:
        st.markdown("### APO07-09: SDM & Hubungan")
        
        # APO07
        with st.expander("APO07 - Mengelola Sumber Daya Manusia"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan SDM TI yang kompeten untuk mendukung tujuan organisasi")
                maturity_apo07 = st.slider("Kematangan APO07", 1, 5, 3, key="apo07_maturity")
                audit_notes_apo07 = st.text_area("Catatan Audit APO07", key="apo07_notes")
            with col2:
                apo07_items = ["Perencanaan SDM", "Pengembangan kompetensi", "Performance management"]
                apo07_compliance = sum([st.checkbox(item, key=f"apo07_{i}") for i, item in enumerate(apo07_items)])
                st.metric("Kepatuhan APO07", f"{(apo07_compliance/len(apo07_items)*100):.0f}%")
        
        # APO08
        with st.expander("APO08 - Mengelola Hubungan"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Mengelola hubungan antara bisnis dan TI")
                maturity_apo08 = st.slider("Kematangan APO08", 1, 5, 3, key="apo08_maturity")
                audit_notes_apo08 = st.text_area("Catatan Audit APO08", key="apo08_notes")
            with col2:
                apo08_items = ["Business relationship", "Komunikasi stakeholder", "Feedback mechanism"]
                apo08_compliance = sum([st.checkbox(item, key=f"apo08_{i}") for i, item in enumerate(apo08_items)])
                st.metric("Kepatuhan APO08", f"{(apo08_compliance/len(apo08_items)*100):.0f}%")
        
        # APO09
        with st.expander("APO09 - Mengelola Perjanjian Layanan"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Menyelaraskan layanan TI dengan kebutuhan bisnis")
                maturity_apo09 = st.slider("Kematangan APO09", 1, 5, 3, key="apo09_maturity")
                audit_notes_apo09 = st.text_area("Catatan Audit APO09", key="apo09_notes")
            with col2:
                apo09_items = ["Service agreements", "SLA management", "Service catalog"]
                apo09_compliance = sum([st.checkbox(item, key=f"apo09_{i}") for i, item in enumerate(apo09_items)])
                st.metric("Kepatuhan APO09", f"{(apo09_compliance/len(apo09_items)*100):.0f}%")
    
    with tab4:
        st.markdown("### APO10-13: Vendor & Kualitas")
        
        # APO10
        with st.expander("APO10 - Mengelola Supplier"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan layanan supplier memenuhi kebutuhan organisasi")
                maturity_apo10 = st.slider("Kematangan APO10", 1, 5, 3, key="apo10_maturity")
                audit_notes_apo10 = st.text_area("Catatan Audit APO10", key="apo10_notes")
            with col2:
                apo10_items = ["Supplier selection", "Contract management", "Performance monitoring"]
                apo10_compliance = sum([st.checkbox(item, key=f"apo10_{i}") for i, item in enumerate(apo10_items)])
                st.metric("Kepatuhan APO10", f"{(apo10_compliance/len(apo10_items)*100):.0f}%")
        
        # APO11
        with st.expander("APO11 - Mengelola Kualitas"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan TI memenuhi persyaratan kualitas")
                maturity_apo11 = st.slider("Kematangan APO11", 1, 5, 3, key="apo11_maturity")
                audit_notes_apo11 = st.text_area("Catatan Audit APO11", key="apo11_notes")
            with col2:
                apo11_items = ["Quality standards", "Quality assurance", "Continuous improvement"]
                apo11_compliance = sum([st.checkbox(item, key=f"apo11_{i}") for i, item in enumerate(apo11_items)])
                st.metric("Kepatuhan APO11", f"{(apo11_compliance/len(apo11_items)*100):.0f}%")
        
        # APO12
        with st.expander("APO12 - Mengelola Risiko"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Mengintegrasikan manajemen risiko TI dengan risiko enterprise")
                maturity_apo12 = st.slider("Kematangan APO12", 1, 5, 3, key="apo12_maturity")
                audit_notes_apo12 = st.text_area("Catatan Audit APO12", key="apo12_notes")
            with col2:
                apo12_items = ["Risk assessment", "Risk mitigation", "Risk monitoring"]
                apo12_compliance = sum([st.checkbox(item, key=f"apo12_{i}") for i, item in enumerate(apo12_items)])
                st.metric("Kepatuhan APO12", f"{(apo12_compliance/len(apo12_items)*100):.0f}%")
        
        # APO13
        with st.expander("APO13 - Mengelola Keamanan"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan keamanan informasi sesuai dengan strategi organisasi")
                maturity_apo13 = st.slider("Kematangan APO13", 1, 5, 3, key="apo13_maturity")
                audit_notes_apo13 = st.text_area("Catatan Audit APO13", key="apo13_notes")
            with col2:
                apo13_items = ["Security strategy", "Security policies", "Security awareness"]
                apo13_compliance = sum([st.checkbox(item, key=f"apo13_{i}") for i, item in enumerate(apo13_items)])
                st.metric("Kepatuhan APO13", f"{(apo13_compliance/len(apo13_items)*100):.0f}%")

def show_bai():
    """Menu BAI - Build, Acquire and Implement dengan Subdomain Lengkap"""
    st.markdown('<h2 class="menu-header">🔧 BAI - Build, Acquire and Implement</h2>', unsafe_allow_html=True)
    st.markdown("**Pembangunan, Akuisisi dan Implementasi TI**")
    
    # Tab untuk subdomain BAI (dikelompokkan untuk efisiensi)
    tab1, tab2, tab3 = st.tabs(["BAI01-04", "BAI05-08", "BAI09-11"])
    
    with tab1:
        st.markdown("### BAI01-04: Program & Kebutuhan")
        
        # BAI01
        with st.expander("BAI01 - Mengelola Program dan Proyek"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan program dan proyek TI dikelola dengan efektif")
                maturity_bai01 = st.slider("Kematangan BAI01", 1, 5, 3, key="bai01_maturity")
                audit_notes_bai01 = st.text_area("Catatan Audit BAI01", key="bai01_notes")
            with col2:
                bai01_items = ["Program management", "Project management", "Resource allocation"]
                bai01_compliance = sum([st.checkbox(item, key=f"bai01_{i}") for i, item in enumerate(bai01_items)])
                st.metric("Kepatuhan BAI01", f"{(bai01_compliance/len(bai01_items)*100):.0f}%")
        
        # BAI02
        with st.expander("BAI02 - Mengelola Definisi Kebutuhan"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan kebutuhan bisnis didefinisikan dengan jelas")
                maturity_bai02 = st.slider("Kematangan BAI02", 1, 5, 3, key="bai02_maturity")
                audit_notes_bai02 = st.text_area("Catatan Audit BAI02", key="bai02_notes")
            with col2:
                bai02_items = ["Requirements definition", "Business analysis", "Stakeholder approval"]
                bai02_compliance = sum([st.checkbox(item, key=f"bai02_{i}") for i, item in enumerate(bai02_items)])
                st.metric("Kepatuhan BAI02", f"{(bai02_compliance/len(bai02_items)*100):.0f}%")
        
        # BAI03
        with st.expander("BAI03 - Mengelola Identifikasi dan Pembangunan Solusi"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan solusi TI diidentifikasi dan dibangun sesuai kebutuhan")
                maturity_bai03 = st.slider("Kematangan BAI03", 1, 5, 3, key="bai03_maturity")
                audit_notes_bai03 = st.text_area("Catatan Audit BAI03", key="bai03_notes")
            with col2:
                bai03_items = ["Solution design", "Development methodology", "Quality assurance"]
                bai03_compliance = sum([st.checkbox(item, key=f"bai03_{i}") for i, item in enumerate(bai03_items)])
                st.metric("Kepatuhan BAI03", f"{(bai03_compliance/len(bai03_items)*100):.0f}%")
        
        # BAI04
        with st.expander("BAI04 - Mengelola Ketersediaan dan Kapasitas"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan ketersediaan dan kapasitas TI memenuhi kebutuhan")
                maturity_bai04 = st.slider("Kematangan BAI04", 1, 5, 3, key="bai04_maturity")
                audit_notes_bai04 = st.text_area("Catatan Audit BAI04", key="bai04_notes")
            with col2:
                bai04_items = ["Availability management", "Capacity planning", "Performance monitoring"]
                bai04_compliance = sum([st.checkbox(item, key=f"bai04_{i}") for i, item in enumerate(bai04_items)])
                st.metric("Kepatuhan BAI04", f"{(bai04_compliance/len(bai04_items)*100):.0f}%")
    
    with tab2:
        st.markdown("### BAI05-08: Perubahan & Pengetahuan")
        
        # BAI05
        with st.expander("BAI05 - Mengelola Perubahan Organisasi"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan perubahan organisasi dikelola dengan efektif")
                maturity_bai05 = st.slider("Kematangan BAI05", 1, 5, 3, key="bai05_maturity")
                audit_notes_bai05 = st.text_area("Catatan Audit BAI05", key="bai05_notes")
            with col2:
                bai05_items = ["Change management", "Training programs", "Communication strategy"]
                bai05_compliance = sum([st.checkbox(item, key=f"bai05_{i}") for i, item in enumerate(bai05_items)])
                st.metric("Kepatuhan BAI05", f"{(bai05_compliance/len(bai05_items)*100):.0f}%")
        
        # BAI06
        with st.expander("BAI06 - Mengelola Perubahan"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan semua perubahan TI dikelola dengan terkontrol")
                maturity_bai06 = st.slider("Kematangan BAI06", 1, 5, 3, key="bai06_maturity")
                audit_notes_bai06 = st.text_area("Catatan Audit BAI06", key="bai06_notes")
            with col2:
                bai06_items = ["Change control", "Change approval", "Change implementation"]
                bai06_compliance = sum([st.checkbox(item, key=f"bai06_{i}") for i, item in enumerate(bai06_items)])
                st.metric("Kepatuhan BAI06", f"{(bai06_compliance/len(bai06_items)*100):.0f}%")
        
        # BAI07
        with st.expander("BAI07 - Mengelola Penerimaan Perubahan dan Transisi"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan perubahan diterima dan ditransisikan dengan baik")
                maturity_bai07 = st.slider("Kematangan BAI07", 1, 5, 3, key="bai07_maturity")
                audit_notes_bai07 = st.text_area("Catatan Audit BAI07", key="bai07_notes")
            with col2:
                bai07_items = ["Change acceptance", "Transition planning", "Go-live support"]
                bai07_compliance = sum([st.checkbox(item, key=f"bai07_{i}") for i, item in enumerate(bai07_items)])
                st.metric("Kepatuhan BAI07", f"{(bai07_compliance/len(bai07_items)*100):.0f}%")
        
        # BAI08
        with st.expander("BAI08 - Mengelola Pengetahuan"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan pengetahuan TI dikelola dan dibagikan dengan efektif")
                maturity_bai08 = st.slider("Kematangan BAI08", 1, 5, 3, key="bai08_maturity")
                audit_notes_bai08 = st.text_area("Catatan Audit BAI08", key="bai08_notes")
            with col2:
                bai08_items = ["Knowledge management", "Documentation", "Knowledge sharing"]
                bai08_compliance = sum([st.checkbox(item, key=f"bai08_{i}") for i, item in enumerate(bai08_items)])
                st.metric("Kepatuhan BAI08", f"{(bai08_compliance/len(bai08_items)*100):.0f}%")
    
    with tab3:
        st.markdown("### BAI09-11: Aset & Konfigurasi")
        
        # BAI09
        with st.expander("BAI09 - Mengelola Aset"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan aset TI dikelola sepanjang siklus hidupnya")
                maturity_bai09 = st.slider("Kematangan BAI09", 1, 5, 3, key="bai09_maturity")
                audit_notes_bai09 = st.text_area("Catatan Audit BAI09", key="bai09_notes")
            with col2:
                bai09_items = ["Asset inventory", "Asset lifecycle", "Asset disposal"]
                bai09_compliance = sum([st.checkbox(item, key=f"bai09_{i}") for i, item in enumerate(bai09_items)])
                st.metric("Kepatuhan BAI09", f"{(bai09_compliance/len(bai09_items)*100):.0f}%")
        
        # BAI10
        with st.expander("BAI10 - Mengelola Konfigurasi"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan konfigurasi TI dikelola dengan akurat")
                maturity_bai10 = st.slider("Kematangan BAI10", 1, 5, 3, key="bai10_maturity")
                audit_notes_bai10 = st.text_area("Catatan Audit BAI10", key="bai10_notes")
            with col2:
                bai10_items = ["Configuration management", "Configuration baseline", "Configuration audit"]
                bai10_compliance = sum([st.checkbox(item, key=f"bai10_{i}") for i, item in enumerate(bai10_items)])
                st.metric("Kepatuhan BAI10", f"{(bai10_compliance/len(bai10_items)*100):.0f}%")
        
        # BAI11
        with st.expander("BAI11 - Mengelola Proyek"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan proyek TI dikelola dengan metodologi yang konsisten")
                maturity_bai11 = st.slider("Kematangan BAI11", 1, 5, 3, key="bai11_maturity")
                audit_notes_bai11 = st.text_area("Catatan Audit BAI11", key="bai11_notes")
            with col2:
                bai11_items = ["Project methodology", "Project governance", "Project delivery"]
                bai11_compliance = sum([st.checkbox(item, key=f"bai11_{i}") for i, item in enumerate(bai11_items)])
                st.metric("Kepatuhan BAI11", f"{(bai11_compliance/len(bai11_items)*100):.0f}%")

def show_dss():
    """Menu DSS - Deliver, Service and Support dengan Subdomain Lengkap"""
    st.markdown('<h2 class="menu-header">🚀 DSS - Deliver, Service and Support</h2>', unsafe_allow_html=True)
    st.markdown("**Penyampaian, Layanan dan Dukungan TI**")
    
    # Tab untuk subdomain DSS (dikelompokkan untuk efisiensi)
    tab1, tab2 = st.tabs(["DSS01-03", "DSS04-06"])
    
    with tab1:
        st.markdown("### DSS01-03: Operasi & Layanan")
        
        # DSS01
        with st.expander("DSS01 - Mengelola Operasi"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan operasi TI berjalan dengan stabil dan efisien")
                maturity_dss01 = st.slider("Kematangan DSS01", 1, 5, 3, key="dss01_maturity")
                audit_notes_dss01 = st.text_area("Catatan Audit DSS01", key="dss01_notes")
            with col2:
                dss01_items = ["Operations procedures", "System monitoring", "Performance management"]
                dss01_compliance = sum([st.checkbox(item, key=f"dss01_{i}") for i, item in enumerate(dss01_items)])
                st.metric("Kepatuhan DSS01", f"{(dss01_compliance/len(dss01_items)*100):.0f}%")
        
        # DSS02
        with st.expander("DSS02 - Mengelola Permintaan Layanan dan Insiden"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan permintaan layanan dan insiden ditangani dengan efektif")
                maturity_dss02 = st.slider("Kematangan DSS02", 1, 5, 3, key="dss02_maturity")
                audit_notes_dss02 = st.text_area("Catatan Audit DSS02", key="dss02_notes")
            with col2:
                dss02_items = ["Service request management", "Incident management", "Service desk"]
                dss02_compliance = sum([st.checkbox(item, key=f"dss02_{i}") for i, item in enumerate(dss02_items)])
                st.metric("Kepatuhan DSS02", f"{(dss02_compliance/len(dss02_items)*100):.0f}%")
        
        # DSS03
        with st.expander("DSS03 - Mengelola Masalah"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan masalah TI diidentifikasi dan diselesaikan dengan efektif")
                maturity_dss03 = st.slider("Kematangan DSS03", 1, 5, 3, key="dss03_maturity")
                audit_notes_dss03 = st.text_area("Catatan Audit DSS03", key="dss03_notes")
            with col2:
                dss03_items = ["Problem identification", "Root cause analysis", "Problem resolution"]
                dss03_compliance = sum([st.checkbox(item, key=f"dss03_{i}") for i, item in enumerate(dss03_items)])
                st.metric("Kepatuhan DSS03", f"{(dss03_compliance/len(dss03_items)*100):.0f}%")
    
    with tab2:
        st.markdown("### DSS04-06: Kontinuitas & Keamanan")
        
        # DSS04
        with st.expander("DSS04 - Mengelola Kontinuitas"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan kontinuitas layanan TI dalam situasi gangguan")
                maturity_dss04 = st.slider("Kematangan DSS04", 1, 5, 3, key="dss04_maturity")
                audit_notes_dss04 = st.text_area("Catatan Audit DSS04", key="dss04_notes")
            with col2:
                dss04_items = ["Business continuity planning", "Disaster recovery", "Backup management"]
                dss04_compliance = sum([st.checkbox(item, key=f"dss04_{i}") for i, item in enumerate(dss04_items)])
                st.metric("Kepatuhan DSS04", f"{(dss04_compliance/len(dss04_items)*100):.0f}%")
        
        # DSS05
        with st.expander("DSS05 - Mengelola Layanan Keamanan"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan keamanan informasi dan sistem TI")
                maturity_dss05 = st.slider("Kematangan DSS05", 1, 5, 3, key="dss05_maturity")
                audit_notes_dss05 = st.text_area("Catatan Audit DSS05", key="dss05_notes")
            with col2:
                dss05_items = ["Security monitoring", "Incident response", "Access management"]
                dss05_compliance = sum([st.checkbox(item, key=f"dss05_{i}") for i, item in enumerate(dss05_items)])
                st.metric("Kepatuhan DSS05", f"{(dss05_compliance/len(dss05_items)*100):.0f}%")
        
        # DSS06
        with st.expander("DSS06 - Mengelola Kontrol Proses Bisnis"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Tujuan:** Memastikan kontrol yang memadai dalam proses bisnis yang didukung TI")
                maturity_dss06 = st.slider("Kematangan DSS06", 1, 5, 3, key="dss06_maturity")
                audit_notes_dss06 = st.text_area("Catatan Audit DSS06", key="dss06_notes")
            with col2:
                dss06_items = ["Business process controls", "Data integrity", "Compliance monitoring"]
                dss06_compliance = sum([st.checkbox(item, key=f"dss06_{i}") for i, item in enumerate(dss06_items)])
                st.metric("Kepatuhan DSS06", f"{(dss06_compliance/len(dss06_items)*100):.0f}%")

def show_mea():
    """Menu MEA - Monitor, Evaluate and Assess dengan Subdomain Lengkap"""
    st.markdown('<h2 class="menu-header">📈 MEA - Monitor, Evaluate and Assess</h2>', unsafe_allow_html=True)
    st.markdown("**Pemantauan, Evaluasi dan Penilaian TI dengan Subdomain Lengkap**")
    
    # Informasi Dasar MEA
    st.markdown("""
    <div class="info-box">
    <h3>🎯 Tujuan Domain MEA</h3>
    <p>Domain MEA berfokus pada pemantauan, evaluasi, dan penilaian TI untuk memastikan kinerja optimal dan kepatuhan.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tab untuk subdomain MEA
    tab1, tab2, tab3 = st.tabs(["MEA01", "MEA02", "MEA03"])
    
    with tab1:
        st.markdown("### 📊 MEA01 - Monitor, Evaluate and Assess Performance and Conformance")
        st.markdown("**Memantau, mengevaluasi dan menilai kinerja serta kesesuaian**")
        
        st.markdown("""
        <div class="info-box">
        <h3>🎯 Tujuan MEA01</h3>
        <p>Menyediakan transparansi kinerja TI dan kesesuaian dengan tujuan bisnis, serta memungkinkan pengambilan keputusan yang tepat.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📝 Penilaian Kematangan MEA01")
            mea01_maturity = st.slider("Tingkat Kematangan MEA01 (1-5)", 1, 5, 3, key="mea01_maturity")
            
            if mea01_maturity == 1:
                interpretation = "🔴 Initial - Monitoring ad-hoc"
            elif mea01_maturity == 2:
                interpretation = "🟡 Managed - Monitoring dasar"
            elif mea01_maturity == 3:
                interpretation = "🟠 Defined - Proses monitoring standar"
            elif mea01_maturity == 4:
                interpretation = "🟢 Quantitatively Managed - Monitoring terukur"
            else:
                interpretation = "🔵 Optimizing - Monitoring optimal"
            
            st.markdown(f"**Status:** {interpretation}")
            
            mea01_notes = st.text_area("Catatan Audit MEA01", placeholder="Masukkan temuan audit untuk MEA01...", key="mea01_notes")
        
        with col2:
            st.markdown("#### 📊 Checklist Audit MEA01")
            
            mea01_items = [
                "Framework monitoring kinerja TI",
                "KPI dan metrik bisnis terdefinisi",
                "Dashboard kinerja real-time",
                "Pelaporan kinerja berkala",
                "Analisis gap kinerja",
                "Tindak lanjut perbaikan"
            ]
            
            mea01_compliance = 0
            for item in mea01_items:
                if st.checkbox(item, key=f"mea01_{item}"):
                    mea01_compliance += 1
            
            mea01_percentage = (mea01_compliance / len(mea01_items)) * 100
            st.metric("Tingkat Kepatuhan MEA01", f"{mea01_percentage:.0f}%")
            st.progress(mea01_percentage / 100)
    
    with tab2:
        st.markdown("### 🔍 MEA02 - Monitor, Evaluate and Assess the System of Internal Control")
        st.markdown("**Memantau, mengevaluasi dan menilai sistem kontrol internal**")
        
        st.markdown("""
        <div class="info-box">
        <h3>🎯 Tujuan MEA02</h3>
        <p>Memastikan sistem kontrol internal TI berfungsi efektif dan memberikan jaminan yang memadai terhadap risiko TI.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📝 Penilaian Kematangan MEA02")
            mea02_maturity = st.slider("Tingkat Kematangan MEA02 (1-5)", 1, 5, 3, key="mea02_maturity")
            
            if mea02_maturity == 1:
                interpretation = "🔴 Initial - Kontrol ad-hoc"
            elif mea02_maturity == 2:
                interpretation = "🟡 Managed - Kontrol dasar"
            elif mea02_maturity == 3:
                interpretation = "🟠 Defined - Kontrol standar"
            elif mea02_maturity == 4:
                interpretation = "🟢 Quantitatively Managed - Kontrol terukur"
            else:
                interpretation = "🔵 Optimizing - Kontrol optimal"
            
            st.markdown(f"**Status:** {interpretation}")
            
            mea02_notes = st.text_area("Catatan Audit MEA02", placeholder="Masukkan temuan audit untuk MEA02...", key="mea02_notes")
        
        with col2:
            st.markdown("#### 📊 Checklist Audit MEA02")
            
            mea02_items = [
                "Framework kontrol internal TI",
                "Monitoring kontrol otomatis",
                "Evaluasi efektivitas kontrol",
                "Pelaporan defisiensi kontrol",
                "Tindak lanjut perbaikan kontrol",
                "Sertifikasi kontrol berkala"
            ]
            
            mea02_compliance = 0
            for item in mea02_items:
                if st.checkbox(item, key=f"mea02_{item}"):
                    mea02_compliance += 1
            
            mea02_percentage = (mea02_compliance / len(mea02_items)) * 100
            st.metric("Tingkat Kepatuhan MEA02", f"{mea02_percentage:.0f}%")
            st.progress(mea02_percentage / 100)
    
    with tab3:
        st.markdown("### ⚖️ MEA03 - Monitor, Evaluate and Assess Compliance with External Requirements")
        st.markdown("**Memantau, mengevaluasi dan menilai kepatuhan terhadap persyaratan eksternal**")
        
        st.markdown("""
        <div class="info-box">
        <h3>🎯 Tujuan MEA03</h3>
        <p>Memastikan kepatuhan TI terhadap hukum, regulasi, dan persyaratan kontraktual yang berlaku.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📝 Penilaian Kematangan MEA03")
            mea03_maturity = st.slider("Tingkat Kematangan MEA03 (1-5)", 1, 5, 3, key="mea03_maturity")
            
            if mea03_maturity == 1:
                interpretation = "🔴 Initial - Kepatuhan reaktif"
            elif mea03_maturity == 2:
                interpretation = "🟡 Managed - Kepatuhan dasar"
            elif mea03_maturity == 3:
                interpretation = "🟠 Defined - Kepatuhan standar"
            elif mea03_maturity == 4:
                interpretation = "🟢 Quantitatively Managed - Kepatuhan terukur"
            else:
                interpretation = "🔵 Optimizing - Kepatuhan proaktif"
            
            st.markdown(f"**Status:** {interpretation}")
            
            mea03_notes = st.text_area("Catatan Audit MEA03", placeholder="Masukkan temuan audit untuk MEA03...", key="mea03_notes")
        
        with col2:
            st.markdown("#### 📊 Checklist Audit MEA03")
            
            mea03_items = [
                "Identifikasi persyaratan eksternal",
                "Monitoring kepatuhan regulasi",
                "Pelaporan kepatuhan berkala",
                "Audit kepatuhan eksternal",
                "Tindak lanjut temuan kepatuhan",
                "Update persyaratan regulasi"
            ]
            
            mea03_compliance = 0
            for item in mea03_items:
                if st.checkbox(item, key=f"mea03_{item}"):
                    mea03_compliance += 1
            
            mea03_percentage = (mea03_compliance / len(mea03_items)) * 100
            st.metric("Tingkat Kepatuhan MEA03", f"{mea03_percentage:.0f}%")
            st.progress(mea03_percentage / 100)

def show_executive_dashboard():
    """Dashboard Eksekutif Sederhana untuk Audit Sistem Informasi"""
    st.markdown('<h2 class="menu-header">👔 Dashboard Audit Sistem Informasi</h2>', unsafe_allow_html=True)
    
    # KPI Sederhana
    st.markdown("### 📊 Indikator Utama Audit")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="🎯 Tingkat Kematangan",
            value="3.2/5.0",
            help="Rata-rata kematangan proses COBIT"
        )
    
    with col2:
        st.metric(
            label="✅ Tingkat Kepatuhan",
            value="87%",
            help="Persentase kepatuhan audit"
        )
    
    with col3:
        st.metric(
            label="⚠️ Risiko TI",
            value="Sedang",
            help="Level risiko sistem informasi"
        )
    
    st.markdown("---")
    
    # Grafik Sederhana
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("### 📈 Kematangan Domain COBIT")
        
        domains = ["EDM", "APO", "BAI", "DSS", "MEA"]
        scores = [3.5, 3.1, 2.8, 3.4, 3.0]
        
        fig = go.Figure(data=[go.Bar(x=domains, y=scores, marker_color='#1f77b4')])
        fig.update_layout(
            title="Skor Kematangan per Domain",
            yaxis_title="Skor (1-5)",
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col_right:
        st.markdown("### ⚠️ Distribusi Risiko")
        
        risk_levels = ["Rendah", "Sedang", "Tinggi"]
        risk_counts = [60, 30, 10]
        
        fig = go.Figure(data=[go.Pie(labels=risk_levels, values=risk_counts)])
        fig.update_layout(title="Tingkat Risiko (%)", height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # Temuan Audit Sederhana
    st.markdown("### 📋 Temuan Audit Utama")
    
    col_finding1, col_finding2 = st.columns(2)
    
    with col_finding1:
        st.markdown("""
        <div class="positive-finding">
        <span class="finding-title">🔍 Temuan Positif:</span>
        <div class="finding-item">✅ Dokumentasi proses sudah baik</div>
        <div class="finding-item">✅ Kontrol akses berfungsi dengan baik</div>
        <div class="finding-item">✅ Backup data rutin dilakukan</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_finding2:
        st.markdown("""
        <div class="improvement-area">
        <span class="finding-title">⚠️ Area Perbaikan:</span>
        <div class="finding-item">🔧 Perlu peningkatan monitoring sistem</div>
        <div class="finding-item">🔧 Training keamanan untuk user</div>
        <div class="finding-item">🔧 Update kebijakan TI</div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()