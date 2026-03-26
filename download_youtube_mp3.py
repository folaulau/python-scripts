from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_as_mp3(url, output_folder="downloads"):
    try:
        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Download the highest quality audio
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download(output_path=output_folder)

        # Convert to MP3 using pydub
        mp3_file = os.path.join(output_folder, yt.title + ".mp3")
        audio = AudioSegment.from_file(audio_file)
        audio.export(mp3_file, format="mp3")

        # Remove the original audio file (optional)
        os.remove(audio_file)

        print(f"Download complete: {mp3_file}")
        return mp3_file

    except Exception as e:
        print(f"Error: {e}")

# Example usage
video_url = input("Enter YouTube video URL: ")
download_youtube_as_mp3(video_url)
