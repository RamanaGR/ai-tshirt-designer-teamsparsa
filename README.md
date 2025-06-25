# 👕 AI-Powered T-Shirt Designer

An interactive Python-based web application built with **Streamlit**, allowing users to design personalized T-shirts using real-time image overlay, color picking, and shirt style preview. Developed by Team **Sparsa** as part of the final project for **MIT 588 – Software Development and Management**.

---

## 🚀 Live Demo

🔗 [Click here to try the app on Streamlit Cloud](https://your-streamlit-app-link)

---

## 📦 Features

- Upload your own design and preview it on different T-shirt types
- Choose from styles: Round Neck, V-Neck, Polo, Hoodie
- Pick T-shirt colors using a live color picker
- Add designs to cart and proceed to checkout
- Download mockup image of your custom shirt
- Fully responsive layout with minimal UI

---

## 🧠 Technologies Used

- **Python 3.10+**
- **Streamlit**
- **Pillow (PIL)** for image processing
- **Session State Management** in Streamlit
- **GitHub** for version control
- **Streamlit Cloud** for deployment

---

## 📁 Project Structure

```text
ai_tshirt_designer_app/
├── app.py                        # Main entry point (Home page)
├── pages/                        # Additional app pages
│   ├── 1_Designer.py             # T-shirt Designer Page
│   ├── 2_Cart.py                 # Shopping Cart Page
│   └── 3_Checkout.py             # Checkout & Order Form
├── assets/                       # Static assets
│   ├── logo.png                  # Brand logo
│   └── [T-shirt templates]       # PNG files for each shirt type
└── .streamlit/
    └── config.toml               # Theme and page config

---

## 🙌 Credits

**Team Sparsa**  
MIT 588 – Software Development and Management  
[Atlantis University]

- **Ramana** – Backend Logic, Cart Integration, Deployment
- **Asha** – UI/UX Design, Visual Assets
- **Srikar** – Testing, Documentation
- **Saphal** – Workflow Planning, Presentation

---

## 📄 License

This project is open-source and for academic demonstration purposes only.

---

## 📚 References

See [Phase 5 Documentation](./docs/Mit588_Phase5_Appendix.md) for detailed citations in APA format.

---

## 📈 Future Enhancements

- AI style recommendation based on design type
- Integration with payment gateways (e.g., Stripe)
- User login system and order history
- Analytics dashboard for admin
