import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client
# We proved in the debug test that this line works.
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except KeyError:
    st.error("OPENAI_API_KEY not found. Please add it to your Streamlit app's 'Secrets' settings.")
    st.stop()
except Exception as e:
    st.error(f"Error initializing OpenAI client: {e}")
    st.stop()

st.title("🤖 AI-Powered Story Generator")

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
                # Use the new chat completions endpoint
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a creative and professional storyteller."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.8,
                    max_tokens=1500
                )
                
                story = response.choices[0].message.content

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