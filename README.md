# Video_bot
📽️ Telegram YouTube Video Downloader Bot (WIP)
🔍 What is this?
This is a Telegram bot written in Python that allows users to download YouTube videos directly by sending a link to the bot. The bot uses the powerful yt_dlp library to fetch and convert videos, and automatically splits large videos into smaller chunks if the file size exceeds Telegram’s file upload limit.

✅ Features:
Supports downloading 480p videos or lower to ensure smaller sizes.

Automatically splits videos into 45MB chunks to bypass Telegram’s max upload limit.

Uses ffmpeg to convert and merge video/audio.

Fully functional Telegram bot setup with pyTelegramBotAPI.

⚙️ How it Works:
A user sends a YouTube link to the bot.

The bot downloads the video and converts it into .mp4.

If the video size is larger than 45MB, it's split into parts.

Each part is sent back to the user directly in the Telegram chat.

🚧 Current Limitations (To Be Fixed)
This code is still under development:

Some videos may not be downloaded properly due to format or resolution issues.

File size handling needs improvement: Telegram bots can't send files >50MB, so a better chunking or compression mechanism could be added.

The bot currently saves files to local storage but does not clean up afterward. This could clutter storage over time.

🧠 Call for Contributions
This project is open to the community! If you’re a Python/TG bot/yt-dlp wizard or just interested in automation projects — your input is welcome:

Fix/improve file-splitting logic

Add progress messages during download

Add file cleanup after sending

Optimize ffmpeg handling for speed and quality

🚀 How to Run
Install the requirements:

bash
Copy
Edit
pip install pyTelegramBotAPI yt-dlp
Make sure ffmpeg is correctly installed and the path is set in the script.

Run the bot:

bash
Copy
Edit
python bot.py
⚠️ Legal Disclaimer
This bot is for educational purposes only. Please respect content creators and copyright laws in your country.


