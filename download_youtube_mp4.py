import ssl
from pytube import YouTube
import os

# Fix SSL issue
ssl._create_default_https_context = ssl._create_unverified_context

def download_youtube_video():
    url = input("Enter the YouTube video URL: ").strip()
    
    if not url:
        print("Error: No URL provided. Please enter a valid YouTube link.")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        if stream:
            save_path = os.path.expanduser("~/Downloads")  # Set download directory (default: Downloads folder)
            print(f"Downloading: {yt.title} at {stream.resolution} resolution...")
            stream.download(output_path=save_path)
            print(f"Download completed! File saved in: {save_path}")
        else:
            print("Error: No suitable MP4 stream found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_youtube_video()
