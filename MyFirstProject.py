import streamlit as st


from PIL import Image
img = Image.open("Tracking.jpg")


st.image(img, width=500)

st.title ("SILVERLINING PACKAGE TRACKER")

st.header ("Tracking your Package Journey")


Name = st.text_input("Full Name", "Type Here ...")



State = st.selectbox("Select State: ",
                     ['Lagos', 'Ibadan', 'Abuja', 'Portharcourt', 'Enugu', 'Asaba', 'Kano'])

 
Address = st.text_input("Input Destination address", " ")


Package = st.text_input("Enter your Unique Package Code", "Type Here ...")

#if(st.button('Submit')):
    #result = Package.title()
    #st.success(result)


#if(st.button('Submit')):
    #result = Address.title()
    #st.success(result)
    
#Number = st.text_input("Input Phone number", "Type Here ...")

#if(st.button('Submit')):
    #result = number.title()
    #st.success(result)
    
#st.write ('Your package will arrive in the next 3 hours dear: ', Name.title())


if(st.button('Submit')):
    result = 'Hi ' + Name.title() + ', your package ' + Package.title() + ' is now at our head office. It will arrive on your doorstep in the next 3 hours.'
    #result1 = Package.title()
    #result2 = Address.title()
    st.success(result)
