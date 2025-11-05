# Lobster - QR Code (Worship) Music Game

A music guessing game where players scan QR codes to play song snippets. The project consists of a SvelteKit web application for playing songs and Python scripts for downloading music from YouTube and generating QR codes.

## Project Structure

```
lobster/
├── web/                 # SvelteKit web application
│   ├── src/
│   │   ├── routes/      # App routes and API endpoints
│   │   └── lib/         # Shared components
│   └── package.json
├── qr-gen/             # Python scripts for song management
│   ├── main.py         # Main CLI script
│   ├── song.py         # Song database and QR generation
│   ├── songs.csv       # Song list (title;artist;year;youtube_url)
│   └── pixi.toml       # Python dependencies
└── README.md
```

## How It Works

1. **Song Management**: Songs are defined in `qr-gen/songs.csv` with their YouTube URLs
2. **Download**: Python scripts download audio from YouTube and convert to MP3
3. **QR Generation**: Generate QR codes containing unique song identifiers
4. **Game Play**: Players scan QR codes with the web app to play song snippets
5. **Audio Streaming**: Web app serves audio files and provides playback controls

## Setup

### Prerequisites

- **For Web App**: [Bun](https://bun.sh/) (JavaScript runtime and package manager)
- **For Python Scripts**: [Pixi](https://pixi.sh/) (Python package manager)

### Web Application Setup

1. Navigate to the web directory:

    ```bash
    cd web/
    ```

2. Install dependencies:

    ```bash
    bun install
    ```

3. Set up environment variables:
   Create a `.env` file or set the environment variable:
    ```bash
    export PUBLIC_SONGS_PATH="/path/to/your/downloaded/songs"
    ```
    This should point to the directory containing the downloaded MP3 files (typically `../qr-gen/downloads`).

### Python Scripts Setup

1. Navigate to the qr-gen directory:

    ```bash
    cd qr-gen/
    ```

2. Install dependencies using Pixi:
    ```bash
    pixi install
    ```

## Usage

### Managing Songs

1. **Edit the song list**: Add songs to `qr-gen/songs.csv` in the format:

    ```csv
    Title;Artist;Year;YouTube_URL
    Only Jesus;Casting Crowns;2018;https://www.youtube.com/watch?v=CAnf2qxtFb4
    ```

2. **Download songs from YouTube**:

    ```bash
    cd qr-gen/
    pixi run python main.py download
    ```

    This will:
    - Download audio from YouTube URLs in the CSV
    - Convert to MP3 format (192kbps)
    - Save files with short IDs in the `downloads/` directory
    - Track downloaded files to avoid re-downloading

3. **Generate QR codes**:
    ```bash
    cd qr-gen/
    pixi run python main.py qr
    ```
    This creates QR code images in the `codes/` directory. Each QR code contains a `lobster://` URL with the song's unique identifier.

### Running the Web Application

1. **Development mode**:

    ```bash
    cd web/
    bun run dev
    ```

    Access the app at `http://localhost:5173`

2. **Production build**:

    ```bash
    cd web/
    bun run build
    bun run preview
    ```

3. **Production deployment**:
   The app is configured to use the Node.js adapter. Build and deploy according to your hosting platform's requirements.

### Playing the Game

1. Open the web application on a device with a camera
2. Allow camera permissions for QR code scanning
3. Scan a generated QR code
4. The corresponding song will start playing automatically
5. Use the audio controls to pause, play, or adjust volume

## Technical Details

### Web App Technologies

- **SvelteKit**: Full-stack web framework
- **TypeScript**: Type-safe JavaScript
- **TailwindCSS**: Utility-first CSS framework
- **QR Scanner**: Browser-based QR code scanning
- **Bun**: Fast JavaScript runtime and package manager

### Python Technologies

- **yt-dlp**: YouTube video/audio downloader
- **qrcode**: QR code generation with PIL imaging
- **pathvalidate**: Safe filename generation
- **Pixi**: Modern Python package management

### Song ID System

Songs are identified by deterministic 24-character Base62 IDs generated from their YouTube URLs. This ensures:

- Consistent IDs across different runs
- URL-safe characters only
- Collision resistance for practical use cases

## Environment Variables

### Web App

- `PUBLIC_SONGS_PATH`: Directory containing downloaded MP3 files (required for production)

## Development

### Web App Development

```bash
cd web/
bun run dev          # Start development server
bun run check        # Type checking
bun run format       # Format code with Prettier
bun run lint         # Lint code
```

### Python Development

The Python scripts use Pixi for dependency management. All dependencies are defined in `pixi.toml`.

## Example Workflow

Here's a complete example of setting up and using the system:

1. **Initial Setup**:

    ```bash
    # Set up web app
    cd web/
    bun install

    # Set up Python environment
    cd ../qr-gen/
    pixi install
    ```

2. **Add Songs**: Edit `qr-gen/songs.csv` to add your songs with YouTube URLs

3. **Download and Generate**:

    ```bash
    cd qr-gen/
    pixi run python main.py download  # Download all songs
    pixi run python main.py qr        # Generate QR codes
    ```

4. **Start Web App**:

    ```bash
    cd ../web/
    export PUBLIC_SONGS_PATH="../qr-gen/downloads"
    bun run dev
    ```

5. **Play**: Open the web app, scan QR codes, and enjoy the music!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note**: Please ensure you have appropriate rights to download and use any copyrighted music content. This software is provided as-is and users are responsible for complying with applicable copyright laws when downloading content from YouTube or other sources.
