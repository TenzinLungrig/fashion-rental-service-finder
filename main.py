import os
import shutil
CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".png", ".gif"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"]
}
TARGET_DIR = "C:/Users/Tenzin/Downloads"
def organize_files():
    for category in CATEGORIES:
        os.makedirs(os.path.join(TARGET_DIR, category), exist_ok=True)
    for filename in os.listdir(TARGET_DIR):
        filepath = os.path.join(TARGET_DIR, filename)
        if os.path.isdir(filepath) or filename.startswith("."):
            continue
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  
        moved = False
        for category, extensions in CATEGORIES.items():
            if ext in extensions:
                shutil.move(filepath, os.path.join(TARGET_DIR, category, filename))
                print(f"Moved '{filename}' to '{category}'")
                moved = True
                break
        if not moved:
            print(f"Unknown file type: '{filename}'")
if __name__ == "__main__":
    organize_files()
