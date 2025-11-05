from bdb import GENERATOR_AND_COROUTINE_FLAGS
from dataclasses import dataclass
from pathlib import PurePath
import random
import string
from typing import override
import csv
import shutil
import os
from concurrent.futures import ProcessPoolExecutor
from yt_dlp import YoutubeDL, postprocessor
import qrcode
from pathvalidate import sanitize_filename


@dataclass
class Song:
    title: str
    artist: str | None = None
    year: int | None = None
    yt_url: str | None = None

    @override
    def __str__(self) -> str:
        return f"{self.title} by {self.artist} ({self.year}): {self.yt_url if self.yt_url else 'No URL'}"

    def qr_code(self) -> qrcode.image.pil.PilImage:
        if not self.yt_url:
            raise ValueError("No YouTube URL to generate QR code for.")

        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=10,
            border=4,
        )

        qr_data = f"lobster://{generate_short_id(self.yt_url, length=24)}"
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        return img


class SongDB:
    songs: list[Song] = []

    def from_csv(self, file_path: str):
        self.songs = []
        with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(
                csvfile,
                delimiter=";",
                fieldnames=["title", "artist", "year", "yt_url"],
            )
            for row in reader:
                if not row["title"]:  # Ensure title is present
                    continue
                self.songs.append(
                    Song(
                        title=row["title"],
                        artist=row["artist"],
                        year=int(row["year"]) if row["year"] else None,
                        yt_url=row["yt_url"] if row["yt_url"] else None,
                    )
                )

    def __iter__(self):
        return iter(self.songs)

    def __getitem__(self, index: int):
        return self.songs[index]

    def download_yt(self):
        params = {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "paths": {"home": "./downloads"},
            "outtmpl": "%(title)s.%(ext)s",
            "download_archive": "downloaded.txt",
            "noplaylist": True,
        }
        urls = [s.yt_url for s in self.songs if s.yt_url]
        yt_download_task(
            params,
            urls,
        )

    def generate_qr_codes(self, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        for song in self.songs:
            if not song.yt_url:
                continue
            file_name = sanitize_filename(f"{song.title}.png")
            img = song.qr_code()
            img.save(os.path.join(output_dir, file_name))


base62_chars = string.digits + string.ascii_letters


def generate_short_id(seed: str, length: int = 24) -> str:
    """Generate a random short ID of specified length using Base62 encoding."""
    random.seed(seed)
    return "".join(random.choice(base62_chars) for _ in range(length))


def yt_download_task(params, urls: list[str]):
    for url in urls:
        id = generate_short_id(url, length=24)

        if os.path.exists(os.path.join("downloads", f"{id}.mp3")):
            print(f"File for URL {url} already exists as {id}.mp3, skipping download.")
            continue

        with YoutubeDL(params=params) as ydl:
            ydl.add_post_processor(FileRenamer(id), when="post_process")
            try:
                ydl.download(url)
            except Exception as _:
                pass


class FileRenamer(postprocessor.PostProcessor):
    new_file_name: str

    def __init__(self, new_file_name: str, downloader=None):
        postprocessor.PostProcessor.__init__(self, downloader)
        self.new_file_name = new_file_name

    def run(self, info):
        oldfile = info["filepath"]
        ext = PurePath(oldfile).suffix
        dir = info.get("__finaldir")
        newfile = os.path.join(dir, PurePath(self.new_file_name).with_suffix(ext))
        shutil.move(oldfile, newfile)
        self.to_screen(f"Renamed file {oldfile} to {newfile}")
        return [], info
