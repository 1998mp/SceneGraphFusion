import os

source_folder = "/path/to/source_folder/"  # replace with the path to the source folder
target_folder = "/path/to/target_folder/"  # replace with the path to the target folder

# Create the target folder if it doesn't exist
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# get a list of all the JPG files in the source folder
files_color = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]

# sort the files by name
files_color.sort()

# loop through the files and rename/move them
for i, file_name in enumerate(files_color):
    # construct the new file name and path in the target folder
    new_name = f"frame-{i:06d}.color.jpg"
    new_path = os.path.join(target_folder, new_name)
    # build the full file path for the source file
    old_path = os.path.join(source_folder, file_name)
    # rename/move the file
    os.rename(old_path, new_path)

# get a list of all the TXT files in the source folder
files_pose = [f for f in os.listdir(source_folder) if f.endswith('.txt')]

# sort the files by name
files_pose.sort()

# loop through the files and rename/move them
for i, file_name in enumerate(files_pose):
    # construct the new file name and path in the target folder
    new_name = f"frame-{i:06d}.pose.txt"
    new_path = os.path.join(target_folder, new_name)
    # build the full file path for the source file
    old_path = os.path.join(source_folder, file_name)
    # rename/move the file
    os.rename(old_path, new_path)

# get a list of all the PGM files in the source folder
files_depth = [f for f in os.listdir(source_folder) if f.endswith('.pgm')]

# sort the files by name
files_depth.sort()

# loop through the files and rename/move them
for i, file_name in enumerate(files_depth):
    # construct the new file name and path in the target folder
    new_name = f"frame-{i:06d}.depth.pgm"
    new_path = os.path.join(target_folder, new_name)
    # build the full file path for the source file
    old_path = os.path.join(source_folder, file_name)
    # rename/move the file
    os.rename(old_path, new_path)

