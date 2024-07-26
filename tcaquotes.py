import streamlit as st
import random

def get_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return random.choice(lines).strip()

def main():
    st.title("The Creative Act Quote Generator")

    file_path = "tca_quotes.txt"  # Replace with your actual file path

    if st.button("Generate"):
        random_line = get_random_line(file_path)
        st.subheader(random_line)

if __name__ == "__main__":
    main()
