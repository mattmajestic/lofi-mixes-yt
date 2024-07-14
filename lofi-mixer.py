import moviepy.editor as mp

# Define the input video and the desired output duration for each part
input_video = "skateboard.mp4"
output_video = "output-skateboard.mp4"
desired_duration = 308  # ~ 5 minutes 

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

# Write the output video
final_clip.write_videofile(output_video, codec="libx264", audio=False)
