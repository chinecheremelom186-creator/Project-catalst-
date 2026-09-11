import streamlit as st
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="System Clearance Portal",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Departmental Clearance Terminal")
st.caption("Restricted Portal | 100L Medical Surgery Database")
st.write("---")

# ==========================================
# 2. INTERACTIVE QUERY INTERFACE
# ==========================================
st.info("Enter identity credentials below to query system access logs.")

with st.form("clearance_form"):
    user_query = st.text_input("Enter Full Name / Alias:", placeholder="Type a name to check database...")
    submit_clearance = st.form_submit_button("🔍 Execute Query")

# ==========================================
# 3. LOGIC & CONDITIONAL REVEAL
# ==========================================
if submit_clearance:
    if not user_query.strip():
        st.warning("⚠️ Please input a valid name before running the query.")
    else:
        name_input = user_query.strip().lower()
        
        # Checking if the special name is entered
        if "somto" in name_input or "somtochukwu" in name_input:
            st.success("✨ SPECIAL RECORD FOUND: PLOT TWIST CATALYST ✨")
            
            with st.spinner("Accessing origin milestone logs..."):
                time.sleep(1.2) # Adds dramatic suspense
                
            # The Confident, High-Value Easter Egg Reveal
            st.markdown("""
            ---
            ### 📂 Milestone File: The Origin of Power
            * **Subject:** Somtochukwu
            * **Status:** Unintentional Muse & Coding Catalyst
            
            #### 📊 Growth & Development Log:
            1. **The Encounter:** An unforgettable first attempt at conversation (complete with vocabulary tests like *"Are you coy?"*).
            2. **The Plot Twist:** Navigating the unpredictable social dynamics of 100L Med-Surg.
            3. **The Transformation:** Channeling all that energy away from social stress and straight into mastering Python, GitHub deployments, and building web apps.
            
            > **Developer Note:** *"Looking back, every awkward silence and closed door was just the universe forcing me to level up. What started as frustration turned into a genuine passion for programming. App built, deployed, and mastered with zero regrets."*
            ---
            """)
            st.balloons()
            
        else:
            # Standard output for anyone else
            st.success(f"Access Verified for: **{user_query}**")
            st.write("Status: Standard 100L student profile active. Cleared for CBT exams, long lecture hours, and general survival.")
            st.info("No custom milestone logs found for this user.")

# ==========================================
# 4. FOOTER
# ==========================================
st.write("---")
st.markdown("<div style='text-align: center; color: gray;'>Engineered with Grit, Code, and Growth</div>", unsafe_allow_html=True)
