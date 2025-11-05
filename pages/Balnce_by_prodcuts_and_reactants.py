from chempy import balance_stoichiometry
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



# --------

st.markdown(f"""

<h2 style="margin-bottom:20px;">Balance By Prodcuts And Reactants ⚗️</h2>

""",unsafe_allow_html=True)

st.markdown("""

    <h5>Enter the reactance and set , after each one without space (HCl,NaOH)</h5>
            

""",unsafe_allow_html=True)
re_input=st.text_input("",key="reactance")

st.markdown("""

    <h5>Enter the products and set , after each one without space (H2O,NaCl)</h5>
            

""",unsafe_allow_html=True)


pr_inputs=st.text_input("",key="product")


re = set(x.strip() for x in re_input.split(",") if x.strip())
pr = set(x.strip() for x in pr_inputs.split(",") if x.strip())

if re_input and pr_inputs:
    re = set(x.strip() for x in re_input.split(",") if x.strip())
    pr = set(x.strip() for x in pr_inputs.split(",") if x.strip())

    try:
        reactants, products = balance_stoichiometry(re, pr)

        reactance_part = ""
        resltant_part = ""
        add_reactance = 1
        add_resultance = 1

        for x in reactants:
            reactance_part += f"{reactants[x]}{x}"
            if add_reactance < len(reactants):
                reactance_part += " + "
                add_reactance += 1
            else:
                reactance_part += " → "

        for z in products:
            resltant_part += f"{products[z]}{z}"
            if add_resultance < len(products):
                resltant_part += " + "
                add_resultance += 1
        final=st.button("Click To Balance",type="primary")
        if final:
            st.markdown(f"""
            <div style="background:rgba(120,120,120,0.5); padding:20px; border-radius:20px; text-align:center;">
                <h3 style="color:black;">{reactance_part} {resltant_part}</h3>
            </div>
            """, unsafe_allow_html=True)

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


                <h5 style=" margin-left:20px; margin-top:6px;color:black;">   ❌ Invalid input! Please check the compounds and try again.</h5>
    

                        
                </div>


    """,unsafe_allow_html=True)