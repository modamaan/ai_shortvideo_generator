import os
import json

# Check for Google Gemini API (recommended - free tier available)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_KEY")

if GEMINI_API_KEY:
    import google.generativeai as genai
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
    client_type = "gemini"
    print("🤖 Using Google Gemini 2.5 Flash")
elif GROQ_API_KEY and len(GROQ_API_KEY) > 30:
    from groq import Groq
    model = "llama-3.3-70b-versatile"  # Updated to current model
    client = Groq(api_key=GROQ_API_KEY)
    client_type = "groq"
    print("🤖 Using Groq API")
elif OPENAI_API_KEY:
    from openai import OpenAI
    model = "gpt-4o"
    client = OpenAI(api_key=OPENAI_API_KEY)
    client_type = "openai"
    print("🤖 Using OpenAI API")
else:
    raise ValueError("No API key found! Please set GEMINI_API_KEY, GROQ_API_KEY, or OPENAI_KEY in your .env file")

def generate_script(topic):
    prompt = (
        """You are a seasoned content writer for a YouTube Shorts channel, specializing in facts videos. 
        Your facts shorts are concise, each lasting less than 50 seconds (approximately 140 words). 
        They are incredibly engaging and original. When a user requests a specific type of facts short, you will create it.

        For instance, if the user asks for:
        Weird facts
        You would produce content like this:

        Weird facts you don't know:
        - Bananas are berries, but strawberries aren't.
        - A single cloud can weigh over a million pounds.
        - There's a species of jellyfish that is biologically immortal.
        - Honey never spoils; archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.
        - The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.
        - Octopuses have three hearts and blue blood.

        You are now tasked with creating the best short script based on the user's requested type of 'facts'.

        Keep it brief, highly interesting, and unique.

        Stictly output the script in a JSON format like below, and only provide a parsable JSON object with the key 'script'.

        # Output
        {"script": "Here is the script ..."}
        """
    )

    if client_type == "gemini":
        # Gemini API format
        full_prompt = f"{prompt}\n\nUser request: {topic}"
        response = model.generate_content(full_prompt)
        content = response.text
    else:
        # OpenAI/Groq format
        response = client.chat.completions.create(
                model=model if client_type == "groq" else model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": topic}
                ]
            )
        content = response.choices[0].message.content
    
    try:
        # Clean the content - remove markdown code blocks if present
        content = content.strip()
        if content.startswith('```'):
            content = content.split('```')[1]
            if content.startswith('json'):
                content = content[4:]
        content = content.strip()
        
        script = json.loads(content)["script"]
    except Exception as e:
        # Fallback: try to extract JSON from the content
        json_start_index = content.find('{')
        json_end_index = content.rfind('}')
        if json_start_index != -1 and json_end_index != -1:
            content = content[json_start_index:json_end_index+1]
            # Replace newlines within the JSON string value
            content = content.replace('\n', ' ').replace('\r', ' ')
            script = json.loads(content)["script"]
        else:
            raise Exception(f"Failed to parse script from AI response: {e}")
    
    return script
