import streamlit as st

from PIL import image
img = image.open ("Tracking.jpg")

st.image(img, width=500)

st.title ("SILVERLINING PACKAGE TRACKER")

st.header ("Tracking your Package Journey")


Name = st.text_input("Input Destination address", "Type Here ...")

if(st.button('Submit')):
    result = Name.title()
    st.success(result)

State = st.selectbox("Select State: ",
                     ['Lagos', 'Ibadan', 'Abuja', 'Portharcourt', 'Enugu', 'Asaba', 'Kano'])
 

st.text("Enter your Unique Package Code")

Package = st.text_input("Enter your Unique Package Code", "Type Here ...")

if(st.button('Submit')):
    result = Package.title()
    st.success(result)
    
Address = st.text_input("Input Destination address", "Type Here ...")

if(st.button('Submit')):
    result = Address.title()
    st.success(result)
    
Number = st.text_input("Input Phone number", "Type Here ...")

if(st.button('Submit')):
    result = number.title()
    st.success(result)
    
st.write ('Your package will arrive in the next 3 hours dear: ', Name)
