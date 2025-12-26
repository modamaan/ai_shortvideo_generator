# 🎬 Text-To-Video AI - Quick Start Guide

## ✅ You're Almost Ready!

I've integrated **Google Gemini 2.0 Flash** into your project. Here's what you need to do:

---

## 📝 Step 1: Get Your Gemini API Key (2 minutes)

1. Visit: **[aistudio.google.com](https://aistudio.google.com/)**
2. Sign in with your Google account
3. Click **"Get API Key"** → **"Create API Key"**
4. Copy the key (starts with `AIzaSy...`)

---

## ⚙️ Step 2: Update Your `.env` File

Open `.env` and replace the placeholder:

```bash
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Your `.env` should look like this:

```bash
# Pexels API for background videos
PEXELS_KEY=qLECYIyrUJZY4xbFV2K7ACJjeg2SYvTiowq1x8CSGabu1w5cEQEiR2V5

# AI Provider (Gemini recommended)
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 🧪 Step 3: Test Your Setup

```bash
python verify_apis.py
```

You should see:

```
✅ Pexels API is working!
✅ Gemini API is working!
🎉 All APIs configured!
```

---

## 🚀 Step 4: Generate Your First Video!

```bash
python app.py "Amazing space facts"
```

The video will be saved as `rendered_video.mp4`

---

## 🎯 What Works Now

✅ **Fixed Issues:**

- TypeError with environment variables
- Deprecated Groq model updated
- Added Gemini 2.0 Flash support

✅ **API Priority:**

1. Gemini 2.0 Flash (if `GEMINI_API_KEY` is set)
2. Groq API (if `GROQ_API_KEY` is set)
3. OpenAI (if `OPENAI_KEY` is set)

✅ **Free Tier Limits:**

- **Gemini**: 1,500 requests/day (FREE)
- **Pexels**: 200 requests/hour (FREE)

---

## 💡 Example Topics to Try

```bash
python app.py "Weird animal facts"
python app.py "Mind-blowing science discoveries"
python app.py "Ancient civilization mysteries"
python app.py "Future technology predictions"
```

---

## 🆘 Troubleshooting

### Issue: "No API key found"

**Solution**: Make sure `.env` file has `GEMINI_API_KEY` set

### Issue: "Module not found"

**Solution**: Run `pip install google-generativeai python-dotenv`

### Issue: Pexels videos not loading

**Solution**: Check your internet connection and Pexels API key

---

## 📚 More Information

- Full setup guide: `GEMINI_SETUP.md`
- Original README: `README.md`

---

**🎉 You're all set! Get your Gemini API key and start creating videos!**
