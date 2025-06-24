import streamlit as st
from factorial import fact


def main():
    st.title("Factorial Calculator")
    number = st.number_input("Enter a number:", min_value=0, max_value=900)
    if st.button("Calculate"):
        resutl = fact(number)
        st.write(f"The factorial of {number} is {resutl}")


if __name__ == "__main__":
    main()
