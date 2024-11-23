#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Ask GPT a question about an image
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🎨
# @raycast.packageName Developer Utils
# @raycast.argument1 { "type": "text", "placeholder": "Prompt" }

# Documentation:
# @raycast.description Asks GPT a question about an image
# @raycast.author Markus
# @raycast.authorURL mabe@monta.com

import base64
import datetime
import sys
import requests
import creds

# OpenAI API Key
api_key = creds.openai_api_key

image_path = sys.argv[1]
questions = {
  "style": "Describe the style of this image so that an AI could reproduce it.",
  "content": "Describe the content of this image so that an AI could reproduce it.",
  "detail": "Describe this image in high detail, describing both content and style."
}
question_select = "detail"
question = questions[question_select]

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-turbo",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": question
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 1000
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())
with open("image_query.log", "a") as f:
    f.write(f"{datetime.datetime.now().isoformat()} {image_path} {response.json()['choices'][0]['message']['content']}\n")
