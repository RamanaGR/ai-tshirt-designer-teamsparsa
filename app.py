import streamlit as st

st.set_page_config(
    page_title="AI-Powered T-Shirt Designer",
    layout="centered",
    initial_sidebar_state="collapsed"
)
        
col1, col2 = st.columns([1, 6])
with col1:
    try:
        st.image("assets/logo.png", width=80)
    except:
        st.markdown(" ")

with col2:
    st.markdown("<h1>AI-Powered T-Shirt Designer</h1>", unsafe_allow_html=True)
    st.markdown("Design your perfect T-shirt with live previews and smart AI features.")

st.image("assets/round_neck.png", use_container_width=True, caption="Customize styles, colors, and more")

st.markdown("## 👇 Ready to create your own?")
if st.button("🎨 Start Designing", use_container_width=True):
    st.switch_page("pages/1_Designer.py")

if 'cart' not in st.session_state:
    st.session_state.cart = []

st.markdown("---")
st.markdown("### 🙌 Project Credits")
st.markdown("""
**Team Sparsa** – MIT 588: Software Development and Management  
- 👨‍💻 **Ramana** – Backend Logic, Cart Integration, Deployment  
- 🎨 **Asha** – UI/UX Design, Visual Assets  
- 🧪 **Srikar** – Testing, Documentation  
- 📊 **Saphal** – Workflow Planning, Presentation  
""")
