import streamlit as st
import platform

# --- Start Debugging ---
st.set_page_config(layout="wide")
st.title("App Debugger 🐛")
st.write(f"--- Step 1: App has started. ---")
st.write(f"Python version: {platform.python_version()}")
st.write(f"Streamlit version: {st.__version__}")

try:
    st.write("--- Step 2: Attempting to import OpenAI... ---")
    from openai import OpenAI
    st.write(f"✅ SUCCESS: OpenAI imported.")
except Exception as e:
    st.error(f"❌ FAILED at Step 2 (Import): {e}")
    st.write("This means 'openai' is not installed correctly. Check requirements.txt.")
    st.stop()

try:
    st.write("--- Step 3: Attempting to read secret 'OPENAI_API_KEY'... ---")
    my_key = st.secrets["OPENAI_API_KEY"]
    st.write("✅ SUCCESS: Secret read from st.secrets.")
    
    if not my_key:
         st.error("❌ FAILED: 'OPENAI_API_KEY' exists but is EMPTY.")
         st.stop()
    elif "sk-" not in my_key:
         st.error("❌ FAILED: The value for 'OPENAI_API_KEY' does not look like a valid key.")
         st.stop()
    else:
         st.write("Key appears to be a valid format (starts with 'sk-').")

except KeyError:
    st.error("❌ FAILED: 'OPENAI_API_KEY' NOT FOUND in st.secrets.")
    st.write("This is a 'KeyError'. It means the secret name does not exist or has a typo.")
    st.write("Go to Settings > Secrets and make sure the name is 100% correct.")
    st.stop()
except Exception as e:
    st.error(f"❌ FAILED at Step 3 (Unknown Error): {e}")
    st.stop()

try:
    st.write("--- Step 4: Attempting to initialize OpenAI client... ---")
    client = OpenAI(api_key=my_key)
    st.write("✅ SUCCESS: OpenAI client initialized.")
except Exception as e:
    st.error(f"❌ FAILED at Step 4 (Client Init): {e}")
    st.write("This could be a bad API key or an OpenAI service issue.")
    st.stop()
    
st.success("--- App is fully initialized! If you see this, the problem is in your main app logic. ---")
st.divider()

# --- Your Original App Code (can be added back later) ---
# st.title("🤖 AI-Powered Story Generator")
# ...