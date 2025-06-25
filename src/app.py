import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import seaborn as sns

# load the .env file variables
load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
artista_id = "7iOw6TIHh8GcNnaAFvXyTu"
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

top_tracks = auth_manager.artist_top_tracks(artista_id, country='EC')
for i, track in enumerate(top_tracks['tracks'][:10], 1):
    nombre = track['name']
    
    # Duración en milisegundos -> minutos
    duracion_ms = track['duration_ms']
    duracion_min = duracion_ms / 60000  # 1000 ms * 60 seg
    
    # Popularidad (de 0 a 100)
    popularidad = track['popularity']
    
    print(f"{i}. {nombre} | Duración: {duracion_min:.2f} min | Popularidad: {popularidad}/100")