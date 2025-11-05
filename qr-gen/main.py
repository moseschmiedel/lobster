from song import SongDB

if __name__ == "__main__":
    songs = SongDB()
    songs.from_csv("songs.csv")
    for s in songs:
        print(s)

    songs.download_yt()
