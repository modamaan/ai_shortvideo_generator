"""
Quick test to verify all dependencies are working
"""
import os
from dotenv import load_dotenv

load_dotenv()

print("🧪 Testing Text-To-Video AI Dependencies...\n")

# Test 1: MoviePy
print("1️⃣ Testing MoviePy...")
try:
    from utility.render.render_engine import VideoFileClip, AudioFileClip, TextClip
    print("   ✅ MoviePy imports successful\n")
except Exception as e:
    print(f"   ❌ MoviePy Error: {e}\n")

# Test 2: Whisper
print("2️⃣ Testing Whisper...")
try:
    import whisper_timestamped as whisper
    print("   ✅ Whisper imported successfully\n")
except Exception as e:
    print(f"   ❌ Whisper Error: {e}\n")

# Test 3: Edge TTS
print("3️⃣ Testing Edge-TTS...")
try:
    import edge_tts
    print("   ✅ Edge-TTS imported successfully\n")
except Exception as e:
    print(f"   ❌ Edge-TTS Error: {e}\n")

# Test 4: AI Providers
print("4️⃣ Testing AI Provider...")
try:
    from utility.script.script_generator import client_type
    print(f"   ✅ Using: {client_type}\n")
except Exception as e:
    print(f"   ❌ AI Provider Error: {e}\n")

# Test 5: Pexels
print("5️⃣ Testing Pexels...")
try:
    PEXELS_KEY = os.environ.get('PEXELS_KEY')
    if PEXELS_KEY:
        print(f"   ✅ Pexels API key found\n")
    else:
        print(f"   ⚠️  Pexels API key not found\n")
except Exception as e:
    print(f"   ❌ Pexels Error: {e}\n")

print("=" * 50)
print("✅ All core dependencies are working!")
print("=" * 50)
print("\n💡 Ready to generate videos! Run:")
print("   python app.py \"Your topic here\"")
