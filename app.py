import streamlit as st

# Simple function : isko test me use krna h 

def add_numbers(a: int, b: int) -> int:
    return a + b

st.title("My First CI/CD Streamlit App")
st.write(
    "ye app Githb  Actions sw test ho rhi h, aur streamlit Cloud se auto-deploy!"
)

x = st.number_input("Enter first number", value=1)
y = st.number_input("Enter second number", value=2)


if st.button("Add"):
    result = add_numbers(x, y)
    st.success(f"Result: {result}")