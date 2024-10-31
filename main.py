import streamlit as st
from encoding_techniques import nrz_l, nrz_i
from plot_utils import plot_signal
from data_validation import is_binary_string

st.title("Data Encoding Techniques")
st.write("Enter digital data (e.g., '101010') and select an encoding technique to visualize the output signal.")


data = st.text_input("Enter digital data (binary):")

# Select Encoding Technique
technique = st.selectbox("Select Encoding Technique", [
    "NRZ-L", "NRZ-I", "Bipolar AMI", "Pseudoternary", "Manchester", "Differential Manchester"
])


if st.button("Generate Signal") and data:
    # Validate input to be binary
    if is_binary_string(data):
        if technique == "NRZ-L":
            encoded_signal = nrz_l(data)
        elif technique == "NRZ-I":
            encoded_signal = nrz_i(data)

        # Plot and display the signal
        fig = plot_signal(encoded_signal, f"{technique} Encoding")
        st.pyplot(fig)
    else:
        st.error("Please enter a valid binary string.")


