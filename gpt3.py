import openai
import streamlit as st
openai.api_key = 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


st.title('GPT-3')

st.text('This GPT-3 model is the Davinci-engine')
prompt_text = st.text_input(label="Add here phrase, which you want to be completed", value="Add here few words")
response = openai.Completion.create(engine="davinci", prompt=prompt_text, max_tokens=5)
st.text('Remaining phrase:')
st.text(response["choices"][0]["text"])


