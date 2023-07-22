import streamlit as st
import pandas as pd
import openai

st.set_page_config(page_title='AstroGPT', layout='wide', menu_items={
    'Get Help': 'https://www.linkedin.com/in/maazjamshaid/',
    'Report a bug': 'https://www.linkedin.com/in/maazjamshaid/',
    'About': 'by [Maaz Jamshaid](https://www.linkedin.com/in/maazjamshaid/), maaz@astroalgo.com'
})

key = "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"
openai.api_key = key

st.markdown('---')
col1, col2, col3 = st.columns(3)
with col2:
    st.title("$AstroGPT$")
st.markdown('---')

st.markdown("---")
name = st.text_input("Name")
date = st.date_input("Date", value=None)

st.markdown("---")

uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
  
    # Display the DataFrame
    st.dataframe(df)

    # Convert DataFrame to a string representation
    text = df.to_string(index=False)

    st.write(f"Token: {len(text)}")

    if st.button('ANALYZE'):
        messages = [{"role": "system", "content": f"Generate an analysis report based on the provided CSV file.\nName: {name}\nDate: {date}"}]

        def CustomChatGPT(user_input):
            messages.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            ChatGPT_reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": ChatGPT_reply})
            return ChatGPT_reply

        response = CustomChatGPT(text)
        st.text_area('AstroGPT:', value=response, height=150, max_chars=None, key=None)
