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
