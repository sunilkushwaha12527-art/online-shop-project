import requests
import time
import os

# --- Configuration ---
# Aapko Luma AI ya Runway ki API key yahan daalni hogi
API_KEY = "YOUR_EXTERNAL_SERVER_API_KEY" 
API_ENDPOINT = "https://api.luma.ai/v1/generations" # Example for Luma

def generate_15s_video(prompt):
    print(f"🚀 Processing your 15-second video for: {prompt}")
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "prompt": prompt,
        "aspect_ratio": "16:9",
        "loop": False,
        "duration": 15  # Specific for 15s
    }

    # 1. Video Request bhejna
    response = requests.post(API_ENDPOINT, json=payload, headers=headers)
    
    if response.status_code == 201:
        job_id = response.json().get("id")
        print(f"✅ Job Created! ID: {job_id}")
        return job_id
    else:
        print(f"❌ Error: {response.text}")
        return None

# --- Main Program ---
if __name__ == "__main__":
    user_prompt = input("Aap kis cheez ki 15s video banana chahte hain? ")
    job = generate_15s_video(user_prompt)
    
    if job:
        print("\n⏳ Ab server video bana raha hai... GitHub par update karke chill karein!")

