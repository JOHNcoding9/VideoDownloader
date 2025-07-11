# 📽️ Video Downloader
An easy-to-use and intuitive media downloader for videos and audio.  
Just copy a URL from YouTube or other supported media platforms, paste it into the application, and click **Download**.  
Files will be saved in your `downloads/` folder, and YouTube content will be organized into a `downloads/youtube/` subfolder.

 # 🎯 Features
- ✅ Download full video in best available quality
- ✅ Optionally Extract audio only (MP3, 192kbps)
- ✅ Optionally generate and download subtitles (PT-BR)
- ✅ Detect and handle YouTube, Shorts, TikTok, Twitch clips, and more
- ✅ Clean, minimal, user-friendly interface (`tkinter`)

# 🛠️ Technologies Used
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) — for video/audio downloading
- [`ffmpeg`](https://ffmpeg.org/) — for conversion and subtitle handling
-- `tkinter` — GUI components
- `validators` — URL validation
- `urllib.parse` — domain parsing

  
## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/JOHNcoding9/videoDownloader.git
cd videoDownloader
