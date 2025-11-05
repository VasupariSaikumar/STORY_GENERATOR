import streamlit as st
import google.generativeai as genai

st.title("Google AI Model Debugger 🔬")

try:
    st.write("--- Step 1: Configuring Google AI client... ---")
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    st.write("✅ SUCCESS: Google AI client configured.")
except KeyError:
    st.error("❌ FAILED: 'GOOGLE_API_KEY' NOT FOUND in st.secrets.")
    st.write("Please check your Streamlit secrets again.")
    st.stop()
except Exception as e:
    st.error(f"❌ FAILED at Step 1 (Config): {e}")
    st.stop()

st.write("--- Step 2: Fetching available models... ---")
st.write("This will show all models your API key has access to.")

try:
    st.subheader("Available Models:")
    
    # This is the command from the error message: ListModels
    for m in genai.list_models():
        st.write(f"**Model Name:** `{m.name}`")
        st.write(f"**Supported Methods:** `{m.supported_generation_methods}`")
        st.divider()
        
    st.success("--- Model list complete. ---")
    st.info("Look for a model in the list above that includes **'generateContent'** in its supported methods. That is the exact name we must use.")
    
except Exception as e:
    st.error(f"❌ FAILED at Step 2 (ListModels): {e}")
    st.write("This could mean your API key is invalid or has no permissions.")