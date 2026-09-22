import os
import glob
import shutil

# 1. Define paths
base_dir = "."
target_dir = os.path.join(base_dir, "notebooks")

# 2. Create 'notebooks' folder if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# 3. Find all .ipynb files in the root folder
ipynb_files = [f for f in glob.glob(os.path.join(base_dir, "*.ipynb")) if os.path.isfile(f)]

# 4. Move each notebook (preserving all cells and content)
for file_path in ipynb_files:
    filename = os.path.basename(file_path)
    destination = os.path.join(target_dir, filename)
    
    shutil.move(file_path, destination)
    print(f"Successfully moved full notebook: {filename} -> notebooks/")

print("\nDone! All cells and notebook content have been preserved.")