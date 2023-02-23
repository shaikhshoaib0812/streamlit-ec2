import components.authenticate as authenticate
import streamlit as st

# Check authentication
authenticate.set_st_state_vars()
# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()

if (st.session_state["authenticated"]):
    if("GroupOne" in st.session_state["user_cognito_groups"]):
        if st.button('Wish Hello'):
            st.write("""
            # Streamlit App
            Hello *Group 1 !*
            """)
        else:
            st.write('')
    elif("GroupTwo" in st.session_state["user_cognito_groups"]):
        if st.button('Wish Hello'):
            st.write("""
            # Streamlit App
            Hello *Group 2 !*
            """)
        else:
            st.write('')
    else:
        if st.button('Wish Hello'):
            st.write("""
            # Streamlit App
            Hello *External User !*
            """)
        else:
            st.write('')
else:
    st.write("Please login!")

