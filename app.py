import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="COBIT Framework Management System",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f4e79, #2e6da4);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .domain-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
        <h1>🏢 COBIT Framework Management System</h1>
        <p>Comprehensive IT Governance and Management Framework</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.markdown("### 📊 Navigation Menu")
    page = st.sidebar.selectbox(
        "Select Domain:",
        ["Dashboard", "EDM - Evaluate, Direct and Monitor", "APO - Align, Plan and Organise", 
         "BAI - Build, Acquire and Implement", "DSS - Deliver, Service and Support", 
         "MEA - Monitor, Evaluate and Assess"]
    )
    
    if page == "Dashboard":
        show_dashboard()
    elif page == "EDM - Evaluate, Direct and Monitor":
        show_edm()
    elif page == "APO - Align, Plan and Organise":
        show_apo()
    elif page == "BAI - Build, Acquire and Implement":
        show_bai()
    elif page == "DSS - Deliver, Service and Support":
        show_dss()
    elif page == "MEA - Monitor, Evaluate and Assess":
        show_mea()

def show_dashboard():
    st.markdown("## 📊 Executive Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🎯 Overall Maturity</h3>
            <h2 style="color: #2e6da4;">3.2/5</h2>
            <p>Defined Level</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>✅ Compliance Rate</h3>
            <h2 style="color: #28a745;">78%</h2>
            <p>Above Target</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>⚠️ Risk Level</h3>
            <h2 style="color: #ffc107;">Medium</h2>
            <p>Manageable</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Domain maturity chart
    st.markdown("### 📈 Domain Maturity Overview")
    
    domains = ['EDM', 'APO', 'BAI', 'DSS', 'MEA']
    maturity_scores = [3.5, 3.2, 2.8, 3.4, 3.1]
    
    fig = px.bar(
        x=domains, 
        y=maturity_scores,
        title="Maturity Levels by Domain",
        color=maturity_scores,
        color_continuous_scale="viridis"
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Recent audit findings
    st.markdown("### 📋 Recent Audit Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #d4edda; padding: 1rem; border-radius: 10px; border-left: 4px solid #28a745;">
            <h4 style="color: #155724;">✅ Positive Findings</h4>
            <ul style="color: #155724;">
                <li>Strong governance framework implementation</li>
                <li>Effective risk management processes</li>
                <li>Good stakeholder communication</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #f8d7da; padding: 1rem; border-radius: 10px; border-left: 4px solid #dc3545;">
            <h4 style="color: #721c24;">⚠️ Areas for Improvement</h4>
            <ul style="color: #721c24;">
                <li>Need better change management processes</li>
                <li>Enhance monitoring and evaluation</li>
                <li>Improve vendor management controls</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_edm():
    st.markdown("""
    <div class="domain-card">
        <h2>📊 EDM - Evaluate, Direct and Monitor</h2>
        <p>Ensure that stakeholder needs, conditions and options are evaluated to determine balanced, agreed-on enterprise objectives.</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["EDM01-02", "EDM03-04", "EDM05"])
    
    with tab1:
        st.markdown("### EDM01 - Ensure Governance Framework Setting and Maintenance")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Objective:** Provide a consistent approach integrated with the enterprise governance approach.")
            maturity = st.slider("Maturity Level", 0, 5, 3, key="edm01_maturity")
            
        with col2:
            st.text_area("Audit Notes", placeholder="Enter audit findings and recommendations...", key="edm01_notes")
        
        # Compliance checklist
        st.markdown("**Compliance Checklist:**")
        checks = [
            "Governance framework is documented",
            "Roles and responsibilities are defined",
            "Governance processes are implemented",
            "Regular governance reviews are conducted"
        ]
        
        completed = 0
        for i, check in enumerate(checks):
            if st.checkbox(check, key=f"edm01_check_{i}"):
                completed += 1
        
        progress = completed / len(checks)
        st.progress(progress)
        st.write(f"Completion: {completed}/{len(checks)} ({progress:.0%})")
        
        st.markdown("### EDM02 - Ensure Benefits Delivery")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Objective:** Optimize value creation from IT-enabled investments.")
            maturity = st.slider("Maturity Level", 0, 5, 3, key="edm02_maturity")
            
        with col2:
            st.text_area("Audit Notes", placeholder="Enter audit findings and recommendations...", key="edm02_notes")
    
    with tab2:
        st.markdown("### EDM03 - Ensure Risk Optimization")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Objective:** Ensure that enterprise risk appetite and tolerance are understood.")
            maturity = st.slider("Maturity Level", 0, 5, 3, key="edm03_maturity")
            
        with col2:
            st.text_area("Audit Notes", placeholder="Enter audit findings and recommendations...", key="edm03_notes")
        
        st.markdown("### EDM04 - Ensure Resource Optimization")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Objective:** Ensure that adequate and sufficient capabilities are available.")
            maturity = st.slider("Maturity Level", 0, 5, 3, key="edm04_maturity")
            
        with col2:
            st.text_area("Audit Notes", placeholder="Enter audit findings and recommendations...", key="edm04_notes")
    
    with tab3:
        st.markdown("### EDM05 - Ensure Stakeholder Transparency")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Objective:** Ensure that enterprise IT performance and conformance measurement and reporting.")
            maturity = st.slider("Maturity Level", 0, 5, 3, key="edm05_maturity")
            
        with col2:
            st.text_area("Audit Notes", placeholder="Enter audit findings and recommendations...", key="edm05_notes")

def show_apo():
    st.markdown("""
    <div class="domain-card">
        <h2>🎯 APO - Align, Plan and Organise</h2>
        <p>Provide direction for solution delivery and service delivery.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Key Processes")
    
    processes = [
        "APO01 - Manage the IT Management Framework",
        "APO02 - Manage Strategy", 
        "APO03 - Manage Enterprise Architecture",
        "APO04 - Manage Innovation",
        "APO05 - Manage Portfolio",
        "APO06 - Manage Budget and Costs",
        "APO07 - Manage Human Resources",
        "APO08 - Manage Relationships",
        "APO09 - Manage Service Agreements",
        "APO10 - Manage Suppliers",
        "APO11 - Manage Quality",
        "APO12 - Manage Risk",
        "APO13 - Manage Security",
        "APO14 - Manage Data"
    ]
    
    for i, process in enumerate(processes):
        with st.expander(process):
            col1, col2 = st.columns(2)
            with col1:
                maturity = st.slider("Maturity Level", 0, 5, 3, key=f"apo_{i}_maturity")
            with col2:
                st.text_area("Notes", placeholder="Enter notes...", key=f"apo_{i}_notes")

def show_bai():
    st.markdown("""
    <div class="domain-card">
        <h2>🔧 BAI - Build, Acquire and Implement</h2>
        <p>Provide solutions and pass them to service delivery.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Key Processes")
    
    processes = [
        "BAI01 - Manage Programmes and Projects",
        "BAI02 - Manage Requirements Definition",
        "BAI03 - Manage Solutions Identification and Build",
        "BAI04 - Manage Availability and Capacity",
        "BAI05 - Manage Organisational Change",
        "BAI06 - Manage IT Changes",
        "BAI07 - Manage Change Acceptance and Transitioning",
        "BAI08 - Manage Knowledge",
        "BAI09 - Manage Assets",
        "BAI10 - Manage Configuration",
        "BAI11 - Manage Projects"
    ]
    
    for i, process in enumerate(processes):
        with st.expander(process):
            col1, col2 = st.columns(2)
            with col1:
                maturity = st.slider("Maturity Level", 0, 5, 3, key=f"bai_{i}_maturity")
            with col2:
                st.text_area("Notes", placeholder="Enter notes...", key=f"bai_{i}_notes")

def show_dss():
    st.markdown("""
    <div class="domain-card">
        <h2>🚀 DSS - Deliver, Service and Support</h2>
        <p>Receive solutions from build and make them usable by end users.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Key Processes")
    
    processes = [
        "DSS01 - Manage Operations",
        "DSS02 - Manage Service Requests and Incidents",
        "DSS03 - Manage Problems",
        "DSS04 - Manage Continuity",
        "DSS05 - Manage Security Services",
        "DSS06 - Manage Business Process Controls"
    ]
    
    for i, process in enumerate(processes):
        with st.expander(process):
            col1, col2 = st.columns(2)
            with col1:
                maturity = st.slider("Maturity Level", 0, 5, 3, key=f"dss_{i}_maturity")
            with col2:
                st.text_area("Notes", placeholder="Enter notes...", key=f"dss_{i}_notes")

def show_mea():
    st.markdown("""
    <div class="domain-card">
        <h2>📈 MEA - Monitor, Evaluate and Assess</h2>
        <p>Monitor all processes to ensure they follow the set direction.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Key Processes")
    
    processes = [
        "MEA01 - Monitor, Evaluate and Assess Performance and Conformance",
        "MEA02 - Monitor, Evaluate and Assess the System of Internal Controls",
        "MEA03 - Monitor, Evaluate and Assess Compliance with External Requirements"
    ]
    
    for i, process in enumerate(processes):
        with st.expander(process):
            col1, col2 = st.columns(2)
            with col1:
                maturity = st.slider("Maturity Level", 0, 5, 3, key=f"mea_{i}_maturity")
            with col2:
                st.text_area("Notes", placeholder="Enter notes...", key=f"mea_{i}_notes")

if __name__ == "__main__":
    main()