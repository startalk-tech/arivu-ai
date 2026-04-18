import streamlit as st
from google import genai

# Arivu AI Web Layout
st.set_page_config(page_title="Arivu AI", page_icon="🧠")
st.title("🧠 Arivu AI")
st.caption("Startalk Technologies - വിജ്ഞാനം എല്ലാവർക്കും")

# API Key - ഇത് പിന്നീട് സുരക്ഷിതമായി സെറ്റ് ചെയ്യാം
MY_API_KEY = st.secrets.get("GEMINI_API_KEY", "no_key")

if MY_API_KEY == "no_key":
    st.warning("API Key സെറ്റ് ചെയ്തിട്ടില്ല. ദയവായി കാത്തിരിക്കുക...")
else:
    try:
        client = genai.Client(api_key=MY_API_KEY)
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input("നിങ്ങൾക്ക് എന്ത് അറിയണം?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

            response = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.chat_message("assistant").write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
      
