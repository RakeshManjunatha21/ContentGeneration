import streamlit as st
import os
import requests
import re
import json
import google.generativeai as genai
import markdown2

# Title
st.title("Funnel Content Generation")

# Content Type
content_type = st.selectbox("1. Content Type:", ["Blog", "Article"])

# What do you want to write about
topic = st.text_input("2. What do you want to write about:")

# Keywords
keywords_text = st.text_area("3. Keywords to be included (Max 3):", "Keyword 1, Keyword 2, Keyword 3")
keywords = [word.strip() for word in keywords_text.split(',') if word.strip()]

# Funnel Type
funnel_type = st.selectbox("4. Funnel Type:", ["Top Funnel", "Mid Funnel", "Bottom Funnel"])

# Social Media Post
social_media = st.selectbox("5. Social Media Post:", ["LinkedIn", "X", "None"])

# Button to generate content
if st.button("Generate Content"):
    with st.spinner('We are generating content...'):
      GeminiKeys = [
      "AIzaSyCcVUOyL2M9aNRUhgO6lzTAJ-BjOUXZrt0",
      "AIzaSyC9JxomOkNel9uy0qdqixDcI6UH6KhMcho"
      ]
      os.environ["GOOGLE_API_KEY"] = GeminiKeys[0]
      prompt_final = ""
      if len(social_media) != None:
        format_structure = {

        }
        prompt = f"""
        Pretend like you are a Human with 10 years of experience in marketing funnel content writer like top of the funnel(ToFu), middle of the funnel(MoFU) and bottom of the funnel(BoFU) specialist and {social_media} creator for {content_type} with minimum of atleast two thousand words in the response is must.

        write a {funnel_type} content for the website {content_type} about "{topic}" with catchy title and title should not be same as given input and content should related with these keywords "{keywords}", also must create a detailed {social_media} for the same separated by hr tag and the post must be in the bottom like {social_media}:" in bold as title in html format with h1 tag.
        Strictly the output response content must contain {social_media} with maximun of 50 words.
        Strictly the output response content must contain minimum of three thousand words in the response context.
        Strictly Don't include any other information or special characters in the beginning of the response.
        Strictly the output response must be in HTML Format only with sub-headers, bullet points wherever needed and remove unecessary <br> new lines Example: '\n'.
        Strictly the output Must Include Human Touch and Emotions in the generated text and change the tone inevitably. Dont include Repetitive Language and Keyword Stuffing.

        """
        prompt_final = prompt

      else:
        format_structure = {
        }
        prompt = f"""
        Pretend like you are a Human with 10 years of experience in marketing funnel content writer like top of the funnel(ToFu), middle of the funnel(MoFU) and bottom of the funnel(BoFU) specialist creator for {content_type} with minimum of atleast two thousand words in the response is must.

        write a {funnel_type} content for the website {content_type} about "{topic}" with catchy title and title should not be same as given input and content should related with these keywords "{keywords}".
        Strictly the output reponse content must contain minimum of three thousand words in the response context.
        Strictly Don't include any other information or special characters in the beginning of the response.
        Strictly the output response must be in HTML Format only with sub-headers, bullet points wherever needed and remove unecessary <br> new lines Example: '\n'.
        Strictly the output Must Include Human Touch and Emotions in the generated text and change the tone inevitably. Dont include Repetitive Language and Keyword Stuffing.

        """
        prompt_final = prompt
      genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
      gemini_model = genai.GenerativeModel("gemini-pro",
                                          generation_config=genai.types.GenerationConfig(
                                              max_output_tokens=64000,
                                              temperature=0.0
                                          ))
      response = gemini_model.generate_content(prompt_final)
      llm_response  = response.text
      html_funnel_content = markdown2.markdown(llm_response)
      # html_result = generate_content_gemini(content_type, topic, [keywords], funnel_type, social_media)
    st.markdown(html_funnel_content, unsafe_allow_html=True)
    
    # Display the generated content
    st.success(f"Content Type: {content_type}\n"
               f"Topic: {topic}\n"
               f"Keywords: {', '.join(keywords)}\n"
               f"Funnel Type: {funnel_type}\n"
               f"Social Media Post: {social_media}")
