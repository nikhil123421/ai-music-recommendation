import random
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components
from ytmusicapi import YTMusic

# --- 1. Page Configuration ---
st.set_page_config(page_title="Hindi Mood Radio", page_icon="📻", layout="centered")

# Initialize the YouTube Music API
@st.cache_resource
def init_yt():
    return YTMusic()

yt_api = init_yt()

# --- 2. Data Mapping (Optimized for Hindi Music Styles) ---
vibe_lookup = {
    "Happy": {"styles": ["bollywood dance", "upbeat hindi pop", "bhangra"]},
    "Sad": {"styles": ["hindi sad emotional", "arijit singh melancholy", "ghazal"]},
    "Angry": {"styles": ["hindi rock", "aggressive bollywood", "hindi rap"]},
    "Relaxed": {"styles": ["hindi acoustic", "bollywood unplugged", "sufi calm"]},
    "Romantic": {"styles": ["bollywood romance", "hindi love songs", "90s melodies"]},
    "Focused": {"styles": ["hindi instrumental", "sitar ambient", "flute focus"]},
    "Party": {"styles": ["item songs", "bollywood party hits", "punjabi dance"]},
    "Nostalgic": {"styles": ["70s bollywood", "80s hindi classics", "old gold tracks"]}
}

def get_time_context():
    current_hour = datetime.now().hour
    if current_hour < 12: return "🌅 Morning vibes"
    elif current_hour < 18: return "☀️ Daytime energy"
    else: return "🌙 Night mode"

# --- 3. Streamlit UI Build (English Interface) ---
st.title("📻 AI Hindi Music Radio")
st.write("Pick your mood and I'll find a random Hindi track for you!")

# Input (English UI)
user_mood = st.selectbox("How are you feeling right now?", list(vibe_lookup.keys()))

# The Generate Button
if st.button("🎲 Play a Random Hindi Song", type="primary", use_container_width=True):
    with st.spinner(f"Searching for the perfect {user_mood.lower()} track..."):
        
        # Logic calculations
        vibe_data = vibe_lookup[user_mood]
        selected_style = random.choice(vibe_data["styles"])
        
        try:
            # We strictly add "Hindi" to the query to ensure language consistency
            # Using quotes around "Hindi" helps tell the search engine it's a requirement
            search_string = f'"{selected_style}" Hindi song'
            
            # Fetch a pool of 20 songs
            search_results = yt_api.search(search_string, filter="songs", limit=20)
            
            if not search_results:
                st.warning("Couldn't find an exact match. Try clicking again!")
            else:
                # Randomly select ONE track from the pool
                chosen_track = random.choice(search_results)
                song_title = chosen_track.get('title', 'Unknown Track')
                yt_video_id = chosen_track.get('videoId')
                
                if yt_video_id:
                    # --- UI: ONLY SHOW THE SONG NAME ---
                    st.markdown("---")
                    st.markdown(f"<h2 style='text-align: center; color: #FF4B4B;'>🎶 {song_title}</h2>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align: center; color: gray;'>{get_time_context()}</p>", unsafe_allow_html=True)
                    st.markdown("---")
                    
                    # --- INVISIBLE AUTOPLAY AUDIO ---
                    # The iframe is hidden (0x0) and set to autoplay
                    player_html = f"""
                        <iframe width="0" height="0" 
                                src="https://www.youtube.com/embed/{yt_video_id}?autoplay=1" 
                                frameborder="0" 
                                allow="autoplay; encrypted-media">
                        </iframe>
                    """
                    components.html(player_html, height=0)
                    
        except Exception as error:
            st.error(f"⚠️ Connection Error: {error}")