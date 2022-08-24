playlist = {
    'title':'Korean Pop',
    'author': 'heizle',
    'songs' : [
        {'title': 'Darari', 'artist': ['Treasure'], 'duration': 3.45},
        {'title': 'Still Life', 'artist': ['Bigbang'], 'duration': 3.05},
        {'title': 'Rock With You', 'artist': ['Seventeen'], 'duration': 4.25}
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)