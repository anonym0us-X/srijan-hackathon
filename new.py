import streamlit as st

# Set the page configuration
# This must be the first Streamlit command in your script.
st.set_page_config(
    page_title="Sustainable Energy Monitor",
    page_icon="💡", # A suitable emoji for a page icon
    layout="wide"
)

# --- Custom CSS for fine-tuning (Optional) ---
# This can be used to style elements that config.toml doesn't cover
def local_css(file_name):
    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# You could create a style.css file for more complex styles, but for a few lines:
st.markdown("""
<style>
/* This targets the "Add Appliance" button to give it a custom look */
.stButton>button {
    border: 2px solid #66FF99;
    background-color: transparent;
    color: #66FF99;
}
.stButton>button:hover {
    border-color: #EAEAEA;
    background-color: #66FF99;
    color: #1A2B2F;
}
</style>
""", unsafe_allow_html=True)


# --- App Layout ---

st.title("💡 Sustainable Energy Monitor")
st.caption("Monitor your home appliances' energy consumption and get smart recommendations!")

st.header("Appliance Usage")

# --- Appliance Input Rows ---
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text_input("Appliance Name #1", "Refrigerator")
    with col2:
        st.number_input("Wattage (W) #1", value=200, min_value=0)
    with col3:
        st.number_input("Duration (hrs) #1", value=18.0, min_value=0.0, step=0.5, format="%.2f")

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text_input("Appliance Name #2", "Air Conditioner")
    with col2:
        st.number_input("Wattage (W) #2", value=800, min_value=0)
    with col3:
        st.number_input("Duration (hrs) #2", value=6.0, min_value=0.0, step=0.5, format="%.2f")
        
st.button("➕ Add Appliance")


st.header("Upload Past Electricity Bills")
st.file_uploader(
    "Upload electricity bill files (PDF, image, or CSV)",
    type=['pdf', 'png', 'jpg', 'jpeg', 'csv'],
    accept_multiple_files=True
)

st.header("Suggestions & Savings (ML)")
st.info("After entering your appliance usage and uploading bills, click 'Analyze' to get smart recommendations.")

if st.button("Analyze", type="primary"):
    with st.spinner("Analyzing your data..."):
        # Placeholder for your analysis logic
        import time
        time.sleep(3)
        st.success("Analysis complete! See recommendations below.")
        st.balloons()

st.markdown("---")
st.markdown("Made with ♥️ for sustainable living.")