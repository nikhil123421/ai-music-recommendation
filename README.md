# 📻 AI Music Recommender - Mood Radio

A Streamlit-based AI music recommendation app that generates random songs based on your current mood and emotional state. The app uses YouTube Music API integration to provide personalized music suggestions with autoplay functionality.

## ✨ Features

- **8 Mood Categories:** Happy, Sad, Angry, Relaxed, Romantic, Focused, Party, Nostalgic
- **Time-Based Context:** Adjusts vibes based on time of day (Morning, Daytime, Night)
- **One-Click Music Discovery:** Generate a random song matching your mood instantly
- **Autoplay Integration:** Seamless YouTube Music embedded player with autoplay
- **Mood-to-Genre Mapping:** Intelligent genre selection based on emotional state
- **Clean UI:** Centered, intuitive interface with emoji-enhanced visual feedback

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone or download the project**
   ```bash
   cd spotifyProject
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   - The app will automatically open in your browser at `http://localhost:8501`

## 📖 How to Use

1. **Select Your Mood:** Choose from 8 mood categories using the dropdown menu
2. **Click Generate:** Press the "🎲 Play a Random Song" button
3. **Enjoy:** The app fetches a matching song from YouTube Music and auto-plays it

## 🛠️ Technical Stack

- **Framework:** Streamlit - Interactive Python web app framework
- **Music API:** ytmusicapi - YouTube Music API wrapper
- **Language:** Python 3.9+
- **Frontend:** HTML/CSS with Streamlit components

## 📚 Core Concepts Implemented

| Concept | Implementation |
|---------|-----------------|
| **Data Structures** | Nested dictionaries for mood-to-genre mapping |
| **Error Handling** | Try/Except blocks for robust API response management |
| **Functional Programming** | Modular design with cached API initialization |
| **Caching** | `@st.cache_resource` for efficient API connection reuse |
| **External Libraries** | Integration with `ytmusicapi` and `streamlit` |
| **Time Logic** | Dynamic time-based context generation |
| **Random Selection** | Randomized song generation for variety |

## 📋 Project Structure

```
spotifyProject/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🎵 Mood Categories & Genres

- **Happy:** Upbeat pop, Dance, Feel good
- **Sad:** Acoustic melancholy, Sad piano, Emotional
- **Angry:** Heavy metal, Hard rock, Aggressive
- **Relaxed:** Lofi chill, Ambient relaxing, Calm
- **Romantic:** Romantic R&B, Love soul, Sweet
- **Focused:** Study lo-fi, Instrumental focus, Concentration
- **Party:** Party EDM, Club dance, Hype
- **Nostalgic:** Retro, Classic throwback, Vintage

## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| App won't start | Ensure Python 3.9+ is installed and dependencies are installed via `pip install -r requirements.txt` |
| No songs found | YouTube Music API sometimes returns no results for niche searches; try again or adjust mood selection |
| Autoplay not working | Check browser autoplay permissions and allow autoplay for the localhost site |

## 📝 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements, bug fixes, or new mood categories.