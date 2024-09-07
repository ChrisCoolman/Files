import os
import shutil

# Delete Spam Directory
spam_directory = 'Spam'
if os.path.exists(spam_directory):
    shutil.rmtree(spam_directory)
    print(f"Deleted directory: {spam_directory}")
else:
    print(f"Directory {spam_directory} does not exist.")

# Create spam directory
os.makedirs(spam_directory, exist_ok=True)
print(f"Created directory: {spam_directory}")