import io
from collections import Counter
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import streamlit as st

st.set_page_config(
    page_title="DesignOps Studio",
    page_icon="🎨",
    layout="wide"
)

# Persistent state for client tickets
if "client_tickets" not in st.session_state:
    st.session_state.client_tickets = [
        {"Client": "Acme SaaS", "Task": "Homepage Hero Refresh", "Priority": "High", "Status": "In Progress"},
        {"Client": "FinTech Daily", "Task": "Pitch Deck Redesign", "Priority": "Medium", "Status": "Review"}
    ]

# Sidebar navigation
st.sidebar.title("🎨 DesignOps Studio")
page = st.sidebar.radio("Navigate", [
    "1. Brand Palette Extractor",
    "2. Ad Banner Resizer",
    "3. Asset Storefront",
    "4. Client Request Board"
])

# -------------------------------------------------------------
# 1. Brand Palette Extractor
# -------------------------------------------------------------
if page == "1. Brand Palette Extractor":
    st.header("🎨 Brand Palette Extractor")
    st.caption("Upload any brand logo or visual to extract dominant hex colors.")

    uploaded_img = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if uploaded_img:
        img = Image.open(uploaded_img).convert("RGB")
        st.image(img, caption="Uploaded File", width=250)

        # Downsample and extract dominant colors
        small_img = img.resize((100, 100))
        pixels = list(small_img.getdata())
        common_colors = [c[0] for c in Counter(pixels).most_common(5)]

        st.subheader("Extracted Palette")
        cols = st.columns(len(common_colors))
        for idx, (r, g, b) in enumerate(common_colors):
            hex_val = f"#{r:02x}{g:02x}{b:02x}"
            with cols[idx]:
                st.markdown(
                    f'<div style="background-color:{hex_val}; height:70px; border-radius:8px; border:1px solid #ddd;"></div>',
                    unsafe_allow_html=True
                )
                st.code(hex_val, language="text")

# -------------------------------------------------------------
# 2. Ad Banner Resizer & Generator
# -------------------------------------------------------------
elif page == "2. Ad Banner Resizer":
    st.header("📐 Ad Banner Generator")
    st.caption("Auto-render formatted graphics for social marketing.")

    col1, col2 = st.columns([1, 2])
    with col1:
        headline = st.text_input("Banner Headline", "Scale Your Creative Output")
        subtext = st.text_input("Subtext", "Productized design workflows made simple.")
        preset = st.selectbox("Dimension Preset", [
            "Instagram Post (1080x1080)",
            "Twitter/X Header (1500x500)",
            "LinkedIn Banner (1200x628)"
        ])
        bg_color = st.color_picker("Background Color", "#0F172A")
        text_color = st.color_picker("Text Color", "#F8FAFC")

    # Dimensions lookup
    dims = {
        "Instagram Post (1080x1080)": (1080, 1080),
        "Twitter/X Header (1500x500)": (1500, 500),
        "LinkedIn Banner (1200x628)": (1200, 628)
    }
    w, h = dims[preset]

    # Generate banner canvas
    banner = Image.new("RGB", (w, h), color=bg_color)
    draw = ImageDraw.Draw(banner)
    
    # Text placement
    draw.text((int(w * 0.1), int(h * 0.35)), headline, fill=text_color)
    draw.text((int(w * 0.1), int(h * 0.5)), subtext, fill=text_color)

    with col2:
        st.subheader("Live Preview")
        st.image(banner, use_container_width=True)

        buf = io.BytesIO()
        banner.save(buf, format="PNG")
        st.download_button(
            label="Download Banner (PNG)",
            data=buf.getvalue(),
            file_name="social_banner.png",
            mime="image/png"
        )

# -------------------------------------------------------------
# 3. Asset Storefront
# -------------------------------------------------------------
elif page == "3. Asset Storefront":
    st.header("📦 Digital Asset Storefront")
    st.caption("Downloadable design kits and templates.")

    assets = [
        {"title": "B2B SaaS Pitch Deck Kit", "format": "Figma / PPTX", "price": "$39", "desc": "35 high-conversion slides."},
        {"title": "Social Ad Performance Bundle", "format": "Figma / Canva", "price": "$29", "desc": "60 tested e-commerce templates."},
        {"title": "Design System Starter Kit", "format": "Figma", "price": "$49", "desc": "Typography, auto-layout, tokens."}
    ]

    cols = st.columns(len(assets))
    for idx, asset in enumerate(assets):
        with cols[idx]:
            st.markdown(f"### {asset['title']}")
            st.write(f"**Format:** {asset['format']}")
            st.write(f"**Price:** {asset['price']}")
            st.write(asset['desc'])
            st.button(f"Purchase ({asset['price']})", key=f"buy_{idx}")

# -------------------------------------------------------------
# 4. Client Request Board
# -------------------------------------------------------------
elif page == "4. Client Request Board":
    st.header("📋 Client Request Board")
    st.caption("Simple queue to manage active retainer tasks.")

    with st.expander("➕ Submit New Task"):
        client_name = st.text_input("Client Name")
        task_title = st.text_input("Task Description")
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        if st.button("Submit Ticket"):
            if client_name and task_title:
                st.session_state.client_tickets.append({
                    "Client": client_name,
                    "Task": task_title,
                    "Priority": priority,
                    "Status": "Pending"
                })
                st.success("Ticket added.")
            else:
                st.error("Please fill in both fields.")

    st.subheader("Active Tasks")
    df = pd.DataFrame(st.session_state.client_tickets)
    st.dataframe(df, use_container_width=True)
