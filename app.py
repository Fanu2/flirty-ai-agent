import streamlit as st
from mistralai import Mistral
from utils import copy_to_clipboard, download_button  # Make sure utils.py has these functions
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")

def create_text_agent(api_key):
    try:
        client = Mistral(api_key=api_key)
        try:
            agent = client.beta.agents.create(
                model="mistral-large",
                name="Flirty Text Agent",
                description="Generates romantic and flirty messages",
                instructions="Generate charming romantic texts.",
                tools=[],
                completion_args={"temperature": 0.7, "top_p": 0.95},
            )
        except Exception as e:
            st.warning(f"Primary model 'mistral-large' failed: {e}. Falling back to 'mistral-medium-latest'.")
            agent = client.beta.agents.create(
                model="mistral-medium-latest",
                name="Flirty Text Agent",
                description="Generates romantic and flirty messages",
                instructions="Generate charming romantic texts.",
                tools=[],
                completion_args={"temperature": 0.7, "top_p": 0.95},
            )
        return client, agent
    except Exception as e:
        st.error(f"Failed to create text agent: {e}")
        return None, None

def generate_flirty_message(client, agent, prompt):
    if not client or not agent:
        return "Agent not available."
    try:
        response = client.beta.conversations.start(
            agent_id=agent.id,
            inputs=prompt
        )
        # Assuming response.outputs contains a list of outputs with text
        message = ""
        for output in response.outputs:
            if hasattr(output, 'content'):
                if isinstance(output.content, str):
                    message += output.content
                elif isinstance(output.content, list):
                    for item in output.content:
                        if hasattr(item, 'get'):
                            message += item.get("text", "")
                        elif hasattr(item, 'text'):
                            message += item.text
        return message.strip()
    except Exception as e:
        return f"Error generating message: {e}"

def main():
    st.title("❤️ Flirty AI Agent - Romantic Messages ❤️")

    if not API_KEY:
        st.warning("Please set your MISTRAL_API_KEY in the .env file.")
        return

    client, agent = create_text_agent(API_KEY)
    prompt = st.text_area("Enter a prompt for a flirty romantic message:",
                         "Write a charming and romantic message to woo someone special.")
    if st.button("Generate Message"):
        with st.spinner("Generating flirty message..."):
            message = generate_flirty_message(client, agent, prompt)
            st.success("Here's your flirty message:")
            st.markdown(f"**{message}**")
            copy_to_clipboard(message)
            download_button(message, "flirty_message.txt", "Download Message")

if __name__ == "__main__":
    main()
