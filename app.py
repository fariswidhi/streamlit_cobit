import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="COBIT 2019 - Tata Kelola SI Rumah Sakit Digital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #2c5aa0, #1e88e5);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .domain-card {
        background: linear-gradient(135deg, #42a5f5 0%, #1976d2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #2e6da4;
        margin: 0.5rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .metric-card h3 {
        color: #495057 !important;
        margin-bottom: 0.5rem;
        font-size: 1rem;
    }
    
    .metric-card h2 {
        margin: 0.5rem 0;
        font-weight: bold;
    }
    
    .metric-card p {
        color: #6c757d !important;
        margin-top: 0.5rem;
        font-size: 0.9rem;
    }
    
    .stSelectbox > div > div {
        background-color: #f8f9fa;
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3, #54a0ff);
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>🏥 COBIT 2019 - Tata Kelola Sistem Informasi Rumah Sakit Digital</h1>
        <p>Implementasi Framework COBIT untuk Governance dan Management TI Rumah Sakit</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.markdown("### 🏥 Menu Navigasi Rumah Sakit")
    page = st.sidebar.radio(
        "Pilih Domain COBIT:",
        ["Dashboard Rumah Sakit", "EDM - Evaluasi, Pengarahan, dan Pemantauan", "APO - Penjajaran, Perencanaan, dan Pengorganisasian", 
         "BAI - Pengembangan, Akuisisi, dan Implementasi", "DSS - Penyampaian, Layanan, dan Dukungan", 
         "MEA - Pemantauan, Evaluasi, dan Penilaian"]
    )
    
    if page == "Dashboard Rumah Sakit":
        show_dashboard()
    elif page == "EDM - Evaluasi, Pengarahan, dan Pemantauan":
        show_edm()
    elif page == "APO - Penjajaran, Perencanaan, dan Pengorganisasian":
        show_apo()
    elif page == "BAI - Pengembangan, Akuisisi, dan Implementasi":
        show_bai()
    elif page == "DSS - Penyampaian, Layanan, dan Dukungan":
        show_dss()
    elif page == "MEA - Pemantauan, Evaluasi, dan Penilaian":
        show_mea()

def show_dashboard():
    st.markdown("## 📊 Dashboard Eksekutif Rumah Sakit")
    
    # Interactive Assessment Section
    st.markdown("### 🎯 Penilaian Interaktif Maturity Level")
    st.markdown("Silakan berikan penilaian untuk setiap domain berdasarkan kondisi saat ini di rumah sakit Anda:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        edm_score = st.slider("📊 EDM - Evaluasi, Pengarahan, dan Pemantauan", 1, 5, 4, help="1=Initial, 2=Managed, 3=Defined, 4=Quantitatively Managed, 5=Optimizing")
        apo_score = st.slider("📋 APO - Penjajaran, Perencanaan, dan Pengorganisasian", 1, 5, 3, help="Seberapa baik perencanaan TI selaras dengan tujuan RS?")
        bai_score = st.slider("🔧 BAI - Pengembangan, Akuisisi, dan Implementasi", 1, 5, 3, help="Seberapa efektif pengembangan dan implementasi sistem TI?")
    
    with col2:
        dss_score = st.slider("🛠️ DSS - Penyampaian, Layanan, dan Dukungan", 1, 5, 4, help="Seberapa baik layanan TI mendukung operasional RS?")
        mea_score = st.slider("📈 MEA - Pemantauan, Evaluasi, dan Penilaian", 1, 5, 3, help="Seberapa efektif monitoring dan evaluasi kinerja TI?")
    
    # Calculate average
    avg_maturity = (edm_score + apo_score + bai_score + dss_score + mea_score) / 5
    
    # Display calculated metrics based on user input
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        maturity_color = "#28a745" if avg_maturity >= 4 else "#ffc107" if avg_maturity >= 3 else "#dc3545"
        maturity_level = "Optimizing" if avg_maturity >= 4.5 else "Managed" if avg_maturity >= 3.5 else "Defined" if avg_maturity >= 2.5 else "Initial"
        st.markdown(f"""
        <div class="metric-card">
            <h3>🏥 Maturity TI RS</h3>
            <h2 style="color: {maturity_color};">{avg_maturity:.1f}/5</h2>
            <p>{maturity_level}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        uptime_target = 99.0 + (dss_score * 0.2)  # Higher DSS score = better uptime
        uptime_color = "#28a745" if uptime_target >= 99 else "#ffc107"
        st.markdown(f"""
        <div class="metric-card">
            <h3>📋 EMR Uptime</h3>
            <h2 style="color: {uptime_color};">{uptime_target:.1f}%</h2>
            <p>Target: >99%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        security_level = "Sangat Aman" if edm_score >= 4 else "Aman" if edm_score >= 3 else "Perlu Perbaikan"
        security_color = "#28a745" if edm_score >= 4 else "#ffc107" if edm_score >= 3 else "#dc3545"
        st.markdown(f"""
        <div class="metric-card">
            <h3>🔒 Keamanan Data</h3>
            <h2 style="color: {security_color};">{security_level}</h2>
            <p>Compliance HIPAA</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        satisfaction = 3.0 + (avg_maturity * 0.4)  # Higher maturity = higher satisfaction
        st.markdown(f"""
        <div class="metric-card">
            <h3>👥 Kepuasan User</h3>
            <h2 style="color: #1976d2;">{satisfaction:.1f}/5</h2>
            <p>Dokter & Staff</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Interactive Domain maturity chart that updates based on user input
    st.markdown("### 📈 Tingkat Kematangan Domain TI Rumah Sakit (Berdasarkan Penilaian Anda)")
    
    domains = ['EDM\n(Tata Kelola)', 'APO\n(Perencanaan)', 'BAI\n(Implementasi)', 'DSS\n(Layanan)', 'MEA\n(Evaluasi)']
    maturity_scores = [edm_score, apo_score, bai_score, dss_score, mea_score]
    
    fig = px.bar(
        x=domains, 
        y=maturity_scores,
        title="Tingkat Kematangan Domain COBIT untuk Sistem Informasi RS",
        color=maturity_scores,
        color_continuous_scale="RdYlGn",
        labels={'x': 'Domain COBIT', 'y': 'Tingkat Kematangan (1-5)'},
        range_y=[0, 5]
    )
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Recommendations based on scores
    st.markdown("### 💡 Rekomendasi Berdasarkan Penilaian Anda")
    
    recommendations = []
    if edm_score < 3:
        recommendations.append("🔴 **EDM**: Perkuat kerangka tata kelola TI dan keterlibatan stakeholder")
    if apo_score < 3:
        recommendations.append("🔴 **APO**: Tingkatkan perencanaan strategis dan manajemen portofolio TI")
    if bai_score < 3:
        recommendations.append("🔴 **BAI**: Perbaiki proses pengembangan dan implementasi sistem")
    if dss_score < 3:
        recommendations.append("🔴 **DSS**: Optimalkan layanan operasional dan dukungan TI")
    if mea_score < 3:
        recommendations.append("🔴 **MEA**: Perkuat monitoring dan evaluasi kinerja TI")
    
    if not recommendations:
        st.success("🎉 Excellent! Semua domain memiliki maturity level yang baik (≥3). Fokus pada optimisasi berkelanjutan.")
    else:
        for rec in recommendations:
            st.warning(rec)
    
    # Priority Action Items
    st.markdown("### 🎯 Action Items Prioritas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #e8f5e8; padding: 1rem; border-radius: 10px; border-left: 4px solid #28a745;">
            <h4 style="color: #155724;">✅ Pencapaian Positif</h4>
            <ul style="color: #155724;">
                <li>EMR terintegrasi dengan baik antar unit</li>
                <li>Sistem backup data pasien berjalan optimal</li>
                <li>Keamanan data pasien sesuai standar</li>
                <li>Uptime sistem mencapai target 99%+</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #fff3cd; padding: 1rem; border-radius: 10px; border-left: 4px solid #ffc107;">
            <h4 style="color: #856404;">⚠️ Area yang Perlu Diperbaiki</h4>
            <ul style="color: #856404;">
                <li>Perlu pelatihan EMR untuk staff baru</li>
                <li>Optimasi kecepatan akses sistem di jam sibuk</li>
                <li>Integrasi sistem farmasi dengan EMR</li>
                <li>Monitoring real-time performa server</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Save Assessment Button
    if st.button("💾 Simpan Penilaian", type="primary"):
        st.success(f"✅ Penilaian tersimpan! Rata-rata Maturity Level: {avg_maturity:.1f}/5")
        st.balloons()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🏥 Maturity TI RS</h3>
            <h2 style="color: #1976d2;">3.4/5</h2>
            <p>Managed Level</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>📋 EMR Uptime</h3>
            <h2 style="color: #28a745;">99.2%</h2>
            <p>Target: >99%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🔒 Keamanan Data</h3>
            <h2 style="color: #28a745;">Aman</h2>
            <p>Compliance HIPAA</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>👥 Kepuasan User</h3>
            <h2 style="color: #1976d2;">4.2/5</h2>
            <p>Dokter & Staff</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Domain maturity chart
    st.markdown("### 📈 Tingkat Kematangan Domain TI Rumah Sakit")
    
    domains = ['EDM\n(Tata Kelola)', 'APO\n(Perencanaan)', 'BAI\n(Implementasi)', 'DSS\n(Layanan)', 'MEA\n(Evaluasi)']
    maturity_scores = [3.6, 3.4, 3.2, 3.8, 3.3]
    
    fig = px.bar(
        x=domains, 
        y=maturity_scores,
        title="Tingkat Kematangan Domain COBIT untuk Sistem Informasi RS",
        color=maturity_scores,
        color_continuous_scale="Blues",
        labels={'x': 'Domain COBIT', 'y': 'Tingkat Kematangan (1-5)'}
    )
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Recent audit findings
    st.markdown("### 📋 Temuan Audit Sistem Informasi RS Terbaru")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #e8f5e8; padding: 1rem; border-radius: 10px; border-left: 4px solid #28a745;">
            <h4 style="color: #155724;">✅ Pencapaian Positif</h4>
            <ul style="color: #155724;">
                <li>EMR terintegrasi dengan baik antar unit</li>
                <li>Sistem backup data pasien berjalan optimal</li>
                <li>Keamanan data pasien sesuai standar</li>
                <li>Uptime sistem mencapai target 99%+</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #fff3cd; padding: 1rem; border-radius: 10px; border-left: 4px solid #ffc107;">
            <h4 style="color: #856404;">⚠️ Area yang Perlu Diperbaiki</h4>
            <ul style="color: #856404;">
                <li>Perlu pelatihan EMR untuk staff baru</li>
                <li>Optimasi kecepatan akses sistem di jam sibuk</li>
                <li>Integrasi sistem farmasi dengan EMR</li>
                <li>Monitoring real-time performa server</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_edm():
    st.markdown("""
    <div class="domain-card">
        <h2>📊 EDM - Evaluasi, Pengarahan, dan Pemantauan</h2>
        <p>Domain EDM memastikan kebutuhan stakeholder rumah sakit dievaluasi untuk menentukan tujuan yang seimbang dalam tata kelola TI rumah sakit.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Domain EDM berfokus pada evaluasi kebutuhan stakeholder rumah sakit, menentukan tujuan yang seimbang 
    untuk sistem informasi RS, memberikan arahan melalui prioritas dan pengambilan keputusan, 
    serta memantau kinerja dan kepatuhan terhadap tujuan tata kelola TI rumah sakit.
    """)
    
    # Only keep the dynamic assessment tab
    st.markdown("### 🎯 Penilaian Maturity Level EDM")
    st.markdown("Berikan penilaian untuk setiap proses EDM berdasarkan kondisi saat ini:")
    
    # EDM01 Assessment
    st.markdown("#### EDM01 - Menetapkan Kerangka Tata Kelola TI RS")
    edm01_score = st.slider("Tingkat implementasi kerangka tata kelola TI", 1, 5, 4, key="edm01", 
                            help="1=Tidak ada, 2=Ad-hoc, 3=Terdefinisi, 4=Terkelola, 5=Optimal")
    
    edm01_comment = st.text_area("Komentar untuk EDM01:", 
                                placeholder="Jelaskan kondisi kerangka tata kelola TI saat ini...", 
                                key="edm01_comment")
    
    # EDM02 Assessment
    st.markdown("#### EDM02 - Memastikan TI Memberikan Manfaat bagi Layanan Pasien")
    edm02_score = st.slider("Tingkat manfaat TI untuk layanan pasien", 1, 5, 4, key="edm02",
                            help="Seberapa efektif TI meningkatkan kualitas layanan pasien?")
    
    edm02_benefits = st.multiselect("Manfaat TI yang sudah dirasakan:",
                                   ["Efisiensi administrasi", "Akurasi data pasien", "Kecepatan layanan", 
                                    "Integrasi antar unit", "Keamanan data", "Laporan real-time"],
                                   default=["Efisiensi administrasi", "Akurasi data pasien"])
    
    # EDM03 Assessment
    st.markdown("#### EDM03 - Mengelola Risiko Sistem Informasi Pasien")
    edm03_score = st.slider("Tingkat pengelolaan risiko TI", 1, 5, 3, key="edm03")
    
    risk_areas = st.multiselect("Area risiko yang sudah diidentifikasi:",
                               ["Keamanan data pasien", "Downtime sistem", "Human error", 
                                "Backup & recovery", "Compliance", "Integrasi sistem"],
                               default=["Keamanan data pasien", "Downtime sistem"])
    
    # EDM04 Assessment
    st.markdown("#### EDM04 - Mengoptimalkan Sumber Daya TI")
    edm04_score = st.slider("Tingkat optimasi sumber daya TI", 1, 5, 4, key="edm04")
    
    col1, col2 = st.columns(2)
    with col1:
        it_budget = st.number_input("Budget TI tahunan (juta Rp):", min_value=0, value=500, step=50)
    with col2:
        it_staff = st.number_input("Jumlah staff TI:", min_value=1, value=12, step=1)
    
    # EDM05 Assessment
    st.markdown("#### EDM05 - Memastikan Keterlibatan Pemangku Kepentingan")
    edm05_score = st.slider("Tingkat keterlibatan stakeholder", 1, 5, 4, key="edm05")
    
    stakeholders = st.multiselect("Stakeholder yang terlibat aktif:",
                                 ["Direktur RS", "Dokter", "Perawat", "Admin", "IT Manager", "Pasien"],
                                 default=["Direktur RS", "IT Manager", "Admin"])
    
    # Calculate EDM Average
    edm_avg = (edm01_score + edm02_score + edm03_score + edm04_score + edm05_score) / 5
    
    # Display Results
    st.markdown("### 📊 Hasil Penilaian EDM")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        color = "#28a745" if edm_avg >= 4 else "#ffc107" if edm_avg >= 3 else "#dc3545"
        st.markdown(f"""
        <div class="metric-card">
            <h3>📊 Rata-rata EDM</h3>
            <h2 style="color: {color};">{edm_avg:.1f}/5</h2>
            <p>{'Excellent' if edm_avg >= 4 else 'Good' if edm_avg >= 3 else 'Needs Improvement'}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        budget_per_staff = (it_budget * 1000000) / it_staff  # Convert to rupiah
        st.markdown(f"""
        <div class="metric-card">
            <h3>💰 Budget Efficiency</h3>
            <h2 style="color: #1976d2;">Rp {budget_per_staff:,.0f}</h2>
            <p>Per staff TI</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        stakeholder_score = len(stakeholders) / 6 * 5
        st.markdown(f"""
        <div class="metric-card">
            <h3>👥 Stakeholder Engagement</h3>
            <h2 style="color: #1976d2;">{stakeholder_score:.1f}/5</h2>
            <p>{len(stakeholders)}/6 terlibat</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recommendations
    if st.button("💡 Dapatkan Rekomendasi", key="edm_recommendations"):
        st.markdown("### 🎯 Rekomendasi Perbaikan EDM")
        
        if edm01_score < 4:
            st.warning("**EDM01**: Perkuat dokumentasi dan sosialisasi kerangka tata kelola TI")
        if edm02_score < 4:
            st.warning("**EDM02**: Lakukan evaluasi ROI dan dampak TI terhadap layanan pasien")
        if edm03_score < 4:
            st.warning("**EDM03**: Tingkatkan identifikasi dan mitigasi risiko TI")
        if edm04_score < 4:
            st.warning("**EDM04**: Optimalkan alokasi dan utilisasi sumber daya TI")
        if edm05_score < 4:
            st.warning("**EDM05**: Tingkatkan komunikasi dan keterlibatan stakeholder")
        
        if edm_avg >= 4:
            st.success("🎉 EDM sudah dalam kondisi baik! Fokus pada continuous improvement.")

def show_apo():
    st.markdown("""
    <div class="domain-card">
        <h2>📋 APO - Penjajaran, Perencanaan, dan Pengorganisasian</h2>
        <p>Memberikan arahan untuk perencanaan strategis dan taktis sistem informasi rumah sakit melalui penjajaran dengan tujuan bisnis RS.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Only keep the dynamic assessment tab
    st.markdown("### 🎯 Penilaian Skor Subdomain APO (1-5)")
    st.markdown("Berikan skor untuk setiap proses APO berdasarkan kondisi saat ini di rumah sakit:")
    
    # APO01 - Manage the IT Management Framework
    st.markdown("#### APO01 - Mengelola Kerangka Kerja Manajemen TI")
    apo01_score = st.slider("APO01 - Kerangka Kerja Manajemen TI", 1, 5, 3, key="apo01",
                            help="Seberapa baik kerangka kerja manajemen TI didefinisikan dan diimplementasikan?")
    apo01_comment = st.text_area("Komentar APO01:", placeholder="Jelaskan kondisi kerangka kerja manajemen TI...", key="apo01_comment")
        
    # APO02 - Manage Strategy
    st.markdown("#### APO02 - Mengelola Strategi TI Rumah Sakit")
    apo02_score = st.slider("APO02 - Strategi TI", 1, 5, 3, key="apo02",
                            help="Seberapa baik strategi TI selaras dengan strategi bisnis rumah sakit?")
    
    strategy_alignment = st.multiselect("Area strategi yang sudah selaras:",
                                      ["Visi & Misi RS", "Rencana Strategis", "Budget Planning", "Digital Transformation", "Patient Care Excellence"],
                                      default=["Visi & Misi RS", "Patient Care Excellence"])
    
    # APO03 - Manage Enterprise Architecture
    st.markdown("#### APO03 - Mengelola Arsitektur Enterprise")
    apo03_score = st.slider("APO03 - Arsitektur Enterprise", 1, 5, 4, key="apo03",
                            help="Seberapa baik arsitektur TI mendukung proses bisnis rumah sakit?")
    
    # APO04 - Manage Innovation
    st.markdown("#### APO04 - Mengelola Inovasi TI")
    apo04_score = st.slider("APO04 - Inovasi TI", 1, 5, 3, key="apo04",
                            help="Seberapa baik rumah sakit mengidentifikasi dan mengimplementasikan inovasi TI?")
    
    innovation_areas = st.multiselect("Area inovasi yang sedang dikembangkan:",
                                    ["Telemedicine", "AI Diagnosis", "Mobile Apps", "IoT Devices", "Cloud Computing", "Big Data Analytics"],
                                    default=["Telemedicine", "Mobile Apps"])
    
    # APO05 - Manage Portfolio
    st.markdown("#### APO05 - Mengelola Portofolio Proyek TI")
    apo05_score = st.slider("APO05 - Portofolio Proyek", 1, 5, 4, key="apo05",
                            help="Seberapa efektif manajemen portofolio proyek TI?")
    
    col1, col2 = st.columns(2)
    with col1:
        active_projects = st.number_input("Jumlah proyek aktif:", min_value=0, value=8, step=1)
    with col2:
        project_success_rate = st.slider("Success rate proyek (%)", 0, 100, 85, step=5)
    
    # APO06 - Manage Budget and Costs
    st.markdown("#### APO06 - Mengelola Budget dan Biaya TI")
    apo06_score = st.slider("APO06 - Budget & Biaya", 1, 5, 3, key="apo06",
                            help="Seberapa baik pengelolaan budget dan biaya TI?")
    
    # APO07 - Manage Human Resources
    st.markdown("#### APO07 - Mengelola SDM TI")
    apo07_score = st.slider("APO07 - SDM TI", 1, 5, 3, key="apo07",
                            help="Seberapa efektif pengelolaan sumber daya manusia TI?")
    
    hr_metrics = st.multiselect("Aspek SDM yang sudah dikelola dengan baik:",
                               ["Rekrutmen", "Training", "Performance Management", "Career Development", "Retention"],
                               default=["Rekrutmen", "Training"])
    
    # APO08 - Manage Relationships
    st.markdown("#### APO08 - Mengelola Hubungan dengan Stakeholder")
    apo08_score = st.slider("APO08 - Hubungan Stakeholder", 1, 5, 4, key="apo08",
                            help="Seberapa baik hubungan dengan stakeholder internal dan eksternal?")
        
    # APO09 - Manage Service Agreements
    st.markdown("#### APO09 - Mengelola Perjanjian Layanan")
    apo09_score = st.slider("APO09 - Service Agreements", 1, 5, 3, key="apo09",
                            help="Seberapa baik pengelolaan SLA dan perjanjian layanan TI?")
    
    # APO10 - Manage Suppliers
    st.markdown("#### APO10 - Mengelola Supplier/Vendor")
    apo10_score = st.slider("APO10 - Supplier Management", 1, 5, 3, key="apo10",
                            help="Seberapa efektif pengelolaan vendor dan supplier TI?")
    
    # APO11 - Manage Quality
    st.markdown("#### APO11 - Mengelola Kualitas")
    apo11_score = st.slider("APO11 - Quality Management", 1, 5, 3, key="apo11",
                            help="Seberapa baik sistem manajemen kualitas TI?")
    
    # APO12 - Manage Risk
    st.markdown("#### APO12 - Mengelola Risiko TI")
    apo12_score = st.slider("APO12 - Risk Management", 1, 5, 3, key="apo12",
                            help="Seberapa efektif identifikasi dan mitigasi risiko TI?")
    
    # APO13 - Manage Security
    st.markdown("#### APO13 - Mengelola Keamanan Informasi")
    apo13_score = st.slider("APO13 - Information Security", 1, 5, 4, key="apo13",
                            help="Seberapa baik pengelolaan keamanan informasi dan data pasien?")
    
    # Calculate APO Average
    apo_scores = [apo01_score, apo02_score, apo03_score, apo04_score, apo05_score, apo06_score, 
                 apo07_score, apo08_score, apo09_score, apo10_score, apo11_score, apo12_score, apo13_score]
    apo_avg = sum(apo_scores) / len(apo_scores)
    
    # Display Results
    st.markdown("### 📊 Hasil Penilaian APO")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        color = "#28a745" if apo_avg >= 4 else "#ffc107" if apo_avg >= 3 else "#dc3545"
        st.markdown(f"""
        <div class="metric-card">
            <h3>📊 Rata-rata APO</h3>
            <h2 style="color: {color};">{apo_avg:.1f}/5</h2>
            <p>{'Excellent' if apo_avg >= 4 else 'Good' if apo_avg >= 3 else 'Needs Improvement'}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🚀 Proyek Aktif</h3>
            <h2 style="color: #1976d2;">{active_projects}</h2>
            <p>Proyek TI</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>✅ Success Rate</h3>
            <h2 style="color: #28a745;">{project_success_rate}%</h2>
            <p>Proyek berhasil</p>
        </div>
            """, unsafe_allow_html=True)
        
    with col4:
        innovation_score = len(innovation_areas) / 6 * 5
        st.markdown(f"""
        <div class="metric-card">
            <h3>💡 Innovation Index</h3>
            <h2 style="color: #1976d2;">{innovation_score:.1f}/5</h2>
            <p>{len(innovation_areas)}/6 area</p>
        </div>
        """, unsafe_allow_html=True)
    
    # APO Subdomain Chart
    st.markdown("### 📈 Skor Subdomain APO")
    
    apo_processes = ['APO01\nFramework', 'APO02\nStrategy', 'APO03\nArchitecture', 'APO04\nInnovation', 
                    'APO05\nPortfolio', 'APO06\nBudget', 'APO07\nHR', 'APO08\nRelations', 
                    'APO09\nSLA', 'APO10\nSupplier', 'APO11\nQuality', 'APO12\nRisk', 'APO13\nSecurity']
    
    fig = px.bar(
        x=apo_processes,
        y=apo_scores,
        title="Skor Penilaian Subdomain APO",
        color=apo_scores,
        color_continuous_scale="RdYlGn",
        range_y=[0, 5]
    )
    fig.update_layout(height=400, showlegend=False, xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
    
    # Recommendations
    if st.button("💡 Dapatkan Rekomendasi APO", key="apo_recommendations"):
        st.markdown("### 🎯 Rekomendasi Perbaikan APO")
        
        low_scores = [(i+1, score) for i, score in enumerate(apo_scores) if score < 3]
        medium_scores = [(i+1, score) for i, score in enumerate(apo_scores) if 3 <= score < 4]
        
        if low_scores:
            st.error("**Prioritas Tinggi (Skor < 3):**")
            for process_num, score in low_scores:
                process_name = f"APO{process_num:02d}"
                st.error(f"- {process_name}: Skor {score}/5 - Perlu perbaikan segera")
        
        if medium_scores:
            st.warning("**Prioritas Sedang (Skor 3-4):**")
            for process_num, score in medium_scores:
                process_name = f"APO{process_num:02d}"
                st.warning(f"- {process_name}: Skor {score}/5 - Dapat ditingkatkan")
        
        if apo_avg >= 4:
            st.success("🎉 APO sudah dalam kondisi baik! Fokus pada continuous improvement.")

def show_bai():
    st.markdown("""
    <div class="domain-card">
        <h2>🔧 BAI - Pengembangan, Akuisisi, dan Implementasi</h2>
        <p>Menyediakan solusi TI untuk rumah sakit dan mengoperasionalkannya untuk mendukung layanan kesehatan yang optimal.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Only keep the dynamic assessment tab
    st.markdown("### 🎯 Penilaian Skor Subdomain BAI (1-5)")
    st.markdown("Berikan skor untuk setiap proses BAI berdasarkan kondisi saat ini di rumah sakit:")
    
    # BAI01 - Manage Programmes and Projects
    st.markdown("#### BAI01 - Mengelola Program dan Proyek TI")
    bai01_score = st.slider("BAI01 - Program & Proyek TI", 1, 5, 4, key="bai01",
                            help="Seberapa efektif pengelolaan program dan proyek TI rumah sakit?")
    
    project_methodology = st.multiselect("Metodologi yang digunakan:",
                                           ["Waterfall", "Agile", "Scrum", "PRINCE2", "PMI", "Hybrid"],
                                           default=["Agile", "Waterfall"])
    
    # BAI02 - Manage Requirements Definition
    st.markdown("#### BAI02 - Mengelola Definisi Kebutuhan")
    bai02_score = st.slider("BAI02 - Definisi Kebutuhan", 1, 5, 3, key="bai02",
                            help="Seberapa baik proses identifikasi dan dokumentasi kebutuhan sistem?")
    
    # BAI03 - Manage Solutions Identification and Build
    st.markdown("#### BAI03 - Mengelola Identifikasi dan Pembangunan Solusi")
    bai03_score = st.slider("BAI03 - Pembangunan Solusi", 1, 5, 3, key="bai03",
                            help="Seberapa efektif proses identifikasi dan pembangunan solusi TI?")
    
    development_approach = st.multiselect("Pendekatan pengembangan:",
                                        ["In-house Development", "Outsourcing", "COTS", "Cloud Solutions", "Hybrid"],
                                        default=["In-house Development", "Cloud Solutions"])
    
    # BAI04 - Manage Availability and Capacity
    st.markdown("#### BAI04 - Mengelola Ketersediaan dan Kapasitas")
    bai04_score = st.slider("BAI04 - Availability & Capacity", 1, 5, 4, key="bai04",
                            help="Seberapa baik pengelolaan ketersediaan dan kapasitas sistem?")
    
    col1, col2 = st.columns(2)
    with col1:
        system_uptime = st.slider("System Uptime (%)", 90, 100, 99, step=1)
    with col2:
        capacity_utilization = st.slider("Capacity Utilization (%)", 0, 100, 78, step=5)
    
    # BAI05 - Manage Organisational Change Enablement
    st.markdown("#### BAI05 - Mengelola Enablement Perubahan Organisasi")
    bai05_score = st.slider("BAI05 - Change Enablement", 1, 5, 3, key="bai05",
                            help="Seberapa efektif manajemen perubahan organisasi terkait TI?")
    
    # BAI06 - Manage Changes
    st.markdown("#### BAI06 - Mengelola Perubahan Sistem")
    bai06_score = st.slider("BAI06 - Change Management", 1, 5, 4, key="bai06",
                            help="Seberapa baik proses manajemen perubahan sistem?")
    
    change_metrics = st.multiselect("Aspek change management yang sudah baik:",
                                  ["Change Request Process", "Impact Analysis", "Testing", "Rollback Plan", "Documentation"],
                                  default=["Change Request Process", "Testing"])
    
    # BAI07 - Manage Change Acceptance and Transitioning
    st.markdown("#### BAI07 - Mengelola Penerimaan dan Transisi Perubahan")
    bai07_score = st.slider("BAI07 - Change Acceptance", 1, 5, 3, key="bai07",
                            help="Seberapa efektif proses penerimaan dan transisi perubahan?")
    
    # BAI08 - Manage Knowledge
    st.markdown("#### BAI08 - Mengelola Pengetahuan")
    bai08_score = st.slider("BAI08 - Knowledge Management", 1, 5, 3, key="bai08",
                            help="Seberapa baik pengelolaan knowledge dan dokumentasi TI?")
    
    knowledge_areas = st.multiselect("Area knowledge yang sudah terdokumentasi:",
                                   ["System Documentation", "User Manuals", "Technical Procedures", "Best Practices", "Lessons Learned"],
                                   default=["System Documentation", "User Manuals"])
    
    # BAI09 - Manage Assets
    st.markdown("#### BAI09 - Mengelola Aset TI")
    bai09_score = st.slider("BAI09 - Asset Management", 1, 5, 4, key="bai09",
                            help="Seberapa efektif pengelolaan aset TI rumah sakit?")
    
    col1, col2 = st.columns(2)
    with col1:
        total_assets = st.number_input("Total aset TI:", min_value=0, value=245, step=10)
    with col2:
        asset_tracking = st.slider("Asset tracking accuracy (%)", 0, 100, 95, step=5)
    
    # BAI10 - Manage Configuration
    st.markdown("#### BAI10 - Mengelola Konfigurasi")
    bai10_score = st.slider("BAI10 - Configuration Management", 1, 5, 3, key="bai10",
                            help="Seberapa baik pengelolaan konfigurasi sistem dan infrastruktur?")
    
    # BAI11 - Manage Projects
    st.markdown("#### BAI11 - Mengelola Proyek")
    bai11_score = st.slider("BAI11 - Project Management", 1, 5, 4, key="bai11",
                            help="Seberapa efektif manajemen proyek TI individual?")
    
    # Calculate BAI Average
    bai_scores = [bai01_score, bai02_score, bai03_score, bai04_score, bai05_score, bai06_score, 
                 bai07_score, bai08_score, bai09_score, bai10_score, bai11_score]
    bai_avg = sum(bai_scores) / len(bai_scores)
    
    # Display Results
    st.markdown("### 📊 Hasil Penilaian BAI")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        color = "#28a745" if bai_avg >= 4 else "#ffc107" if bai_avg >= 3 else "#dc3545"
        st.markdown(f"""
        <div class="metric-card">
            <h3>📊 Rata-rata BAI</h3>
            <h2 style="color: {color};">{bai_avg:.1f}/5</h2>
            <p>{'Excellent' if bai_avg >= 4 else 'Good' if bai_avg >= 3 else 'Needs Improvement'}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>⚡ System Uptime</h3>
            <h2 style="color: #28a745;">{system_uptime}%</h2>
            <p>Ketersediaan sistem</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>💾 Total Aset</h3>
        <h2 style="color: #1976d2;">{total_assets}</h2>
            <p>Aset TI</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>📋 Asset Tracking</h3>
            <h2 style="color: #28a745;">{asset_tracking}%</h2>
            <p>Akurasi tracking</p>
        </div>
        """, unsafe_allow_html=True)
    
    # BAI Subdomain Chart
    st.markdown("### 📈 Skor Subdomain BAI")
    
    bai_processes = ['BAI01\nProgram', 'BAI02\nRequirements', 'BAI03\nSolutions', 'BAI04\nCapacity', 
                    'BAI05\nChange Enable', 'BAI06\nChanges', 'BAI07\nTransition', 'BAI08\nKnowledge', 
                    'BAI09\nAssets', 'BAI10\nConfig', 'BAI11\nProjects']
    
    fig = px.bar(
        x=bai_processes,
        y=bai_scores,
        title="Skor Penilaian Subdomain BAI",
        color=bai_scores,
        color_continuous_scale="RdYlGn",
        range_y=[0, 5]
    )
    fig.update_layout(height=400, showlegend=False, xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
    
    # Recommendations
    if st.button("💡 Dapatkan Rekomendasi BAI", key="bai_recommendations"):
        st.markdown("### 🎯 Rekomendasi Perbaikan BAI")
        
        low_scores = [(i+1, score) for i, score in enumerate(bai_scores) if score < 3]
        medium_scores = [(i+1, score) for i, score in enumerate(bai_scores) if 3 <= score < 4]
        
        if low_scores:
            st.error("**Prioritas Tinggi (Skor < 3):**")
            for process_num, score in low_scores:
                process_name = f"BAI{process_num:02d}"
                st.error(f"- {process_name}: Skor {score}/5 - Perlu perbaikan segera")
        
        if medium_scores:
            st.warning("**Prioritas Sedang (Skor 3-4):**")
            for process_num, score in medium_scores:
                process_name = f"BAI{process_num:02d}"
                st.warning(f"- {process_name}: Skor {score}/5 - Dapat ditingkatkan")
        
        if bai_avg >= 4:
            st.success("🎉 BAI sudah dalam kondisi baik! Fokus pada continuous improvement.")

def show_dss():
    st.markdown("""
    <div class="domain-card">
        <h2>🛠️ DSS - Penyampaian, Layanan, dan Dukungan</h2>
        <p>Menyediakan layanan operasional TI untuk mendukung operasional rumah sakit 24/7 dan memastikan kontinuitas layanan kesehatan.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Only keep the dynamic assessment tab
    st.markdown("### 🎯 Penilaian Skor Subdomain DSS (1-5)")
    st.markdown("Berikan skor untuk setiap proses DSS berdasarkan kondisi saat ini di rumah sakit:")
    
    # DSS01 - Manage Operations
    st.markdown("#### DSS01 - Mengelola Operasional Sistem")
    dss01_score = st.slider("DSS01 - Operasional Sistem", 1, 5, 4, key="dss01",
                            help="Seberapa efektif pengelolaan operasional sistem TI rumah sakit?")
    
    col1, col2 = st.columns(2)
    with col1:
        current_uptime = st.slider("Current Uptime (%)", 90, 100, 99, step=1)
    with col2:
        active_users = st.number_input("Active Users:", min_value=0, value=156, step=10)
    
    # DSS02 - Manage Service Requests and Incidents
    st.markdown("#### DSS02 - Mengelola Permintaan Layanan dan Insiden")
    dss02_score = st.slider("DSS02 - Service Requests & Incidents", 1, 5, 4, key="dss02",
                            help="Seberapa baik pengelolaan permintaan layanan dan insiden?")
    
    incident_categories = st.multiselect("Kategori insiden yang sering terjadi:",
                                       ["EMR Login Issues", "Network Problems", "Hardware Failure", "Software Bugs", "User Training"],
                                       default=["EMR Login Issues", "Network Problems"])
    
    # DSS03 - Manage Problems
    st.markdown("#### DSS03 - Mengelola Masalah Sistem")
    dss03_score = st.slider("DSS03 - Problem Management", 1, 5, 3, key="dss03",
                            help="Seberapa efektif pengelolaan masalah sistem yang berulang?")
    
    col1, col2 = st.columns(2)
    with col1:
        known_issues = st.number_input("Known Issues:", min_value=0, value=5, step=1)
    with col2:
        prevention_rate = st.slider("Prevention Rate (%)", 0, 100, 85, step=5)
    
    # DSS04 - Manage Continuity
    st.markdown("#### DSS04 - Mengelola Kontinuitas Sistem")
    dss04_score = st.slider("DSS04 - Business Continuity", 1, 5, 4, key="dss04",
                            help="Seberapa baik pengelolaan kontinuitas dan pemulihan sistem?")
        
    continuity_measures = st.multiselect("Langkah kontinuitas yang sudah ada:",
                                           ["Daily Backup", "Disaster Recovery Plan", "Redundant Systems", "Offsite Storage", "Recovery Testing"],
                                           default=["Daily Backup", "Disaster Recovery Plan"])
        
        # DSS05 - Manage Security Services
    st.markdown("#### DSS05 - Mengelola Layanan Keamanan")
    dss05_score = st.slider("DSS05 - Security Services", 1, 5, 4, key="dss05",
                                help="Seberapa efektif pengelolaan layanan keamanan TI?")
        
    col1, col2 = st.columns(2)
    with col1:
        security_score = st.slider("Security Score", 0, 100, 95, step=5)
    with col2:
        last_audit = st.selectbox("Last Security Audit:", ["This Month", "Last Month", "2 Months Ago", "3+ Months Ago"], index=1)
    
        # DSS06 - Manage Business Process Controls
        st.markdown("#### DSS06 - Mengelola Kontrol Proses Bisnis")
        dss06_score = st.slider("DSS06 - Business Process Controls", 1, 5, 3, key="dss06",
                                help="Seberapa baik kontrol proses bisnis dalam sistem TI?")
        
        # Calculate DSS Average
        dss_scores = [dss01_score, dss02_score, dss03_score, dss04_score, dss05_score, dss06_score]
        dss_avg = sum(dss_scores) / len(dss_scores)
        
        # Display Results
        st.markdown("### 📊 Hasil Penilaian DSS")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            color = "#28a745" if dss_avg >= 4 else "#ffc107" if dss_avg >= 3 else "#dc3545"
            st.markdown(f"""
            <div class="metric-card">
                <h3>📊 Rata-rata DSS</h3>
                <h2 style="color: {color};">{dss_avg:.1f}/5</h2>
                <p>{'Excellent' if dss_avg >= 4 else 'Good' if dss_avg >= 3 else 'Needs Improvement'}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>⚡ System Uptime</h3>
                <h2 style="color: #28a745;">{current_uptime}%</h2>
                <p>Ketersediaan sistem</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h3>👥 Active Users</h3>
                <h2 style="color: #1976d2;">{active_users}</h2>
                <p>Pengguna aktif</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h3>🔒 Security Score</h3>
                <h2 style="color: #28a745;">{security_score}/100</h2>
                <p>Skor keamanan</p>
            </div>
            """, unsafe_allow_html=True)
        
        # DSS Subdomain Chart
        st.markdown("### 📈 Skor Subdomain DSS")
        
        dss_processes = ['DSS01\nOperations', 'DSS02\nIncidents', 'DSS03\nProblems', 
                        'DSS04\nContinuity', 'DSS05\nSecurity', 'DSS06\nControls']
        
        fig = px.bar(
            x=dss_processes,
            y=dss_scores,
            title="Skor Penilaian Subdomain DSS",
            color=dss_scores,
            color_continuous_scale="RdYlGn",
            range_y=[0, 5]
        )
        fig.update_layout(height=400, showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
        
        # Recommendations
        if st.button("💡 Dapatkan Rekomendasi DSS", key="dss_recommendations"):
            st.markdown("### 🎯 Rekomendasi Perbaikan DSS")
            
            low_scores = [(i+1, score) for i, score in enumerate(dss_scores) if score < 3]
            medium_scores = [(i+1, score) for i, score in enumerate(dss_scores) if 3 <= score < 4]
            
            if low_scores:
                st.error("**Prioritas Tinggi (Skor < 3):**")
                for process_num, score in low_scores:
                    process_name = f"DSS{process_num:02d}"
                    st.error(f"- {process_name}: Skor {score}/5 - Perlu perbaikan segera")
            
            if medium_scores:
                st.warning("**Prioritas Sedang (Skor 3-4):**")
                for process_num, score in medium_scores:
                    process_name = f"DSS{process_num:02d}"
                    st.warning(f"- {process_name}: Skor {score}/5 - Dapat ditingkatkan")
            
            if dss_avg >= 4:
                st.success("🎉 DSS sudah dalam kondisi baik! Fokus pada continuous improvement.")

def show_mea():
    st.markdown("""
    <div class="domain-card">
        <h2>📊 MEA - Pemantauan, Evaluasi, dan Penilaian</h2>
        <p>Memantau semua proses TI rumah sakit untuk memastikan mencapai tujuan layanan kesehatan yang optimal dan mematuhi regulasi.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Only keep the dynamic assessment tab
    st.markdown("### 🎯 Penilaian Skor Subdomain MEA (1-5)")
    st.markdown("Berikan skor untuk setiap proses MEA berdasarkan kondisi saat ini di rumah sakit:")
    
    # MEA01 - Monitor, Evaluate and Assess Performance and Conformance
    st.markdown("#### MEA01 - Memantau, Mengevaluasi, dan Menilai Kinerja & Kepatuhan")
    mea01_score = st.slider("MEA01 - Performance & Conformance", 1, 5, 3, key="mea01",
                            help="Seberapa efektif pemantauan kinerja dan kepatuhan sistem TI?")
    
    col1, col2 = st.columns(2)
    with col1:
        kpi_tracking = st.number_input("Jumlah KPI yang dipantau:", min_value=0, value=15, step=1)
    with col2:
        achievement_rate = st.slider("Achievement Rate (%)", 0, 100, 92, step=5)
        
        performance_areas = st.multiselect("Area kinerja yang dipantau:",
                                         ["EMR Performance", "System Uptime", "User Satisfaction", "Response Time", "Data Quality"],
                                         default=["EMR Performance", "System Uptime"])
        
        # MEA02 - Monitor, Evaluate and Assess the System of Internal Controls
        st.markdown("#### MEA02 - Memantau, Mengevaluasi, dan Menilai Sistem Pengendalian Internal")
        mea02_score = st.slider("MEA02 - Internal Controls", 1, 5, 3, key="mea02",
                                help="Seberapa baik sistem pengendalian internal TI?")
        
        col1, col2 = st.columns(2)
        with col1:
            audit_score = st.slider("Audit Score", 0, 100, 88, step=5)
        with col2:
            last_audit = st.selectbox("Last Internal Audit:", ["This Month", "Last Month", "2 Months Ago", "3+ Months Ago"], index=2)
        
        control_areas = st.multiselect("Area kontrol yang diaudit:",
                                     ["Access Control", "Data Security", "Change Management", "Backup & Recovery", "Incident Response"],
                                     default=["Access Control", "Data Security"])
        
        # MEA03 - Monitor, Evaluate and Assess Compliance with External Requirements
        st.markdown("#### MEA03 - Memantau, Mengevaluasi, dan Menilai Kepatuhan Regulasi Eksternal")
        mea03_score = st.slider("MEA03 - External Compliance", 1, 5, 4, key="mea03",
                                help="Seberapa baik kepatuhan terhadap regulasi eksternal?")
        
        col1, col2 = st.columns(2)
        with col1:
            compliance_rate = st.slider("Compliance Rate (%)", 0, 100, 96, step=1)
        with col2:
            external_audit = st.selectbox("Last External Audit:", ["This Month", "Last Month", "2 Months Ago", "3+ Months Ago"], index=1)
        
        compliance_areas = st.multiselect("Area compliance yang dipantau:",
                                        ["HIPAA", "Data Privacy", "Medical Records", "Security Standards", "Patient Safety"],
                                        default=["HIPAA", "Data Privacy"])
        
        # Additional MEA metrics
        st.markdown("#### 📊 Metrics Tambahan MEA")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            stakeholder_satisfaction = st.slider("Stakeholder Satisfaction", 1, 5, 4, step=1)
        with col2:
            report_frequency = st.selectbox("Report Frequency:", ["Daily", "Weekly", "Monthly", "Quarterly"], index=2)
        with col3:
            remediation_rate = st.slider("Remediation Rate (%)", 0, 100, 75, step=5)
        
        # Calculate MEA Average
        mea_scores = [mea01_score, mea02_score, mea03_score]
        mea_avg = sum(mea_scores) / len(mea_scores)
        
        # Display Results
        st.markdown("### 📊 Hasil Penilaian MEA")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            color = "#28a745" if mea_avg >= 4 else "#ffc107" if mea_avg >= 3 else "#dc3545"
            st.markdown(f"""
            <div class="metric-card">
                <h3>📊 Rata-rata MEA</h3>
                <h2 style="color: {color};">{mea_avg:.1f}/5</h2>
                <p>{'Excellent' if mea_avg >= 4 else 'Good' if mea_avg >= 3 else 'Needs Improvement'}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>📈 KPI Achievement</h3>
                <h2 style="color: #28a745;">{achievement_rate}%</h2>
                <p>Target pencapaian</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h3>✅ Compliance Rate</h3>
                <h2 style="color: #28a745;">{compliance_rate}%</h2>
                <p>Tingkat kepatuhan</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h3>🔍 Audit Score</h3>
                <h2 style="color: #1976d2;">{audit_score}/100</h2>
                <p>Skor audit internal</p>
            </div>
            """, unsafe_allow_html=True)
        
        # MEA Subdomain Chart
        st.markdown("### 📈 Skor Subdomain MEA")
        
        mea_processes = ['MEA01\nPerformance', 'MEA02\nInternal Controls', 'MEA03\nCompliance']
        
        fig = px.bar(
            x=mea_processes,
            y=mea_scores,
            title="Skor Penilaian Subdomain MEA",
            color=mea_scores,
            color_continuous_scale="RdYlGn",
            range_y=[0, 5]
        )
        fig.update_layout(height=400, showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
        
        # Recommendations
        if st.button("💡 Dapatkan Rekomendasi MEA", key="mea_recommendations"):
            st.markdown("### 🎯 Rekomendasi Perbaikan MEA")
            
            low_scores = [(i+1, score) for i, score in enumerate(mea_scores) if score < 3]
            medium_scores = [(i+1, score) for i, score in enumerate(mea_scores) if 3 <= score < 4]
            
            if low_scores:
                st.error("**Prioritas Tinggi (Skor < 3):**")
                for process_num, score in low_scores:
                    process_name = f"MEA{process_num:02d}"
                    st.error(f"- {process_name}: Skor {score}/5 - Perlu perbaikan segera")
            
            if medium_scores:
                st.warning("**Prioritas Sedang (Skor 3-4):**")
                for process_num, score in medium_scores:
                    process_name = f"MEA{process_num:02d}"
                    st.warning(f"- {process_name}: Skor {score}/5 - Dapat ditingkatkan")
            
            if mea_avg >= 4:
                st.success("🎉 MEA sudah dalam kondisi baik! Fokus pada continuous improvement.")
            
            # Specific recommendations
            if compliance_rate < 95:
                st.warning("⚠️ Compliance rate perlu ditingkatkan untuk memenuhi standar regulasi.")
            
            if audit_score < 85:
                st.warning("⚠️ Audit score perlu perbaikan untuk meningkatkan kontrol internal.")

if __name__ == "__main__":
    main()