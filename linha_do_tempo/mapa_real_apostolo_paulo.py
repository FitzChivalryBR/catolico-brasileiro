import folium

locations = [
    ("Damasco", 33.5138, 36.2765, "Conversão de Paulo (AD 30/34)"),
    ("Arábia", [28.0, 38.0, 31.0, 40.0], None, "Tempo após conversão"),
    ("Jerusalém", 31.7683, 35.2137, "Primeira visita após conversão (33/37)"),
    ("Tarso", 37.0000, 34.5833, "Cidade natal de Paulo"),
    ("Cilícia", 37.0000, 34.0000, "Missão em Cilícia (40-44)"),
    ("Antioquia", 36.2021, 37.1343, "Base missionária (44-45)"),
    ("Chipre", 35.1264, 33.4299, "Primeira viagem missionária (46-49)"),
    ("Pisídia", 38.0000, 31.0000, "Primeira viagem missionária (46-49)"),
    ("Listra", 37.5833, 32.4500, "Primeira viagem missionária (46-49)"),
    ("Derbe", 37.3667, 33.7667, "Primeira viagem missionária (46-49)"),
    ("Troas", 39.7500, 26.9833, "Visão do homem macedônio"),
    ("Samotrácia", 40.4633, 24.4750, "Passagem na segunda viagem"),
    ("Neápolis", 41.0000, 24.0000, "Chegada à Macedônia"),
    ("Filipos", 41.0082, 24.2860, "Segunda viagem missionária (49-52)"),
    ("Tessalônica", 40.6401, 22.9444, "Segunda viagem missionária (49-52)"),
    ("Beréia", 40.5223, 22.2037, "Pregação após Tessalônica"),
    ("Atenas", 37.9838, 23.7275, "Segunda viagem missionária (49-52)"),
    ("Corinto", 37.9391, 22.9530, "Segunda viagem missionária (49-52)"),
    ("Éfeso", 37.9394, 27.3403, "Terceira viagem missionária (54-57)"),
    ("Mileto", 37.3153, 27.2566, "Encontro com presbíteros de Éfeso"),
    ("Rodes", 36.4341, 28.2176, "Parada na viagem a Jerusalém"),
    ("Pátara", 36.2667, 29.3167, "Embarque para a Fenícia"),
    ("Tiro", 33.2700, 35.2000, "Parada antes de Jerusalém"),
    ("Ptolemaida", 32.9333, 35.0833, "Última parada antes de Jerusalém"),
    ("Cesareia", 32.5000, 34.9000, "Prisão em Cesareia (58-60)"),
    ("Sidon", 33.5639, 35.3689, "Paulo recebeu assistência"),
    ("Cnido", 36.6863, 27.3759, "Passagem a caminho de Roma"),
    ("Creta", 35.2401, 24.8093, "Navegação antes do naufrágio"),
    ("Malta", 35.9375, 14.3754, "Naufrágio e estadia em Malta (60)"),
    ("Siracusa", 37.0755, 15.2866, "Parada na Sicília"),
    ("Regium", 38.1105, 15.6431, "Última parada antes da Itália"),
    ("Puteoli", 40.8333, 14.1000, "Primeira cidade na Itália"),
    ("Roma", 41.9028, 12.4964, "Prisão e morte (61-64)")
]

# Criar o mapa centralizado no Mediterrâneo Oriental
m = folium.Map(location=[37.5, 30.0], zoom_start=5, tiles="CartoDB positron", attr="© OpenStreetMap contributors, © CARTO")

# Definir cores para as etapas
colors = [
    "red", "blue", "green", "purple", "orange", "darkred", "cadetblue", "pink", "darkblue", "black", "lightblue",
    "darkgreen", "lightgreen", "darkpurple", "lightred", "gray", "beige", "lightgray", "white", "brown"
]

# Adicionar os locais ao mapa com numeração e informações
for i, (city, lat, lon, description) in enumerate(locations):
    if isinstance(lat, list):  # Caso especial para Arábia (representação por área)
        folium.Rectangle(
            bounds=[[lat[0]-1, lat[1]-1], [lat[2]+1, lat[3]+1]],
            color="gray",
            fill=True,
            fill_color="gray",
            fill_opacity=0.3,
            popup=f"{city}: {description}"
        ).add_to(m)
    else:
        if city == 'Roma':
            folium.Marker(
            location=[lat, lon],
            popup=f"{i+1}. {city}: {description}",
            tooltip=f"{i+1}. {city}",
            icon=folium.Icon(icon='cross', color='darkred', prefix="fa")
            ).add_to(m)

        elif city == "Damasco":
            folium.Marker(
            location=[lat, lon],
            popup=f"{i+1}. {city}: {description}",
            tooltip=f"{i+1}. {city}",
            icon=folium.Icon(icon='hand-holding-heart', color='blue', prefix="fa")
            ).add_to(m)
        else:
            folium.Marker(
                location=[lat, lon],
                popup=f"{i+1}. {city}: {description}",
                tooltip=f"{i+1}. {city}",
                icon=folium.Icon(color=colors[i % len(colors)])
            ).add_to(m)

# Criar trajetórias entre os pontos
coordinates = [(lat, lon) for _, lat, lon, _ in locations if not isinstance(lat, list)]
for i in range(len(coordinates) - 1):
    folium.PolyLine(
        [coordinates[i], coordinates[i+1]],
        color=colors[i % len(colors)],
        weight=2.5,
        opacity=0.7
    ).add_to(m)

# Adicionar camadas extras
folium.LayerControl().add_to(m)

# Salvar o mapa
map_filepath = "mapa_paulino.html"
m.save(map_filepath)

print(f"Mapa salvo em {map_filepath}")
m