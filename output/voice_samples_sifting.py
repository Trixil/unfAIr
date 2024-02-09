
# Python script to go through all voice samples in the provided directory
import os

# Set the directory path where voice samples reside
dir_path = "/path_to_directory_with_voice_samples"

# List all files in the given directory
voice_samples = [entry.path for entry in os.scandir(dir_path) if entry.is_file()]

# Pseudocode:
# import necessary libraries
# set the directory path where the voice samples are located
# fetch the list of all files in the directory
# if a file is a voice sample, add it to the list of voice samples
