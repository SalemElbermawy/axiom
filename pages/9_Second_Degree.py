import streamlit as st
import sympy as sp

# cong page 

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

    <h1 style="text-align:center"> Sovle equation of seond degree </h1>

""",unsafe_allow_html=True)

st.markdown("""
 <p style="text-align:center; font-size:16px;"> You just add The COEs of variables and you will get the solution set </p>
""",unsafe_allow_html=True)

# prepare inputs for user

st.markdown("""
<h6>Enter the coe of x^2</h6>
""",unsafe_allow_html=True)

coe_x_2=st.number_input("",key="second",)

st.markdown("""
    <h6>Enter the coe of x</h6>
""",unsafe_allow_html=True)

coe_x_1=st.number_input("",key="first")

st.markdown("""
    <h6>Enter the value of abslute 'a0'</h6>
""",unsafe_allow_html=True)

abslute=st.number_input("",key="abs")

st.markdown("""

   <h4 style="text-align:center;"> You should set your function as that ( f(x) = x^2 + x - c ) </h4>

""",unsafe_allow_html=True)


# set symbols

x=sp.Symbol("x")
a=sp.Symbol("a")

# set equation

eq=sp.Eq(coe_x_2*(x)**2+coe_x_1*(x)+a,0)


eq_sub=eq.subs({a:abslute})

result=sp.solve(eq_sub,x)

# container of the result

st.markdown(f"""

    <div style="background:rgba(120,120,120,0.5); text-align:center; padding:10px; border-radius:27px"> <h5> ( {result} ) </h5> </div>
 
""",unsafe_allow_html=True)

