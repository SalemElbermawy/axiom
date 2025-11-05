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
st.markdown(
    """
    <style>
    .custom-box {
        background: rgba(240, 5, 5,0.8);
        border-radius: 20px;
        padding: 20px;
        color: white;
        text-align: center;
    }
    </style>

    <div class="custom-box">
        <h2>🧪 Welcome To Your 🧠 Scientific Page ⚛️</h2>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("""

<div style="background:grey; border-radius:20px; padding:15px; margin-top:10px; margin-bottom:10px">
    <p style="margin:10px;color:rgb(0,1,1); font-weight:bold; font-size:20px"> Here where you can improve your way in studying by different web pages for different concepts in (Math 📐, CHEM ⚗️, PHY 📈📉, Mechanics🚀, BIO 🧬)</p>
</div>

""",unsafe_allow_html=True)
