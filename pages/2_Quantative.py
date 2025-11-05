import streamlit as st
from chempy import Substance




check=False
molar=None
molal=None

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
    <h1 style="text-align:center;">Quantative Chemistry</h1>
""",unsafe_allow_html=True)

st.markdown("""
    <h5>Choose Which Value You Want To Calcuate</h5>
""",unsafe_allow_html=True)
choice=st.selectbox("",options=["Molarity","Molality"])

if choice == "Molarity":
    st.markdown("""
    <h5> Enter the compound (Solute) of the solution </h5>
""",unsafe_allow_html=True)
    try:
        substance=st.text_input("")
        mass=Substance.from_formula(substance).mass
        check=True

    except Exception as e:
        if substance.strip() !="":
            st.markdown("""
    <div style="background:rgba(255,0,0,0.5); border-radius:20px; text-align:center;">
                        <h2>Invalid compound</h2>
                        </div>
    """,unsafe_allow_html=True)

    if check:
        st.markdown("""
        <h5>Enter the mass of substance in 'grams'</h5>
    """,unsafe_allow_html=True)
        mass_total=st.number_input("",min_value=0)
        st.markdown("""
        <h5>Enter the volume in 'L'</h5>
    """,unsafe_allow_html=True)
        liter=st.number_input("")

        moles=mass_total/mass
        if liter != 0:
            molar=moles/liter

        st.markdown(f"""

        <h6>Molarity = <span>{molar}</span></h6>


    """,unsafe_allow_html=True)

    

elif choice == "Molality":
    st.markdown("""
    <h5> Enter the compound (Solute) of the solution </h5>
""",unsafe_allow_html=True)
    try:
            substance=st.text_input("")
            mass=Substance.from_formula(substance).mass
            check=True

    except Exception as e:
        if substance.strip() !="":
            st.markdown("""
        <div style="background:rgba(255,0,0,0.5); border-radius:20px; text-align:center;">
                            <h2>Invalid compound</h2>
                            </div>
        """,unsafe_allow_html=True)

    if check:
        st.markdown("""
            <h5>Enter the mass of substance in 'grams'</h5>
        """,unsafe_allow_html=True)
        mass_total=st.number_input("",min_value=0)
        st.markdown("""
            <h5>Enter the weight in 'Kg'</h5>
        """,unsafe_allow_html=True)
        weight=st.number_input("")

        moles=mass_total/mass
        if weight != 0:
            molal=moles/weight

        st.markdown(f"""

            <h6>Molarity = <span>{molal}</span></h6>


        """,unsafe_allow_html=True)


st.markdown("""
<div style="margin-top:20px; padding:20px; background: rgba(120,120,120,0.5); border-radius:20px"> 
    <p>
            Molarity and Molality is the way to measure the concentration of solution <br>
            And this is most important in many fields such as the medecine or preparing any thin in the LAB <br>
            The summary is Molality we use it for the solution which affect by changing in volume <br>
            And the Molarity we use it for measure the concentration we need the volume in it.</p>
</div>
""",unsafe_allow_html=True)



