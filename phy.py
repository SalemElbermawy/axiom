import streamlit as st


st.markdown(
    """
    <style>
   .stApp {
        background-color: rgba(54, 88, 97,0.3);
        color: rgb(0,0,0);

    }

    header[data-testid="stHeader"] {
    background: transparent;
    }


    
    </style>""",unsafe_allow_html=True)

tab1,tab2,tab3=st.tabs(["Tab_1","Tab_2","Tab_3"])

with tab1:
    pass

with tab2:
    pass

with tab3:
    pass