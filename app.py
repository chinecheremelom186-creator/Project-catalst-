import streamlit as st
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Secure Clearance Terminal",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Departmental Clearance Terminal")
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
            st.error("⚠️ SYSTEM ALERT: ANOMALY DETECTED IN DATABASE ⚠️")
            
            with st.spinner("Decrypting restricted root-level developer logs..."):
                time.sleep(1.2) # Adds dramatic suspense
                
            st.success("Access Granted: Special Origin File Unlocked.")
            
            # The Easter Egg Reveal
            st.markdown("""
            ---
            ### 📂 Secret File: Project Catalyst
            * **Subject:** Somtochukwu
            * **Classification:** Elite Origin Source / Unofficial Muse
            
            #### 📊 System Activity Log:
            1. **Initial Vector:** Awkward initial greeting (Vocabulary error: *"Are you coy?"*).
            2. **Friction Event:** Prolonged social silence and campus cold shoulder.
            3. **The Core Transformation:** Severe emotional friction converted directly into raw programming power, Python syntax mastery, GitHub commits, and mobile-device debugging.
            
            > **Developer Note:** *"The silence wasn't a loss; it was the compilation error that forced me to rewrite my entire operating system. App built, deployed, and mastered."*
            ---
            """)
            st.balloons()
            
        else:
            # Standard output for anyone else
            st.success(f"Access Verified for: **{user_query}**")
            st.write("Status: Standard 100L student profile active. Cleared for CBT exams, long lecture hours, and general survival.")
            st.info("No anomalies or classified developer roots found for this user.")

# ==========================================
# 4. FOOTER
# ==========================================
st.write("---")
st.markdown("<div style='text-align: center; color: gray;'>System secured by Code & Spite</div>", unsafe_allow_html=True)
