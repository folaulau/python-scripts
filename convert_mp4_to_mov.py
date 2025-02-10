import ffmpeg
import os
import time

def convert_mp4_to_mov_1080p(input_file, output_file):
    start_time = time.time()  # Start timer

    try:
        print(f"Starting conversion: {input_file} -> {output_file}")

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

        print(f"Conversion successful: {output_file}")
        print(f"Time taken: {minutes} min {seconds} sec")

    except ffmpeg.Error as e:
        print(f"Error: {e}")

# Example usage
input_mp4 = "C0091_1-31-25_xl_report.MP4"
output_mov = os.path.splitext(input_mp4)[0] + "_1080p.mov"
convert_mp4_to_mov_1080p(input_mp4, output_mov)
