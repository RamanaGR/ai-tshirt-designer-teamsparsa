import streamlit as st

st.set_page_config(page_title="Checkout", layout="centered", initial_sidebar_state="collapsed")
st.markdown("## 💳 Checkout")

# 🛒 Display order summary if cart is available
cart = st.session_state.get("cart", [])

if cart:
    st.markdown("### 🧾 Order Summary:")
    for i, item in enumerate(cart):
        st.write(f"**Item {i+1}**")
        st.write(f"• Style: {item['type']}")
        st.write(f"• Size: {item['size']}")
        st.write(f"• Color: {item['color']}")
        st.write(f"• Design File: {item['design']}")
    st.markdown("---")
else:
    st.info("Your cart is empty. Please go back and add items.")
    st.stop()

# 📝 Checkout form
with st.form("checkout_form"):
    name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email")
    address = st.text_area("🏠 Shipping Address")
    payment_method = st.selectbox("💰 Payment Method", ["Credit Card", "PayPal", "Cash on Delivery"])
    
    submit = st.form_submit_button("Place Order")

if submit:
    errors = []

    if not name.strip():
        errors.append("❗ Please enter your full name.")
    if not email.strip():
        errors.append("❗ Please enter your email address.")
    if not address.strip():
        errors.append("❗ Please provide a shipping address.")

    if errors:
        for err in errors:
            st.error(err)
    else:
        st.success(f"✅ Order placed successfully! Thank you, {name}.")
        # 🧹 Clear cart after successful checkout
        st.session_state.cart = []
