import os
import shutil

# Get the path from the user
path = input("Enter Path: ")

# Get a list of all subfolders in the specified path
subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

# Loop through each subfolder
for subfolder in subfolders:
    # Get a list of all files in the subfolder
    files = os.listdir(subfolder)
    
    # Loop through each file in the subfolder
    for file in files:
        # Calculate the source and destination paths
        source_path = os.path.join(subfolder, file)
        destination_path = os.path.join(path, file)
        
        # Move the file from subfolder to the main folder
        shutil.move(source_path, destination_path)

    # Remove the now empty subfolder
    os.rmdir(subfolder)

# Unorganizing process completed
print("Files unorganized successfully!")
