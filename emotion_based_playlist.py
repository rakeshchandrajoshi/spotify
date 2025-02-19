# Import necessary libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from textblob import TextBlob
import streamlit as st

# Spotify API setup
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://localhost:8888/callback'

# Authenticate Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-read playlist-read-private"))

# Sentiment analysis function
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = 'happy'
    elif polarity < 0:
        sentiment = 'sad'
    else:
        sentiment = 'neutral'
    
    return sentiment

# Playlist function based on sentiment
def get_playlist_for_sentiment(sentiment):
    playlists = {
        'happy': 'https://open.spotify.com/genre/0JQ5IMCbQBLtqe3T85WC6v',  # Example happy playlist
        'sad': 'https://open.spotify.com/genre/0JQ5DAqbMKFGTIdqXPDTSL',   # Example sad playlist
        'neutral': 'https://open.spotify.com/playlist/7EClwmhqu7mg4JvUI9z5DT'  # Example neutral playlist
    }
    
    return playlists.get(sentiment, 'https://open.spotify.com/artist/1mYsTxnqsietFxj1OgoGbG')  # Default playlist

# Streamlit app interface
def emotion_based_playlist():
    st.title("Emotion-Based Playlist Generator")
    
    # Mood input (user can either type or select)
    mood_input = st.text_input("Enter your mood or thoughts:", "")
    
    if mood_input:
        sentiment = get_sentiment(mood_input)
        playlist_url = get_playlist_for_sentiment(sentiment)
        st.write(f"Based on your input, we recommend this **{sentiment}** playlist:")
        st.markdown(f"[Click here to listen to the playlist]({playlist_url})")
    
    # Option for selecting mood (dropdown)
    mood_select = st.selectbox(
        "Or select your mood from the list below:",
        ["happy", "sad", "neutral"]
    )
    
    if mood_select:
        playlist_url = get_playlist_for_sentiment(mood_select)
        st.write(f"Based on your selected mood, we recommend this **{mood_select}** playlist:")
        st.markdown(f"[Click here to listen to the playlist]({playlist_url})")

# Run the Streamlit app
if __name__ == "__main__":
    emotion_based_playlist()