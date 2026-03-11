# 🎤 AI Voice Agent - Real-time WebRTC Voice Assistant

<div align="center">
  
  ![Version](https://img.shields.io/badge/version-2.0-blue)
  ![Docker](https://img.shields.io/badge/docker-ready-brightgreen)
  ![LiveKit](https://img.shields.io/badge/WebRTC-LiveKit-purple)
  ![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)
  ![License](https://img.shields.io/badge/license-MIT-green)
  
  ### 🗣️ **Talk to AI in real-time, just like in the movies!**
  
  [![GitHub stars](https://img.shields.io/github/stars/Umar5199/Ai-voice-Agent?style=social)](https://github.com/Umar5199/Ai-voice-Agent/stargazers)
  [![GitHub forks](https://img.shields.io/github/forks/Umar5199/Ai-voice-Agent?style=social)](https://github.com/Umar5199/Ai-voice-Agent/network/members)
  
</div>

---

## 📋 **Table of Contents**
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🏗️ Architecture](#️-architecture)
- [🚀 Quick Start](#-quick-start)
- [📦 Project Structure](#-project-structure)
- [🎯 How It Works](#-how-it-works)
- [🔧 Configuration](#-configuration)
- [📊 Performance](#-performance)
- [🚨 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)
- [👨‍💻 Author](#-author)

---

## ✨ **Features**

| Feature | Description |
|---------|-------------|
| 🎯 **Real-time Conversation** | <500ms latency for natural back-and-forth dialogue |
| 🧠 **Intelligent Responses** | Powered by Google Gemini 2.5 Flash LLM |
| 🎤 **Accurate Speech Recognition** | Gladia STT with 95%+ accuracy |
| 🗣️ **Natural Voice Output** | Deepgram Aura TTS with human-like voices |
| 🐳 **Full Containerization** | 3 Docker containers working together |
| 🌐 **Public Access** | Share your agent via ngrok tunnel |
| 📱 **Responsive UI** | Beautiful dashboard that works on all devices |
| ⚡ **WebRTC Infrastructure** | LiveKit Cloud for reliable media streaming |
| 🔒 **Secure Authentication** | JWT token-based room access |
| 📊 **Live Transcript** | See your conversation in real-time |
| ⚠️ **Error Handling** | Visual quota warnings and error messages |

---

## 🛠️ **Tech Stack**

### **Core Technologies**
| Category | Technology | Purpose |
|----------|------------|---------|
| **WebRTC Framework** | [LiveKit Cloud](https://livekit.io) | Real-time media streaming |
| **Speech-to-Text** | [Gladia API](https://gladia.io) | Convert voice to text |
| **Language Model** | [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) | AI response generation |
| **Text-to-Speech** | [Deepgram Aura](https://deepgram.com) | Natural voice synthesis |
| **Voice Detection** | Silero VAD | Detect when user speaks |

### **Backend Infrastructure**
| Component | Technology | Port |
|-----------|------------|------|
| **Agent Service** | Python + LiveKit Agents | - |
| **Token Server** | FastAPI | 8000 |
| **Frontend Server** | Nginx | 8080 |
| **Container Runtime** | Docker | - |
| **Orchestration** | Docker Compose | - |

### **Frontend**
| Technology | Usage |
|------------|-------|
| HTML5 | Structure |
| CSS3 | Styling & Animations |
| JavaScript | Logic & LiveKit Client |
| LiveKit Client SDK | WebRTC connection |

### **DevOps & Deployment**
| Tool | Purpose |
|------|---------|
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| ngrok | Public URL tunneling |
| Git | Version control |

---

## 🏗️ **Architecture**
┌─────────────────────────────────────────────────────────────┐
│ USER BROWSER │
│ (https://your-url) │
└─────────────────────────┬───────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ NGORK TUNNEL │
│ https://your-app.ngrok-free.dev │
└─────────────────────────┬───────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ DOCKER CONTAINERS │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ FRONTEND (Nginx - Port 8080) │ │
│ │ HTML/CSS/JavaScript UI │ │
│ └────────────────────┬────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ TOKEN SERVER (FastAPI - Port 8000) │ │
│ │ JWT Authentication & Room Management │ │
│ └────────────────────┬────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ LIVEKIT CLOUD (WebRTC) │ │
│ │ Media Streaming & Room Management │ │
│ └────────────────────┬────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ VOICE AGENT (Python) │ │
│ │ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │ │
│ │ │ Gladia STT │─▶│Gemini LLM │─▶│Deepgram TTS │ │ │
│ │ └─────────────┘ └─────────────┘ └─────────────┘ │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

---

## 🚀 **Quick Start**

### **Prerequisites**
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac/Linux)
- [Python 3.11+](https://www.python.org/downloads/)
- API Keys (all free tiers available):
  - [Google Gemini API Key](https://aistudio.google.com/apikey)
  - [Gladia API Key](https://app.gladia.io)
  - [Deepgram API Key](https://console.deepgram.com)
  - [LiveKit Cloud Account](https://cloud.livekit.io)

### **Installation Steps**
**1.Set Up Environment Variables
Create a .env file in the root directory:
# LiveKit Cloud Credentials
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_secret

# AI Service Keys
GOOGLE_API_KEY=your_gemini_api_key
GLADIA_API_KEY=your_gladia_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key**
2. Build Docker Images
docker-compose build
3.Start the Containers
docker-compose up -d
4. Verify Everything is Running
docker ps
5.You should see 3 running containers:

voice-agent

voice-backend

voice-frontend

 Access Your Voice Agent
Local Access: http://localhost:8080

Public Access (using ngrok):

ngrok http 8080

#### 6. **Clone the Repository**
```bash
git clone https://github.com/Umar5199/Ai-voice-Agent.git
cd Ai-voice-Agent

