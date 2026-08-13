# 🤖 Jarvis - Python Voice Assistant

> A voice-controlled personal assistant built in Python — listens for the wake word "Jarvis" and executes commands in real time.

## 🎯 Overview
Jarvis is a beginner-to-intermediate level voice assistant that combines speech recognition, text-to-speech, and web automation to create a hands-free command experience — inspired by AI assistants like Alexa and Siri, built from scratch in Python.

## ✨ Features
- 🎤 **Wake-word detection** — activates only when it hears "Jarvis"
- 🌐 **Voice-controlled browsing** — opens Google, YouTube, Facebook, LinkedIn, and Gemini on command
- 🎵 **Music playback** — plays songs from a custom music library via voice command
- 🔊 **Text-to-speech responses** — talks back using offline TTS (pyttsx3)
- ⚠️ **Graceful error handling** — doesn't crash on unrecognized commands or audio errors

## 🛠️ Tech Stack
| Component | Library |
|---|---|
| Speech-to-Text | `SpeechRecognition` (Google Speech API) |
| Text-to-Speech | `pyttsx3` (SAPI5, offline) |
| Web Automation | `webbrowser` |
| Audio Input | `PyAudio` |

## 🚀 How to Run
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the assistant
python main.py

# 3. Say "Jarvis" to activate, then speak your command
```

## 🐛 Challenges I Solved
- Fixed a `pyttsx3` bug where the engine would go silent on repeated calls — solved by reinitializing the TTS engine inside the `speak()` function instead of reusing a single global instance.
- Added a fallback response for unrecognized voice commands instead of letting the assistant fail silently.

## 🔭 What's Next
**This is just the beginning.** I'm actively going to keep building on this project over time. Planned additions:
- [ ] More voice commands (weather updates, time, reminders, app launching)
- [ ] Smarter wake-word matching (currently exact match, will make it fuzzy)
- [ ] Persistent conversation logging
- [ ] A simple GUI instead of console-only interaction
- [ ] Offline speech recognition support

## 🙏 Credits
Built by following CodeWithHarry's Python Mega Project series, with custom debugging, added error handling, and my own modifications on top of the base tutorial.

---
📌 *This project marks my starting point in building real-world Python applications. More updates coming soon.*
