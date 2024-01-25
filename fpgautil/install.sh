#!/bin/bash

# Set source and destination directories
source_dir=~/fpgautil
destination_dir=/usr/bin

# Check if the source directory exists
if [ ! -d "$source_dir" ]; then
    echo "Source directory does not exist: $source_dir"
    exit 1
fi

# Check if the destination directory exists, if not, create it
if [ ! -d "$destination_dir" ]; then
    echo "Destination directory does not exist, creating: $destination_dir"
    sudo mkdir -p "$destination_dir"
fi

# Copy files from source to destination
sudo cp -r "$source_dir"/* "$destination_dir"

# Make the destination file executable
sudo chmod +x "$destination_dir/fpgautil"

echo "Files copied successfully from $source_dir to $destination_dir"
echo "fpgautil is now executable in $destination_dir"
