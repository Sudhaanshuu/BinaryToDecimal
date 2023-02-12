import json
import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 = st.columns(2)
with col1:

    st.markdown("""## Binary code Converter by Sudhanshu""")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


with col1:
    lottie_now = load_lottiefile("file/code.json")
st_lottie(
    lottie_now,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height=300,
    key=None,

)

st.success("Choose one of them")
op1 = "Binary to Decimal"
op2 = "Decimal to Binary"
selected_option = st.radio((""), (op1, op2))

if selected_option == op1:
        binary = int(st.text_input("Enter that binary code"))
        decimal = 0
        binary = str(binary)
        for digit in binary:
            decimal = decimal*2 + int(digit)
        st.write("The decimal equivalent is")
        st.success(decimal)
elif selected_option == op2:
        decimal = int(st.text_input("Enter that decimal number"))
        if decimal == 0:
            binary = "0"
        else:
            binary = ""
            while decimal > 0:
                binary = str(decimal % 2) + binary
                decimal = decimal // 2
        st.write("The binary equivalent is")
        st.success(binary)
else:
        st.warning("Invalid choice. Please try again.")
