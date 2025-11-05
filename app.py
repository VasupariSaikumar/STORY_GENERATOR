import streamlit as st
import google.generativeai as genai
import os

# --- Client Initialization ---
try:
    # Configure the Google AI client from Streamlit secrets
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except KeyError:
    st.error("GOOGLE_API_KEY not found. Please add it to your Streamlit app's 'Secrets' settings.")
    st.stop()
except Exception as e:
    st.error(f"Error initializing Google AI client: {e}")
    st.stop()

# --- Model Setup ---
# Using a fast and capable model
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤖 AI-Powered Story Generator (Google AI)")

# --- User Inputs ---
genre = st.text_input("Enter a genre or theme (e.g., Fantasy, Mystery)")
mood = st.selectbox("Choose a mood:", ["Happy", "Dark", "Suspenseful", "Adventurous", "Romantic"])
length = st.slider("Select story length (approx. words):", 100, 1000, 500, 50)

# --- Button Logic ---
if st.button("Generate Story"):
    if not genre:
        st.error("Please enter a genre or theme to begin!")
    else:
        prompt = f"Write a {mood.lower()} story about {genre}. The story should be approximately {length} words long."
        
        with st.spinner("Generating your story... This might take a moment."):
            try:
                # This is the new API call
                response = model.generate_content(prompt)
                
                # This is the new way to get the text
                story = response.text

                # --- Display Results ---
                st.subheader("Here's Your Story:")
                st.write(story)
                
                st.download_button(
                    label="Download Story",
                    data=story,
                    file_name=f"{genre.lower().replace(' ','_')}_story.txt",
                    mime="text/plain"
                )
            
            except Exception as e:
                st.error(f"An error occurred: {e}")