import sympy as sp
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



v, u, a, t, s = sp.symbols("v u a t s")

eq1 = sp.Eq(v, u + a*t)
eq2 = sp.Eq(s, u*t + 0.5*a*t**2)
eq3 = sp.Eq(v**2, u**2 + 2*a*s)

st.markdown("""
    <h1 style="text-align:center;">
        <span style="color:red;">S</span>
        <span style="color:black;">U</span>
        <span style="color:orange;">V</span>
        <span style="color:green;">A</span>
        <span style="color:blue;">T</span>
    </h1>
    <h4 style="text-align:center;">Enter 3 known values to get the other 2</h4>
""", unsafe_allow_html=True)

options = ["Time", "Initial Velocity", "Final Velocity", "Acceleration", "Displacement"]
chosen = st.multiselect("Choose 3 knowns:", options)

def get_value(label, key):
    val = st.text_input(f"Set {label}", key=key)
    if val.strip() == "":
        return None
    try:
        return float(val)
    except ValueError:
        st.warning(f"{label} must be a number.")
        return None

values = {}
if "Time" in chosen:
    values[t] = get_value("t (Time)", "t")
if "Initial Velocity" in chosen:
    values[u] = get_value("u (Initial Velocity)", "u")
if "Final Velocity" in chosen:
    values[v] = get_value("v (Final Velocity)", "v")
if "Acceleration" in chosen:
    values[a] = get_value("a (Acceleration)", "a")
if "Displacement" in chosen:
    values[s] = get_value("s (Displacement)", "s")

if len(chosen) == 3 and all(v is not None for v in values.values()):
    known = list(values.keys())
    unknowns = [x for x in [v, u, a, t, s] if x not in known]

    subs = {k: val for k, val in values.items()}
    equations = [eq1, eq2, eq3]
    result = None

    for i in range(len(equations)):
        for j in range(i + 1, len(equations)):
            try:
                sol = sp.solve([equations[i].subs(subs),
                                equations[j].subs(subs)], unknowns, dict=True)
                if sol:
                    result = sol
                    break
            except Exception:
                pass
        if result:
            break

    if result:
        st.success("✅ Results:")
        for res in result:
            for k, val in res.items():
                st.markdown(f"""
                    <div style='background:#2c3e50; padding:10px; border-radius:15px; text-align:center; margin:5px;'>
                        <h4 style='color:white;'>{k} = {round(float(val),4)}</h4>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Couldn't solve with these 3 values — check your inputs.")
elif len(chosen) == 3:
    st.warning("⚠️ Please fill all 3 values.")
else:
    st.info("Please choose exactly 3 values.")
