#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title 1h sleep timer
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 💤
# @raycast.packageName Utilities

# Documentation:
# @raycast.description Sets a 1h timer until the computer goes to sleep using shutdown.
# @raycast.author Markus
# @raycast.authorURL mtib.becker@gmail.com

./local-shutdown 60
