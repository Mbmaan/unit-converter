import streamlit as st


def convert_units(value: float, unit_from: str, unit_to: str):
     
     if unit_from == "kilometers" and unit_to == "meters":
          return value * 1000
     elif unit_from == "meters" and unit_to == "kilometers":
          return value * 0.001
     elif unit_from == "kilograms" and unit_to == "grams":
          return value * 1000
     elif unit_from == "grams" and unit_to == "kilograms":
          return value * 0.001
     else: 
          return "conversion is not supported"
     
def main():
     st.title("Unit Converter")
     st.write("Welcome to Unit Converter")
     value = st.number_input("Enter the value you want to convert:", min_value=0.0)
     unit_from = st.text_input("Enter the value you want to convert from:(e.g. meters, kilometers, grams, kilograms)")
     unit_to = st.text_input("Enter the value you want from convertion:(e.g. meters, kilometers, grams, kilograms)")
    

     if st.button("Convert"):
       result = convert_units(value, unit_from, unit_to)
       st.write("converted value is:", result )


main ()     
