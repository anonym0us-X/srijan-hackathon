import streamlit as st

# Set page config for wide, modern layout
st.set_page_config(page_title="Sustainable Energy Monitor", page_icon="💡", layout="wide")

st.title("💡 Sustainable Energy Monitor")
st.write("Monitor your home appliances' energy consumption and get smart recommendations!")

# Appliance input section
st.header("Appliance Usage")
appliance_entries = st.session_state.get('appliance_entries', 3)

# Store appliance data in session for dynamic rows
if 'appliances' not in st.session_state:
    st.session_state['appliances'] = [
        {'name': '', 'wattage': 1, 'duration': 0.0} for _ in range(appliance_entries)
    ]


# Function to add a new appliance input row
def add_appliance():
    st.session_state['appliances'].append({'name': '', 'wattage': 0, 'duration': 0})

# Iterate through appliances
for idx, appliance in enumerate(st.session_state['appliances']):
    cols = st.columns([3, 2, 2])
    with cols[0]:
        st.session_state['appliances'][idx]['name'] = st.text_input(f'Appliance Name #{idx+1}', value=appliance['name'], key=f'name_{idx}')
    with cols[1]:
        st.session_state['appliances'][idx]['wattage'] = st.number_input(f'Wattage (W) #{idx+1}', min_value=1, value=appliance['wattage'], key=f'wattage_{idx}')
    with cols[2]:
        st.session_state['appliances'][idx]['duration'] = st.number_input(f'Duration (hrs) #{idx+1}', min_value=0.0, value=appliance['duration'], step=0.1, key=f'duration_{idx}')
    st.markdown("---")  # Divider between entries

if st.button("➕ Add Appliance"):
    add_appliance()

# Historical bills upload section
st.header("Upload Past Electricity Bills")
uploaded_bills = st.file_uploader(
    "Upload electricity bill files (PDF, Image, or CSV)",
    type=['pdf', 'jpg', 'jpeg', 'png', 'csv'],
    accept_multiple_files=True
)

if uploaded_bills:
    st.success(f"{len(uploaded_bills)} bill(s) uploaded for analysis.")

# Instructions/Suggestions placeholder
st.header("Suggestions & Savings (ML)")
st.info("After entering your appliance usage and uploading bills, click 'Analyze' to get smart recommendations.")

if st.button("Analyze"):
    st.warning("This is a demo! Connect your backend/model here.")

st.write("---")
st.markdown("Made with ❤️ for sustainable living.")


# i am going to an hackathon, our project domain is sustainable energy. Our project is about ML model for continuous monitoring of the home appliances 
# with respect to the unit consumption so that we could send alerts to the user for any short time break off for saving electricity and thus also reducing the electricity bill.
#
# now i am responsible for creating a a basic front end for this. 
# the front end should include the thing like the appliance name, wattage and duration for which it is kept on. 
# Also there should be a section for adding older electricity bills so that the ML model can review them and give suggestion for saving electricity accordingly. 
# Now i am planning to make this front end using streamlit and python. 
# Your task is to make me a good front end, it should be catchy but professional looking. 
# I want a basic 3 compulsory appliances field and have a plus button so that user can add multiple appliances.
