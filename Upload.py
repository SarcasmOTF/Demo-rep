import streamlit as st
import speech_recognition as sr
recognizer = sr.Recognizer()

def main():
    st.title("My First Upload")
    
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    
    if st.button("Submit"):
        with sr.Microphone() as source:
                    #st.write("Listening....")
                    with st.spinner("Listening..."):
                        audio = recognizer.listen(source)
        try:
                    text = recognizer.recognize_google(audio)
                    #message = st.chat_message("user")
                    #message.write(text)
                    st.write("User : ", text)
                    
        except sr.UnknownValueError:
                    st.error("Sorry, I could not understand.")
        #output = f"{first_name}: {last_name}"
        #st.write(output)

if __name__ == "__main__":
    main()