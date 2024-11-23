#!/Users/mtib/Documents/Raycast/.venv/bin/python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Generate DALL·E 3 Image
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🎨
# @raycast.packageName Developer Utils
# @raycast.argument1 { "type": "text", "placeholder": "Prompt" }

# Documentation:
# @raycast.description Generates and opens DALL·E 3 image
# @raycast.author Markus
# @raycast.authorURL mabe@monta.com

import math
import creds
import datetime
import httplib2
import openai
import os
import re
import sys
import time

run_identifier = hex(math.floor(time.time()))[2:]

def log(message):
    print(message)
    with open("dalle3.log", "a") as f:
        f.write(f"{datetime.datetime.now().isoformat()} run={run_identifier} {message}\n")

def generate_dalle_3(description):
    client = openai.OpenAI(api_key=creds.openai_api_key)
    return client.images.generate(
        model="dall-e-3",
        prompt=description,
        size="1024x1024",
        n=1,
    )

if __name__ == '__main__':
    description = sys.argv[1]
    log(f"Starting with '{description}'")

    try:
        response = generate_dalle_3(
            description=description
        )
        image_url = response.data[0].url
        rewritten_description = response.data[0].revised_prompt
        image_response = httplib2.Http().request(image_url, "GET")[1]
        image_filepath = os.path.join(os.environ.get('HOME'), "Pictures", "Dalle3", re.sub(r"[^a-zA-Z0-9_]", "", "_".join([*description.split(" ")[0:6], run_identifier])) + ".png")
        for k, v in [
            ['Description', description],
            ['Rewritten Description', rewritten_description],
            ['Image URL', image_url],
            ['Image Filepath', image_filepath],
        ]:
            log(f"{k}: {v}")
        with open(image_filepath, "wb") as f:
            f.write(image_response)
        log("Opening image")
        os.system(f"open '{image_filepath}'")
        #os.system(f"pbcopy < '{image_filepath}'")
    except Exception as e:
        log(str(e))
        log("Failed with error")
        exit(1)
