import warnings
warnings.filterwarnings("ignore")
import streamlit as st
from langchain.prompts import PromptTemplate
from ctransformers import AutoModelForCausalLM
import time


def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return int(hours), int(minutes), int(seconds)

def format_response(response, word = "Unterscheidung: "):
    if word in response:
        modified_response = response.replace(word, "")
        return modified_response
    else:
        return response

@st.cache_resource
def getLLamaresponse(input_text, no_words):
    input_text = input_text.lower()
    ### LLama2 model
    llm = AutoModelForCausalLM.from_pretrained("llama_models/llama-2-7b-chat.Q2_K.gguf",
                                                model_type='llama',
                                                max_new_tokens = 10240,
                                                repetition_penalty = 1,
                                                temperature = 0.00001
                                              )

    ## Prompt Template
    template = """Write a short paragraph on {input_text} within {no_words} words."""
    prompt = PromptTemplate(input_variables=["input_text", 'no_words'], template=template)


    ## Generating the response
    start_time = time.time()
    response = llm(prompt.format(input_text=input_text, no_words=no_words))
    response = format_response(response)
    time_taken_hours, time_taken_minutes, time_taken_seconds = format_time(time.time() - start_time)
    st.write(f"Time taken: {time_taken_hours} hours, {time_taken_minutes} minutes, {time_taken_seconds} seconds")

    return response


#Rendering Page Setup
st.set_page_config(page_title="Content Generator",
                   layout='centered',
                   initial_sidebar_state='collapsed'
                   )
st.header("Content Generator")
input_text = st.text_input("Enter the Content Topic")
no_words = st.text_input('No of Words')
submit = st.button("Generate")



## Final response
if submit:
    with st.spinner("Generating response..."):
        st.write(getLLamaresponse(input_text, no_words))
