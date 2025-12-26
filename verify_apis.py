import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

print("🔍 Verifying API Keys...\n")

# Check Pexels API
print("1️⃣ Testing Pexels API...")
PEXELS_KEY = os.environ.get('PEXELS_KEY')
if PEXELS_KEY:
    response = requests.get(
        "https://api.pexels.com/v1/search",
        headers={"Authorization": PEXELS_KEY},
        params={"query": "nature", "per_page": 1}
    )
    if response.status_code == 200:
        print(f"   ✅ Pexels API is working!")
        print(f"   📊 Found {response.json()['total_results']:,} nature videos\n")
    else:
        print(f"   ❌ Pexels Error: {response.status_code}\n")
else:
    print("   ⚠️  PEXELS_KEY not found in environment\n")

# Check Groq API
print("2️⃣ Testing Groq API...")
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
if GROQ_API_KEY and len(GROQ_API_KEY) > 30:
    try:
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)
        
        # Test with a simple completion using current model
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Updated model
            messages=[{"role": "user", "content": "Say 'API working' in 2 words"}],
            max_tokens=10
        )
        print(f"   ✅ Groq API is working!")
        print(f"   🤖 Model: llama-3.3-70b-versatile")
        print(f"   💬 Response: {response.choices[0].message.content}\n")
    except Exception as e:
        print(f"   ❌ Groq Error: {str(e)}\n")
else:
    print("   ⚠️  GROQ_API_KEY not found or invalid (needs >30 chars)\n")

# Check Gemini API
print("3️⃣ Testing Gemini API...")
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
if GEMINI_API_KEY and GEMINI_API_KEY != "your_gemini_api_key_here":
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Test with a simple generation
        response = model.generate_content("Say 'API working' in 2 words")
        print(f"   ✅ Gemini API is working!")
        print(f"   🤖 Model: gemini-2.5-flash")
        print(f"   💬 Response: {response.text}\n")
    except Exception as e:
        print(f"   ❌ Gemini Error: {str(e)}\n")
else:
    print("   ⚠️  GEMINI_API_KEY not found or not configured\n")

# Summary
print("=" * 50)
print("📋 Summary:")
print(f"   Pexels: {'✅ Ready' if PEXELS_KEY else '❌ Missing'}")
print(f"   Gemini: {'✅ Ready' if (GEMINI_API_KEY and GEMINI_API_KEY != 'your_gemini_api_key_here') else '❌ Missing/Invalid'}")
print(f"   Groq: {'✅ Ready' if (GROQ_API_KEY and len(GROQ_API_KEY) > 30) else '❌ Missing/Invalid'}")
print("=" * 50)

has_ai_provider = (
    (GEMINI_API_KEY and GEMINI_API_KEY != 'your_gemini_api_key_here') or
    (GROQ_API_KEY and len(GROQ_API_KEY) > 30) or
    os.environ.get('OPENAI_KEY')
)

if PEXELS_KEY and has_ai_provider:
    print("\n🎉 All APIs configured! You're ready to generate videos!")
    print("\n💡 Run: python app.py \"Your topic here\"")
else:
    print("\n⚠️  Please configure missing API keys in .env file")
    if not PEXELS_KEY:
        print("   - Missing: PEXELS_KEY")
    if not has_ai_provider:
        print("   - Missing: At least one AI provider (GEMINI_API_KEY, GROQ_API_KEY, or OPENAI_KEY)")
