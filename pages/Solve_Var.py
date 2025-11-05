import streamlit as st
import sympy as sp



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


#



# add web page of it
"Solve equations in three values at maximum to solve something as closed ohm electric circut"

st.markdown("""
    <h1 style="text-align:center;"> Solve The Equation In One to Five Variables Of One Degree</h1>
""",unsafe_allow_html=True)

st.markdown("""

    <h5 style="text-align=center;">Enter the number of variables</h5>

""",unsafe_allow_html=True)

st.markdown("""
<div>
    <h3>Set your equations as that and input the values (X+Y+Z=a)</h3>
    <h6>You will enter the CEOs of the vriables and value of 'a'</h6>       
</div>
""",unsafe_allow_html=True)


number_variables=st.selectbox("",options=[1,2,3])


if number_variables == 1:
    x=sp.Symbol("x")
    a0=sp.Symbol("a")
    st.markdown("""
<h5>Enter the value of x</h5>
""",unsafe_allow_html=True)
    x_in=st.number_input("",key="x")
    st.markdown("""
<h5>Enter the value of a0</h5>
""",unsafe_allow_html=True)
    a_in=st.number_input("",key="a")
    eq=sp.Eq(x_in*x,a0)
    eq_sub=eq.subs({
        a0:a_in 
    })
    result=sp.solve(eq_sub,x)
    st.markdown(f"""
<h4>The value of x is {result}</h4>

""",unsafe_allow_html=True)

elif number_variables ==2:

    x=sp.Symbol("x")
    y=sp.Symbol("y")
    a0=sp.Symbol("a")
    st.markdown("""
<h3 style="text-align:center">First Equation</h3>
""",unsafe_allow_html=True)
    x_in=st.number_input("enter the value of x of the first equation")
    y_in=st.number_input("enter the value of y of the first equation")
    a_in=st.number_input("enter the value of a of the first equation")
    eq_1=sp.Eq(x_in*x+y_in*y,a0)

    eq_sub_1=eq_1.subs({
        a0:a_in
    })


    st.markdown("""
<h3 style="text-align:center">Second Equation</h3>
""",unsafe_allow_html=True)

    x_in_2=st.number_input("enter the value of x of the second equation")
    y_in_2=st.number_input("enter the value of y of the second equation")
    a_in_2=st.number_input("enter the value of a of the second equation")

    eq_2=sp.Eq(x_in_2*x+y_in*y,a0)
    eq_sub_2=eq_2.subs({a0:a_in_2})
# result
    result=sp.solve((eq_sub_1,eq_sub_2),(x,y))
    st.markdown(f"""
<h4>The value of x is {result}</h4>

""",unsafe_allow_html=True)

    


elif number_variables == 3:
    x=sp.Symbol("x")
    y=sp.Symbol("y")
    z=sp.Symbol("z")
    a0=sp.Symbol("a")


    st.markdown("""
<h3 style="text-align:center">First Equation</h3>
""",unsafe_allow_html=True)
    x_in=st.number_input("enter the value of x of first equation")
    y_in=st.number_input("enter the value of y of first equation")
    z_in=st.number_input("enter the value of z of first equation")
    a_in=st.number_input("enter the value of a of first equation")

    eq_1=sp.Eq(x_in*x+y_in*y+z_in*z,a0)
    # first one is ready
    eq_sub_1=eq_1.subs({a0:a_in})


    st.markdown("""
<h3 style="text-align:center">Second Equation</h3>
""",unsafe_allow_html=True)
    x_in_2=st.number_input("enter the value of x of second equation")
    y_in_2=st.number_input("enter the value of y of second equation")
    z_in_2=st.number_input("enter the value of z of second equation")
    a_in_2=st.number_input("enter the value of a of second equation")

    eq_2=sp.Eq(x_in_2*x+y_in_2*y+z_in_2*z,a0)
    # second one is ready
    eq_sub_2=eq_2.subs({a0:a_in_2})

    st.markdown("""
<h3 style="text-align:center">Third Equation</h3>
""",unsafe_allow_html=True)
    x_in_3=st.number_input("enter the value of x of third equation")
    y_in_3=st.number_input("enter the value of y of third equation")
    z_in_3=st.number_input("enter the value of z of third equation")
    a_in_3=st.number_input("enter the value of a of third equation")

    eq_3=sp.Eq(x_in_3*x+y_in_3*y+z_in_3*z,a0)
    # second one is ready
    eq_sub_3=eq_3.subs({a0:a_in_3})

    result=sp.solve((eq_sub_1,eq_sub_2,eq_sub_3),(x,y,z))

    st.markdown(f"""
<h4>The value of x is {result}</h4>

""",unsafe_allow_html=True) 