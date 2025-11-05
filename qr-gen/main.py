import sys
from song import SongDB

if __name__ == "__main__":
    songs = SongDB()
    songs.from_csv("songs.csv")
    for s in songs:
        print(s)

    if sys.argv[1] == "download":
        songs.download_yt()
    elif sys.argv[1] == "qr":
        songs.generate_qr_codes("codes")
