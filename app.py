import streamlit as st

st.subheader("Safety Check")
age = st.slider('What is your battery level?', 0, 100, 100)
st.write("My energy is at ", age, '%')

if st.button('Send', type='primary'):
    st.write('Sent!')

st.caption("This information is used to prevent work injuries and illnesses")
