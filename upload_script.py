import requests
import os

API_URL = "http://127.0.0.1:5000/api/transcripts"
TRANSCRIPT_DIR = "C:/Users/ryanm/Desktop/my_transcripts"

for filename in os.listdir(TRANSCRIPT_DIR):
    if filename.endswith(".txt"):
        filepath = os.path.join(TRANSCRIPT_DIR,filename)

        with open(filepath,'r') as f:
            content = f.read()
            new_transcript = {
                "mentor_id": "mentor-002",
                "title": filename,
                "content": content
            }

            try:
                response = requests.post(API_URL, json=new_transcript)
                if response.status_code == 201:
                    print(f"Successfully uploaded {filename}")
                else:
                    print(f"Failed to upload {filename}. Status: {response.status_code}")

            except Exception as e:
                print(f"Error uploading {filename}: {e}")
