import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.markdown("""
<h1 style="padding:20px; text-align:center; background: rgba(120,120,120,0.5); border-radius:20px">Projectile Motion</h1 >
""",unsafe_allow_html=True)

st.sidebar.header("Simulation Parameters")

initial_velocity = st.sidebar.slider("Initial velocity (m/s)", 1, 100, 50)
launch_angle = st.sidebar.slider("Launch Angle (degrees)", min_value=0, max_value=90, value=45)
gravity = st.sidebar.slider("Gravity (m/s²)", max_value=20, min_value=1, value=9)
initial_height = st.sidebar.slider("Initial Height (m)", 0, 100, 0)

theta = np.radians(launch_angle)

vx = initial_velocity * np.cos(theta)
vy = initial_velocity * np.sin(theta)

if vy**2 + 2 * gravity * initial_height < 0:
    st.error("Invalid parameters - projectile cannot be launched!")
    st.stop()

peak_time = vy / gravity
peak_height = initial_height + (vy**2) / (2 * gravity)
time_ground = (vy + np.sqrt(vy**2 + 2 * gravity * initial_height)) / gravity
time_total = time_ground
range_x = vx * time_total

t = np.linspace(0, time_total, 1000)
x = vx * t
y = initial_height + vy * t - 0.5 * gravity * t**2
y = np.maximum(y, 0)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Trajectory Plot")

    fig, ax = plt.subplots(figsize=(20, 20))  
    ax.plot(x, y, "b-", linewidth=2, label="Trajectory")
    ax.fill_between(x, y, alpha=0.3)
    ax.set_xlabel("Horizontal Distance (m)")
    ax.set_ylabel("Vertical Height (m)")
    ax.set_title("Projectile Trajectory")
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_ylim(bottom=0)
    ax.plot(range_x, 0, 'ro', markersize=8, label="Landing Point")
    ax.plot(vx * peak_time, peak_height, 'go', markersize=8, label='Max Height')
    st.pyplot(fig)

with col2:
    st.subheader("Simulator Result")
    metrics_data = {
        "Parameter": [
            "Maximum Height",
            "Total Range",
            "Time Of Flight",
            "Time To Reach Max Height",
            "Horizontal Velocity",
            "Initial Vertical Velocity"
        ],
        "Value": [
            f"{peak_height:.2f} m",
            f"{range_x:.2f} m",
            f"{time_total:.2f} s",  
            f"{peak_time:.2f} s",  
            f"{vx:.2f} m/s",
            f"{vy:.2f} m/s"
        ]
    }

    metrics_df = pd.DataFrame(metrics_data)
    st.table(metrics_df)
    
    st.subheader("Real Time Position")
    time_slider = st.slider("Time (s)", 0.0, float(time_total), 0.0, 0.1)

    current_x = vx * time_slider
    current_y = initial_height + vy * time_slider - 0.5 * gravity * time_slider**2
    current_y = max(current_y, 0)
    
    st.metric("Horizontal Position", f"{current_x:.2f} m")
    st.metric("Vertical Position", f"{current_y:.2f} m")  

    current_vy = vy - gravity * time_slider
    speed = np.sqrt(vx**2 + current_vy**2)

    st.metric("Current Speed", f"{speed:.2f} m/s")
    st.metric("Vertical Velocity", f"{current_vy:.2f} m/s")

if st.sidebar.checkbox("Show Data Table"):
    st.subheader("Trajectory Data")
    data = pd.DataFrame({
        "Time (s)": t,
        "X Position (m)": x,
        "Y Position (m)": y
    })
    st.dataframe(data.head(25))