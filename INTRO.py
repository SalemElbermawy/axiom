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
        background: rgb(240, 5, 5);
        border-radius: 20px;
        padding: 20px;
        color: white;
        text-align: center;
    }
    </style>

    <div class="custom-box">
        <h2> Welcome To Your Scientific Page !</h2>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("""

    <div style="background:grey; border-radius:20px; padding:15px; margin-top:10px; margin-bottom:10px">
            <h2>First Page</h2>
            <p style="margin:10px;color:rgb(0,1,1);">You Can enter any element and compound which you want and you will get the most important about it <br>
            Such as Molar Mass, Charge of it, and Formula
            </p>
            </div>

""",unsafe_allow_html=True)

st.markdown("""

    <div style="background:rgb(240,5,5); border-radius:20px; padding:15px; margin-top:10px; margin-bottom:10px">
            <h2>Second Page</h2>
            <p style="margin:10px; ">You can enter just the reactant and product without any COE and you will get the full equation <br>
            for your chemical equation
            </p>
            </div>

""",unsafe_allow_html=True)

st.markdown("""
    <div style="background:green; border-radius:20px; padding:15px; margin-top:10px; margin-bottom:10px; ">
            <h2> Third Page </h2>
            <p style="margin:10px;"> In this page you can write your organic compound by 'smile formula' and you will show <br>
            2D structure of it 
            </p>            
            </div>
""",unsafe_allow_html=True)


st.markdown("""
<div style="background:red; margin-top:10px; margin-bottom:10px; border-radius:20px; padding:15px;">
            
<h2>Fourth Page</h2>
<p style=" margin:10px; ">You will enter just three values of just three values and you will get the another two value </p>

</div>
            
""",unsafe_allow_html=True)

#  edit design from here
st.markdown("""
<div style="background:grey; padding:15px; border-radius:20px; margin-top:10px; margin-bottom:10px; ">
    <h2> Fifth Page </h2>
    <p style="margin:10px; ">You can enter the values of the vector and you will get the value of croos product and dot product of these two vectors</p>
        
                
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div  style="background:blue; padding:15px; border-radius:20px; margin-top:10px; margin-bottom:10px;">
    <h2>Sixth Page</h2>
    <p style="margin:10px"> Enter the number of vriables which you have in equation of first degree and you will get the value of each one <br>
            You can use that in many of thinks specially when you solve closed electric circuts
            </p>
</div>      
""",unsafe_allow_html=True)

st.markdown("""
<div style="background:black; color:white; padding:15px; border-radius:20px; margin-top:10px; margin-bottom:10px; ">
            <h2> Seventh Page</h2>
            <p style="margin:10px;">You Can enter CEOs of the equation in second degree and you will get the roots of this equation or function</p>
</div>
""",unsafe_allow_html=True)


st.markdown("""
    <div style="background:red; color:black; padding:15px; margin-top:10px; border-radius:20px;">
            <h2> Eightth Page </h2>
            <p style="margin:10px;">You can just add the compound of the solution and the web will calcuate the molar mass directly <br>
            After that you should set the mass of solute and the volume of solution</p>
            </div>
""",unsafe_allow_html=True)
