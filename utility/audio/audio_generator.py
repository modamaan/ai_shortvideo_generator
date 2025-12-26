import edge_tts
import asyncio

async def generate_audio(text, outputFilename):
    """
    Generate audio from text using Edge-TTS with gTTS fallback
    """
    # Try Edge-TTS first
    print("🎤 Attempting Edge-TTS...")
    voices = ["en-US-AriaNeural", "en-US-GuyNeural"]
    
    for voice in voices:
        try:
            communicate = edge_tts.Communicate(text, voice, rate="+0%", volume="+0%")
            await asyncio.wait_for(communicate.save(outputFilename), timeout=15.0)
            print(f"✅ Audio generated with Edge-TTS ({voice})")
            return
        except Exception as e:
            print(f"⚠️  Edge-TTS {voice} failed: {type(e).__name__}")
            continue
    
    # Fallback to gTTS (Google Text-to-Speech)
    print("🔄 Edge-TTS failed, falling back to gTTS (Google TTS)...")
    try:
        from gtts import gTTS
        
        # Convert .wav to .mp3 if needed
        output_file = outputFilename
        if outputFilename.endswith('.wav'):
            output_file = outputFilename.replace('.wav', '.mp3')
        
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(output_file)
        
        # If original was .wav, rename .mp3 to .wav (MoviePy can handle it)
        if output_file != outputFilename:
            import os
            if os.path.exists(outputFilename):
                os.remove(outputFilename)
            os.rename(output_file, outputFilename)
        
        print(f"✅ Audio generated with gTTS (Google)")
        return
        
    except Exception as e:
        print(f"❌ gTTS also failed: {e}")
        raise Exception(
            "Both Edge-TTS and gTTS failed. Check your internet connection."
        )




