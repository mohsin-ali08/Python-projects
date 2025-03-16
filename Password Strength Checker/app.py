import streamlit as st
import re
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("Passowrd Strength Checker")
st.markdown("""
            ## Welcome to the ultimate password strength checker !
             use this simple tool to check the strength of your password and get suggestions on how to make it stronger
             we will give you helpful tips to create a **Strong Password** """)

password = st.text_input("Enter your password ", type="password")

feedback = []

score = 0

if password :
    if len(password) >= 8 :
        score +=1      
    else:
        feedback.append("❌ Password should be at least 8 character long .")
    
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("❌ Password should be contain uper and lower case characters .")
    if re.search(r"\d",password):
        score +=1
    else:
        feedback.append("❌ Password should contain at least one digit .")
    if re.search(r"[!@#$%&]",password):
        score +=1
    else:
        feedback.append("❌ Password should contain at least one digit special character [!@#$%&]  .")
    
    if (score == 4):
        feedback.append("✅ Your password is strong ")
    elif(score == 3):
        feedback.append("😶 Your password is medium strength . It could be stronger ")
    else :
        feedback.append("🎈 Your password is week . Please make it stronger ")
        
    if feedback :
        st.markdown("## Imporovement Suggestions ")
        for tip in feedback : 
            st.write(tip)
else :
    st.info("Please Enter Your Password to get started ")
   