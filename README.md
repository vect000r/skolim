# Skolim Discord Music Bot

Skolim is a Discord music bot that allows you to play music in your Discord server. It uses `discord.py` and `yt-dlp` to stream audio from YouTube.

## Features

- Play music from YouTube
- Simple command interface

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/vect000r/skolim
    cd skolim
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Discord bot token:
    ```env
    discord_token=YOUR_DISCORD_BOT_TOKEN
    ```

## Usage

1. Run the bot:
    ```sh
    python3 main.py
    ```

2. Invite the bot to your Discord server.

3. Use the `?play <YouTube URL>` command to play music.

## Example

```
?play https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)
