import streamlit as st

st.set_page_config(
    page_title="Your Cart",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("## 🛒 Your Cart")

# 🛒 Get or create cart
if 'cart' not in st.session_state:
    st.session_state.cart = []

cart = st.session_state.cart

if not cart:
    st.info("Your cart is empty.")
else:
    for i, item in enumerate(cart):
        st.write(f"### Item {i+1}")
        st.write(f"**Style**: {item['type']}")
        st.write(f"**Size**: {item['size']}")
        st.write(f"**Color**: {item['color']}")
        st.write(f"**Design File**: {item['design']}")
        if st.button(f"❌ Remove Item {i+1}"):
            cart.pop(i)
            st.rerun()

    if st.button("💳 Proceed to Checkout", use_container_width=True):
        st.switch_page("pages/3_Checkout.py")
