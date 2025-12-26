# AI Short Video Generator 🎬

Generate engaging short-form videos automatically from text prompts using AI! Perfect for YouTube Shorts, TikTok, Instagram Reels, and social media content.

## ✨ Features

- 🤖 **AI Script Generation** - Powered by Gemini 2.0 Flash, Groq, or OpenAI
- 🎤 **Text-to-Speech** - Google TTS (gTTS) with Edge-TTS fallback
- 📝 **Auto Captions** - Whisper-powered timed captions
- 🎥 **Smart Video Selection** - Pexels API integration for relevant background footage
- 🎨 **Professional Rendering** - MoviePy 2.x for high-quality output
- ⚡ **Python 3.13 Compatible** - Latest Python version supported

## 🎯 Perfect For

- YouTube Shorts creators
- Social media marketers
- Content creators
- Product demos (like DevTree!)
- Educational content
- Fact-based viral videos

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/modamaan/ai_shortvideo_generator.git
cd ai_shortvideo_generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys

Copy `.env.example` to `.env` and add your API keys:

```bash
cp .env.example .env
```

**Required:**

- **Pexels API** - Get free key at [pexels.com/api](https://www.pexels.com/api/)

**Choose ONE AI Provider:**

- **Gemini** (Recommended) - Free at [aistudio.google.com](https://aistudio.google.com/)
- **Groq** (Fast & Free) - Get key at [console.groq.com](https://console.groq.com/)
- **OpenAI** (Paid) - Get key at [platform.openai.com](https://platform.openai.com/)

### 4. Generate Your First Video

```bash
python app.py "Amazing ocean facts"
```

Output: `rendered_video.mp4` (1920x1080, ~30-40 seconds)

## 📖 Usage Examples

```bash
# Facts-based content
python app.py "Mind-blowing space discoveries"

# Product marketing
python app.py "DevTree: The developer's link-in-bio tool with GitHub integration"

# Educational content
python app.py "How photosynthesis works in simple terms"

# Viral content
python app.py "Weird facts you didn't know about the ocean"
```

## 🛠️ How It Works

```
1. User Input → "Amazing ocean facts"
         ↓
2. AI (Gemini/Groq) → Generate engaging script
         ↓
3. gTTS → Convert script to audio
         ↓
4. Whisper → Generate timed captions
         ↓
5. AI → Extract visual keywords
         ↓
6. Pexels API → Fetch background videos
         ↓
7. MoviePy → Render final video
         ↓
8. Output → rendered_video.mp4
```

## 🔧 Configuration

### AI Provider Priority

The system automatically uses the first available API:

1. Gemini 2.0 Flash (if `GEMINI_API_KEY` set)
2. Groq (if `GROQ_API_KEY` set)
3. OpenAI (if `OPENAI_KEY` set)

### Audio Generation

- Primary: Edge-TTS (Microsoft)
- Fallback: gTTS (Google) - more reliable

## 📊 API Limits (Free Tier)

| Service              | Limit              | Cost |
| -------------------- | ------------------ | ---- |
| **Gemini 2.0 Flash** | 1,500 requests/day | FREE |
| **Groq**             | Varies by load     | FREE |
| **Pexels**           | 200 requests/hour  | FREE |
| **gTTS**             | Unlimited          | FREE |

## 🐛 Troubleshooting

### Common Issues

**"No module named 'moviepy'"**

```bash
pip install -r requirements.txt
```

**"API key not found"**

- Check `.env` file exists
- Verify API keys are correct
- No quotes around values in `.env`

**"No audio received" (Edge-TTS)**

- gTTS fallback will activate automatically
- No action needed

**Video rendering fails**

- Check internet connection (downloads Pexels videos)
- Ensure sufficient disk space
- Verify FFmpeg is installed (comes with MoviePy)

## 📚 Documentation

- [`QUICKSTART.md`](QUICKSTART.md) - Quick setup guide
- [`GEMINI_SETUP.md`](GEMINI_SETUP.md) - Detailed Gemini integration
- [`PYTHON313_FIX.md`](PYTHON313_FIX.md) - Python 3.13 compatibility notes

## 🧪 Testing

```bash
# Test API connections
python verify_apis.py

# Test audio generation
python test_audio_gen.py

# Test all dependencies
python test_dependencies.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Original project: [SamurAIGPT/Text-To-Video-AI](https://github.com/SamurAIGPT/Text-To-Video-AI)
- Enhanced with Gemini 2.0 Flash integration
- Python 3.13 compatibility updates
- gTTS fallback implementation
- MoviePy 2.x migration

## 📧 Support

For issues and questions:

- Open an issue on GitHub
- Check existing documentation
- Review troubleshooting guide

---

**Made with ❤️ for content creators**

Generate your first AI video in under 5 minutes! 🚀
