import moviepy.editor as mp
from moviepy.config import change_settings
import numpy as np

# Update the path to the ImageMagick binary
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

# Define the input video and the desired output duration for each part
input_video = "house-car.mp4"
output_video = "output/output-trap-text-linear.mp4"
desired_duration = 396  # ~ 5 minutes

# Load the input video
clip = mp.VideoFileClip(input_video)

# Calculate the number of times the clip needs to be repeated
clip_duration = clip.duration
num_repeats = int(desired_duration // clip_duration) + 1

# Create a concatenated clip
clips = [clip] * num_repeats
final_clip = mp.concatenate_videoclips(clips)

# Trim the final clip to the exact desired duration
final_clip = final_clip.subclip(0, desired_duration)

# Define the text clip
txt_clip = mp.TextClip("Lofi Trap Mix", fontsize=120, font="Comic-Sans-MS", color='#1e0449').set_duration(desired_duration)

# Define a position function to make the text move in straight lines slowly
def linear_move(t):
    x = 700 + 250 * np.cos(0.1 * np.pi * t)
    y = 400 + 150 * np.sin(0.1 * np.pi * t)
    return (x, y)

# Apply the position function to the text clip
txt_clip = txt_clip.set_position(linear_move)

# Composite the text clip on top of the video
video = mp.CompositeVideoClip([final_clip, txt_clip])

# Write the output video
video.write_videofile(output_video, codec="libx264", audio=False)
