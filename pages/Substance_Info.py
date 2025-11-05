from chempy import Substance
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


    
    </style>

    """,unsafe_allow_html=True

)
st.markdown("""

    <h3 style=" margin-left:40px ; ">Enter the substance or molecule:</h3>

""",unsafe_allow_html=True)
substance = st.text_input("")

def details(input_substance):
    try:
        substance_formula = Substance.from_formula(input_substance)
        
        formula = substance_formula.unicode_name
        molar_mass = substance_formula.molar_mass()
        charge = substance_formula.charge
        latex = substance_formula.latex_name

        return [formula, molar_mass, charge, latex]

    except Exception as e:
        st.markdown(f"""
            <div style="
                background-color: rgba(255, 230, 150, 0.2);
                border: 2.6px solid #FFD700;
                border-radius:27px;
                color: #FFD700;
                font-weight:bold;
                font-size:23px;
                    ">


               <h5 style=" margin-left:20px; margin-top:6px; color:black;">⚠️ Invalid substance '<span style="color:#FF6347;">{input_substance}</span>' — please check the formula.</h5>
   

                    
            </div>


""",unsafe_allow_html=True)
        return None

if substance:
    list_info=details(substance)
    if list_info:
        st.write(f"The formula is {list_info[0]}")

        st.markdown(f"<h2>The molar mass of {list_info[0]} is {list_info[1]}</h2>", unsafe_allow_html=True)

        st.write(f"The charge of {list_info[0]} is {list_info[2]} ")

        st.write(f"If you will write it in the research paper or something like that this is the latex code {list_info[-1]}")


        #part of simulation
        