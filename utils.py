import base64
import streamlit as st

def copy_to_clipboard(text: str, button_text: str = "Copy to clipboard"):
    if text:
        unique_key = f"copy_btn_{abs(hash(text)) % 10000}"
        # Escape backticks for JS template literal to avoid syntax errors
        escaped_text = text.replace('`', '\\`')

        js_code = f"""
        <script>
        function copyToClipboard{unique_key}() {{
            const el = document.createElement('textarea');
            el.value = `{escaped_text}`;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            alert('Copied to clipboard!');
        }}
        </script>
        <button onclick="copyToClipboard{unique_key}()">{button_text}</button>
        """
        st.components.v1.html(js_code, height=30)

def download_button(content: str, file_name: str, button_text: str):
    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{file_name}">{button_text}</a>'
    st.markdown(href, unsafe_allow_html=True)
