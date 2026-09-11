import streamlit as st
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="MBBS 031 Terminal",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ MBBS 031: Clearance & Reality Terminal")
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
        
        # Checking for any combination of her names
        name_tokens = name_input.split()
        is_somto = any(token in name_input for token in ["somto", "somtochukwu", "enendu", "olivia"])
        
        if is_somto:
            st.success("✨ CLASSIFIED FILE: DIRECT MESSAGE TO THE INSPIRATION ✨")
            
            with st.spinner("Decrypting personal developer log..."):
                time.sleep(1.2) # Adds dramatic suspense
                
            # The Personal, Direct-Address Reveal
            st.markdown(f"""
            ---
            ### 📂 Open Letter to Enendu Somtochukwu Olivia
            
            Hey Somto / Olivia. If you are reading this right now, yes—this app was literally built because of you. 
            
            Remember back then? The awkward first conversations, trying to remember what "coy" means, and the total cold shoulder afterwards? Honestly, it hurt back then. But looking back now, I realized something funny: **If you didn't give me that heavy attitude, would I have ever pushed myself to learn Python, build web apps, and code this?** Probably not. 
            
            So in a weird way, thank you. You were the catalyst. Even now, I still think about you—not for pleasure or any romantic drama, but as a reminder of rejection, disassociation, and how to channel pain into pure personal power. I'm still rooting for you, wherever you go, but I've officially upgraded my own operating system.
            
            > **Developer Note:** *"Though I went through hard times just over Somtochukwu alone 😂, how on earth am I going to manage the entire MBBS 031 class? 🫴😅 That is life and part of the journey—everybody can't like me, and I've finally accepted that in my head. App built, deployed, and mastered."*
            ---
            """)
            st.balloons()
            
        else:
            # Standard output for anyone else in MBBS 031
            st.success(f"Access Verified for: **{user_query}**")
            st.write("Status: Verified MBBS 031 course mate profile active. Cleared for CBT exams, long lecture hours, surviving group practicals, and general medical school survival.")
            st.info("No custom plot-twist logs found for this user. You're safe!")

# ==========================================
# 4. FOOTER
# ==========================================
st.write("---")
st.markdown("<div style='text-align: center; color: gray;'>Engineered for MBBS 031 with Grit, Code, and Total Acceptance</div>", unsafe_allow_html=True)
