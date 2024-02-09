import csv
import os

def match_audio_files(word_list):
    audio_mappings = {}
    try:
        with open('VoiceMap.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                audio_mappings[row[0]] = row[1]

        result = []
        for word in word_list:
            if word in audio_mappings:
                result.append((word, audio_mappings[word]))
            else:
                result.append((word, None))

    except FileNotFoundError:
        print("Error: The file 'VoiceMap.csv' was not found.")
        return []
    except Exception as e:
        print("Error: An unexpected error occurred while reading 'VoiceMap.csv'. Error details: " + str(e))
        return []

    return result
