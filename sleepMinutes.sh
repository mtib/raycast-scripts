#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Custom sleep timer
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 💤
# @raycast.packageName Utilities
# @raycast.argument1 { "type": "text", "placeholder": "Minute timer" }

# Documentation:
# @raycast.description Sets a custom timer until the computer goes to sleep using shutdown.
# @raycast.author Markus
# @raycast.authorURL mtib.becker@gmail.com

./local-shutdown $1
