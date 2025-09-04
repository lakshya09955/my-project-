# This file looks for new folders inside user_uploads and converts them to reel videos if they are not already converted.
import os
import time
from text_to_audio import text_to_speech_file  # Assuming this is the function from your text_to_audio.py
import subprocess

def text_to_audio(folder):
    print("TTA -",folder)
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
    print(text,folder)
    text_to_speech_file(text,folder)

def create_reel(folder):
    command=f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf \"scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black\" -c:v libx264 -c:a aac -shortest -r  30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    subprocess.run(command, shell=True, check=True)
    print("CR -",folder)

if __name__ == "__main__":
    while True:
        print("Processing queue...")
        with open("done.txt", "r") as f:
            done_folders = f.readlines()
        done_folders = [f.strip() for f in done_folders]  # Clean up the list
        folders = os.listdir("user_uploads")
        for folder in folders:
            if folder not in done_folders:
                text_to_audio(folder) #Generate the audio from desc.txt
                create_reel(folder)  # Create the reel video from the audio.mp3 and images in the folder
                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
        time.sleep(4)