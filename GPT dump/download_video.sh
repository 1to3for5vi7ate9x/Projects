#!/bin/bash

# Check if youtube-dl is installed
command -v youtube-dl >/dev/null 2>&1 || {
    echo >&2 "youtube-dl is required but it's not installed. Aborting.";
    exit 1;
}

# Check if URL was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <YouTube_URL>"
    exit 1
fi

# Download the video at highest quality with audio
youtube-dl -f 'bestvideo+bestaudio/best' $1

exit 0

