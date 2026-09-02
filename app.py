import streamlit as st

st.set_page_config(
    page_title="DesignCraft Hub | Creative Operations",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 DesignCraft: Creative Suite & Ops Portal")
st.caption("All-in-one studio: Automated tools, curated assets, and client project management.")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🛠️ Creative Micro-Tools")
    st.write("Generate palettes, verify WCAG contrast, and resize ad banners instantly.")
    st.info("Navigate to **Brand Toolkit** in the sidebar.")

with col2:
    st.subheader("📦 Digital Asset Hub")
    st.write("Browse premium Figma kits, pitch deck layouts, and marketing templates.")
    st.info("Navigate to **Asset Marketplace** in the sidebar.")

with col3:
    st.subheader("📋 Client Design Desk")
    st.write("Submit design requests, review active deliverables, and manage retainers.")
    st.info("Navigate to **Client Portal** in the sidebar.")

import streamlit as st
from PIL import Image
from collections import Counter

st.title("🎨 Brand Palette & Contrast Inspector")

uploaded_file = st.file_uploader("Upload a brand logo or banner (PNG/JPG)", type=["png", "jpg", "jpeg"])

def get_dominant_colors(image, num_colors=5):
    img = image.copy().convert("RGB").resize((100, 100))
    pixels = list(img.getdata())
    counts = Counter(pixels)
    return [c[0] for c in counts.most_common(num_colors)]

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Source Asset", width=300)
    
    colors = get_dominant_colors(img, 5)
    st.subheader("Extracted Palette")
    
    cols = st.columns(len(colors))
    for idx, (r, g, b) in enumerate(colors):
        hex_code = f"#{r:02x}{g:02x}{b:02x}"
        with cols[idx]:
            st.markdown(
                f'<div style="background-color: {hex_code}; height: 80px; border-radius: 8px; border: 1px solid #ccc;"></div>',
                unsafe_allow_html=True
            )
            st.code(hex_code, language="text")
