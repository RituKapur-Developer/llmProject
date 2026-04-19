from groq import Groq
#import google.generativeai as genai
from google import genai
from app import load_env
#from .config import GROQ_API_KEY, GOOGLE_API_KEY
api_keys_dict = load_env.load_env_vars('.env')
groq_client = Groq(api_key=api_keys_dict["GROQ_API_KEY"])
GOOGLE_API_KEY = api_keys_dict["GOOGLE_API_KEY"]
def call_groq(prompt: str):
    resp = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content


def call_gemini(prompt: str):
    if not GOOGLE_API_KEY:
        return None
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model.generate_content(prompt).text


def route_llm(prompt: str, mode="fast"):
    if mode == "fast":
        return call_groq(prompt)
    elif mode == "reasoning":
        res = call_gemini(prompt)
        return res if res else call_groq(prompt)
    return call_groq(prompt)