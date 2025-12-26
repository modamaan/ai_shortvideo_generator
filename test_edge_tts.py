"""
Test Edge-TTS connectivity and voice availability
"""
import asyncio
import edge_tts

async def test_edge_tts():
    print("🧪 Testing Edge-TTS Connection...\n")
    
    # Test 1: List available voices
    print("1️⃣ Fetching available voices...")
    try:
        voices = await edge_tts.list_voices()
        en_voices = [v for v in voices if v['Locale'].startswith('en-')]
        print(f"   ✅ Found {len(en_voices)} English voices")
        print(f"   First 5: {[v['ShortName'] for v in en_voices[:5]]}\n")
    except Exception as e:
        print(f"   ❌ Failed to fetch voices: {e}\n")
        return
    
    # Test 2: Try generating a simple audio
    print("2️⃣ Testing audio generation...")
    test_text = "Hello, this is a test."
    test_file = "test_audio.mp3"
    
    try:
        communicate = edge_tts.Communicate(test_text, "en-US-AriaNeural")
        await communicate.save(test_file)
        print(f"   ✅ Audio generated successfully: {test_file}\n")
        
        # Check file size
        import os
        if os.path.exists(test_file):
            size = os.path.getsize(test_file)
            print(f"   📊 File size: {size} bytes")
            if size > 0:
                print("   ✅ Edge-TTS is working correctly!\n")
            else:
                print("   ⚠️  File is empty - possible network issue\n")
    except Exception as e:
        print(f"   ❌ Failed to generate audio: {e}\n")
        print("   💡 This might be a firewall/network issue")
        print("   💡 Or Edge-TTS service might be temporarily down")

if __name__ == "__main__":
    asyncio.run(test_edge_tts())
