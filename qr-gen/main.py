import sys

import qrcode
from song import SongDB

if __name__ == "__main__":
    songs = SongDB()
    songs.from_csv("songs-rick-roll.csv")

    if sys.argv[1] == "download":
        songs.download_yt()
    elif sys.argv[1] == "qr":
        songs.generate_qr_codes("codes")
    elif sys.argv[1] == "error-songs":
        songs = SongDB()
        songs.from_csv("songs-redownload.csv")
        songs.error_list()
    elif sys.argv[1] == "site-qr":
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=10,
            border=4,
        )
        qr_data = "https://lobster.jugule.de"
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("lobster_site_qr.png")
