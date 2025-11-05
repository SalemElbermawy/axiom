from rdkit import Chem
from rdkit.Chem import Draw

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

st.markdown("""
        <h2>Simulation For Organic Compounds </h2>
        <p> You must add the molecule at this formula 'Smile Formula' to get the structure of your cmpound <br>
            This an example of it <span style="font-weight:bold;">C(C(C1C(C(C(O1)(O)CO)O)O)O)O</span>
            </p>
""",unsafe_allow_html=True)

# qs
st.markdown("""
    <h3>Enter Your compond and please follow the rules to get the better result</h3>
""",unsafe_allow_html=True)

compound=st.text_input("")



if compound.strip():
    try:
        m = Chem.MolFromSmiles(compound)

        img = Draw.MolToImage(m, size=(400, 400), kekulize=True, wedgeBonds=True)

        st.image(img, caption="2D molecule view")

    except Exception as e:
        
        st.markdown(f"""
                        <div style="
                            background-color: rgba(255, 230, 150, 0.2);
                            border: 2.6px solid #FFD700;
                            border-radius:27px;
                            color: #FFD700;
                            font-weight:bold;
                            font-size:23px;
                            text-align:center;
                                ">


                        <h5 style=" margin-left:20px; margin-top:6px">   ❌ Invalid input! Please check the compounds and try again.</h5>
                    
                        <p>You can use this example to show how it work copy this 'NCCCC(C(=O)O)N'</p>
            

                                
                        </div>


            """,unsafe_allow_html=True)