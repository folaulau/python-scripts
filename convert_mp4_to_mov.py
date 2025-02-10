import ffmpeg
import os
import time

def convert_mp4_to_mov_1080p(input_file, output_file):
    """Convert an MP4 file to MOV in 1080p resolution."""
    start_time = time.time()  # Start timer

    try:
        print(f"🎬 Starting conversion: {input_file} -> {output_file}")

        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec="libx264", acodec="aac", vf="scale=1920:1080")
            .run(overwrite_output=True)
        )

        end_time = time.time()  # End timer
        elapsed_time = end_time - start_time

        # Convert elapsed time to minutes and seconds
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        print(f"✅ Conversion successful: {output_file}")
        print(f"⏱ Time taken: {minutes} min {seconds} sec\n")

    except ffmpeg.Error as e:
        print(f"❌ Error converting {input_file}: {e}")

def batch_convert_mp4_to_mov(folder_path):
    """Scan folder and convert all MP4 files to MOV in 1080p if not already converted."""
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    # Get all .mp4 or .MP4 files
    mp4_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.mp4')]

    if not mp4_files:
        print("⚠️ No MP4 files found in the folder.")
        return

    print(f"🔍 Found {len(mp4_files)} MP4 files for conversion.")

    for file in mp4_files:
        input_file = os.path.join(folder_path, file)
        output_file = os.path.splitext(input_file)[0] + "_1080p.mov"

        # Check if MOV file already exists
        if os.path.exists(output_file):
            print(f"⚡ Skipping {file}: Already converted.")
            continue  # Skip conversion if file exists

        convert_mp4_to_mov_1080p(input_file, output_file)

# Example usage
folder_path = "/Users/folaukaveinga/BAE/Meeting_Recordings"  # Replace with the actual folder path
batch_convert_mp4_to_mov(folder_path)
