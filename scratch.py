import time

def first():
    print('Start')
    time.sleep(3)
    print('First')
    print('End')


def second():
    print('Second')


# first()
# second()


def download_song(song_name):
    print(f"Downloading {song_name}...")
    time.sleep(3)
    return {'song': song_name, 'artist': 'Beyonce'}

def play_song(song_name):
    print('Before Download')
    song = download_song(song_name)
    print('After Download')
    print(f"{song['song']} by {song['artist']} is now playing...")


play_song('Single Ladies')
