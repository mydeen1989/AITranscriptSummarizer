import openai
import toml
import streamlit as st


def summarize_text(text, lang='en'):

    #secrets = toml.load("streamlit/secrets.toml")
    #openai.api_key = secrets["OPENAI_API_KEY"]
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    prompt = f"""
            The following text is in its original language. Provide the output in this lanuage: {lang}. 
            Format the output as follows:
            
            Author:
            Please show the speaker and participant details as well

            Summary:
            Please give 15 bullet points summarization. I need the speaker name as well who talked
            
            Key Takeaways:
            succinct bullet point list of key takeaways

            Action Items:
            List the key Action items before next meeting

            input text: {text}
            """
    
    response = openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        #model="gpt-3.5-turbo",
        model="gpt-4-turbo", # better performance, slower inference
        )
    
    summary_text = response.to_dict()['choices'][0]['message']['content']
    return summary_text

if __name__ == "__main__":
    text_to_summarize = input("Enter the text to summarize: ")
    lang = input("Enter the language for the summary: ")
    summary = summarize_text(text_to_summarize, lang)
    print("Summary:")
    print(summary)