        # Checking for any combination of her names (Somto, Somtochukwu, Olivia, Enendu)
        name_tokens = name_input.split()
        
        is_somto = any(token in name_input for token in ["somto", "somtochukwu", "enendu", "olivia"])
        
        # To make sure it triggers specifically for her (e.g., if someone types just 'olivia' or 'somto')
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
