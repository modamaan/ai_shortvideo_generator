"""
Test the updated audio generator with gTTS fallback
"""
import asyncio
from utility.audio.audio_generator import generate_audio

async def test():
    print("🧪 Testing Audio Generator with gTTS Fallback\n")
    
    test_text = "Amazing ocean facts: The ocean covers 71% of Earth's surface."
    output_file = "test_audio_output.wav"
    
    try:
        await generate_audio(test_text, output_file)
        print(f"\n✅ Test successful! Audio saved to: {output_file}")
        
        # Check file
        import os
        if os.path.exists(output_file):
            size = os.path.getsize(output_file)
            print(f"📊 File size: {size:,} bytes")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")

if __name__ == "__main__":
    asyncio.run(test())
