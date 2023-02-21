import streamlit as st 
import numpy as np 
import numpy.random 
import matplotlib.pyplot as plt
import pandas as pd

def create_random(A):
    x = np.arange(100)
    y = x * 2 + numpy.random.random(100)*A
    df = pd.DataFrame({'x': x, 'y':y}, dtype=np.float16)
    return df

st.set_page_config(layout="wide")

st.write(
    """
    # Random TS Generator

    This is a demo
    """
)

left_col, right_col = st.columns(2)
with left_col:
    A = st.slider('Shock', min_value=0, max_value=50, value=5)
    df = create_random(A)
    df


with right_col:
    st.write("""
    # Plot the line 
    """)

    st.line_chart(df, x='x', y= 'y')



