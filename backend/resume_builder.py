import os
import google.generativeai as genai
import re
from dotenv import load_dotenv
load_dotenv()
# from config import MODEL,generation_config,system_prompt,user_input
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


def generate(api_key, model, system_prompt, inputs, generative_config):
    genai.configure(api_key = api_key)
    model = genai.GenerativeModel(model)
    input_text = "\n".join(inputs) if isinstance(inputs,list) else inputs
    combined_prompt = f"{system_prompt}\n\nUser Information:\n{input_text}"
    response = model.generate_content(
        combined_prompt,
        generation_config=generative_config
    )
    html_pattern = r"```html\n(.*?)```"
    match = re.search(html_pattern, response.text, re.DOTALL)
    if match:
        html_code = match.group(1)
        return html_code.replace("\n", "")
    else:
        return None

if __name__ == "__main__":
    GEMINI_MODEL = MODEL
    SYSTEM_PROMPT = system_prompt
    USER_INPUT = user_input
    GENERATIVE_CONFIG = generation_config
    code = generate(GEMINI_API_KEY, GEMINI_MODEL, SYSTEM_PROMPT, USER_INPUT, GENERATIVE_CONFIG)
    with open("resume.html",'w',encoding='utf-8') as f:
        f.write(code)
        print('Resume generated successfully')

    
