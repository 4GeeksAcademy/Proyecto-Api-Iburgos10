import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import seaborn as sns

load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
artista_id = "7iOw6TIHh8GcNnaAFvXyTu"
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

top_tracks = sp.artist_top_tracks(artista_id, country='EC')
for i, track in enumerate(top_tracks['tracks'][:10], 1):
    nombre = track['name']
    duracion_ms = track['duration_ms']
    duracion_min = duracion_ms / 60000  
    popularidad = track['popularity']
    
    print(f"{i}. {nombre} | Duración: {duracion_min:.2f} min | Popularidad: {popularidad}/100")

##############################################################
datos_canciones = []

for track in top_tracks['tracks'][:10]:
    nombre = track['name']
    duracion_min = track['duration_ms'] / 60000  
    popularidad = track['popularity']
    
    datos_canciones.append({
        'nombre': nombre,
        'duracion_min': round(duracion_min, 2),
        'popularidad': popularidad
    })

df = pd.DataFrame(datos_canciones)

df_ordenado = df.sort_values(by='popularidad', ascending=False)

print(df_ordenado.head(3))
#################################################

plt.figure(figsize=(8, 5))
plt.scatter(df['duracion_min'], df['popularidad'], color='royalblue', edgecolors='black')
plt.title('Relación entre duración y popularidad de las canciones')
plt.xlabel('Duración (minutos)')
plt.ylabel('Popularidad (0 a 100)')
plt.grid(True)
plt.tight_layout()
plt.show()
#######
####No hay una relación directa entre la duración de las canciones y la popularidad###