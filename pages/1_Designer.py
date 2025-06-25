import streamlit as st
from PIL import Image

# 🛒 Initialize cart only once per session
if 'cart' not in st.session_state:
    st.session_state.cart = []

# 🔢 Cart item count
cart_count = len(st.session_state.cart)

# 🧭 Page config
st.set_page_config(
    page_title="Design Your T-Shirt",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🛒 Cart icon on top-right
with st.container():
    col1, col2 = st.columns([8, 1])
    with col2:
        st.page_link("pages/2_Cart.py", label=f"🛒 Cart ({cart_count})", use_container_width=True)

# 🔰 Header section
col1, col2 = st.columns([1, 5])
with col1:
    try:
        st.image("assets/logo.png", width=80)
    except:
        st.markdown(" ")
with col2:
    st.markdown("<h1 style='margin-bottom: 0;'>AI-Powered T-Shirt Designer</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: gray; font-style: italic;'>MIT 588 · Personalized E-Commerce Platform</p>", unsafe_allow_html=True)

st.markdown("---")

# 🎨 Sidebar T-shirt options
st.sidebar.header("🛠️ Customize Your T-Shirt")
tshirt_type = st.sidebar.selectbox("T-Shirt Style", ["Round Neck", "V-Neck", "Polo", "Hoodie"])
color = st.sidebar.color_picker("Pick Shirt Color", "#ffffff")
uploaded_img = st.sidebar.file_uploader("Upload Your Design", type=["jpg", "jpeg", "png"])
size = st.sidebar.radio("Select Size", ["S", "M", "L", "XL"])

style_map = {
    "Round Neck": "assets/round_neck.png",
    "V-Neck": "assets/v_neck.png",
    "Polo": "assets/polo.png",
    "Hoodie": "assets/hoodie.png"
}

# 🖼️ Preview uploaded design image
if uploaded_img:
    user_design = Image.open(uploaded_img).convert("RGBA")
    st.image(user_design, caption="Uploaded Design", use_container_width=True)

# 🧠 Generate AI preview
if uploaded_img and st.button("Generate AI Preview", use_container_width=True):
    tshirt_base = Image.open(style_map[tshirt_type]).convert("RGBA")
    color_overlay = Image.new("RGBA", tshirt_base.size, color)
    colored_shirt = Image.blend(tshirt_base, color_overlay, alpha=0.4)

    shirt_width, shirt_height = colored_shirt.size
    if tshirt_type == "Hoodie":
        max_width = int(shirt_width * 0.55)
        max_height = int(shirt_height * 0.35)
        top_offset = -30
    else:
        max_width = int(shirt_width * 0.65)
        max_height = int(shirt_height * 0.45)
        top_offset = {
            "Round Neck": 70,
            "V-Neck": 120,
            "Polo": 130
        }.get(tshirt_type, 70)

    design_ratio = user_design.width / user_design.height
    if max_width / design_ratio <= max_height:
        new_width = max_width
        new_height = int(max_width / design_ratio)
    else:
        new_height = max_height
        new_width = int(max_height * design_ratio)

    design_resized = user_design.resize((new_width, new_height), Image.LANCZOS)
    alpha = design_resized.split()[3].point(lambda p: int(p * 0.75))
    design_resized.putalpha(alpha)

    x_center = (shirt_width - new_width) // 2
    y_center = ((shirt_height - new_height) // 2) + top_offset

    final_preview = colored_shirt.copy()
    final_preview.paste(design_resized, (x_center, y_center), design_resized)

    st.success(f"✅ AI Preview Generated ({tshirt_type})")
    st.image(final_preview, caption="AI-Generated T-Shirt", use_container_width=True)

    # Save final preview to session for download
    from io import BytesIO
    buf = BytesIO()
    final_preview.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 Download Mockup",
        data=byte_im,
        file_name=f"{tshirt_type}_mockup.png",
        mime="image/png",
        use_container_width=True
    )

    # Save design info for cart
    st.session_state.final_preview_image = final_preview
    st.session_state.final_preview_available = True
    st.session_state.design_data = {
        "type": tshirt_type,
        "size": size,
        "color": color,
        "design": uploaded_img.name
    }

# ✅ Independent Add to Cart button (shown only after preview)
if uploaded_img and st.session_state.get("final_preview_available", False):
    if st.button("Add to Cart", use_container_width=True):
        st.session_state.cart.append(st.session_state.design_data)
        st.session_state.final_preview_available = False  # reset flag
        st.success("✅ Design added to cart!")
        # st.experimental_rerun()  # optional if live count is fixed later
