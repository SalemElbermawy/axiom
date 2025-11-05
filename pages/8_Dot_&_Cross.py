import streamlit as st

import  sympy as sp

vec_1=None
vec_2=None



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



# introduction

st.markdown("""
    <h1 style="text-align:center;">Cross & Dot Product</h1>
            

""",unsafe_allow_html=True)



st.markdown("""
    <p style="text-align:center; font-size:20px;"> Enter the vector of vector (A) and vector (B) <br>
            Then you will get the each result</p>
""",unsafe_allow_html=True)

a1=sp.Symbol("a1")
a2=sp.Symbol("a2")
a3=sp.Symbol("a3")

b1=sp.Symbol("b1")
b2=sp.Symbol("b2")
b3=sp.Symbol("b3")

st.markdown("""

    <p style="font-size:18px; font-weight:bold;">Please inter in each box the vector by this way <span stytle="font-weight:bold;">a1,a2,a3</span></p>
""",unsafe_allow_html=True)

A=sp.Matrix([a1,a2,a3])
B=sp.Matrix([b1,b2,b3])


# inputs_part
st.markdown("""
    <h4 style="text-align=center">Enter the value of the Vector "A" </h4>
""",unsafe_allow_html=True)

values_a=st.text_input("",key="A")

if values_a.strip() != "":
    values_a=values_a.strip()
    vec_1=values_a.split(",")
    

print(vec_1)

st.markdown("""
    <h4 style="text-align=center">Enter the value of the Vector "B" </h4>
""",unsafe_allow_html=True)

values_b=st.text_input("",key="B")

if values_b.strip() != "":
    values_b=values_b.strip()
    vec_2=values_b.split(",")
if vec_1 is not None and vec_2 is not None:

    try:

        sub_A=A.subs({
            a1:float(vec_1[0]),
            a2:float(vec_1[1]),
            a3:float(vec_1[2])
        })



        sub_B=B.subs({
            b1:float(vec_2[0]),
            b2:float(vec_2[1]),
            b3:float(vec_2[2])
        })

        # choose (dot nor cross and all info)
        dot_result=sub_A.dot(sub_B)
        st.markdown(f"""
    <div>
        <h5>The Value of A.B = {dot_result}</h5>           
    </div>
    """,unsafe_allow_html=True)
        cross_result=sub_A.cross(sub_B)

        x_cor=cross_result[0]
        y_cor=cross_result[1]
        z_cor=cross_result[2]
        norm=sp.sqrt((x_cor)**2+(y_cor)**2+(z_cor)**2)

        st.markdown(f"""
    <div> 
                    <h5>Vector of AxB = ({x_cor}, {y_cor}, {z_cor})</h5>
                    <h3> The magnitude of AxB = {norm} </h3>
                    <h5> Unit Vector of AxB = ({x_cor/norm},{y_cor/norm},{z_cor/norm}) </h5>
    </div>
    """,unsafe_allow_html=True)
    
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


                <h5 style=" margin-left:20px; margin-top:6px;color:black;">   ❌ Invalid input! Please check all values are numbers.</h5>
    

                        
                </div>


    """,unsafe_allow_html=True)






