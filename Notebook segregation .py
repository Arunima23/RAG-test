import os
import glob
import shutil

# 1. Define base path and target notebook directory
base_dir = "."
target_dir = os.path.join(base_dir, "notebooks")

# 2. Create the 'notebooks' directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# 3. Find all .ipynb files in the root folder
ipynb_files = glob.glob(os.path.join(base_dir, "*.ipynb"))

# 4. Move each notebook into the 'notebooks' folder
for file_path in ipynb_files:
    filename = os.path.basename(file_path)
    destination = os.path.join(target_dir, filename)
    
    shutil.move(file_path, destination)
    print(f"Moved: {filename} -> notebooks/")

print("\nAll .ipynb files moved successfully!")