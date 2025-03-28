import os
import shutil
CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".png", ".gif"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
}
TARGET_DIR = "C:/Users/YourName/Downloads"
def create_category_folders():
    for category in CATEGORIES:
        folder_path = os.path.join(TARGET_DIR, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")


def get_file_category(file_extension):
    # Find which category this file belongs to
    for category, extensions in CATEGORIES.items():
        if file_extension in extensions:
            return category
    return None  # If no match found


def organize_files():
    create_category_folders()
    for filename in os.listdir(TARGET_DIR):
        filepath = os.path.join(TARGET_DIR, filename)
        if os.path.isdir(filepath) or filename.startswith("."):
            continue
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        category = get_file_category(ext)

        if category:
            dest_path = os.path.join(TARGET_DIR, category, filename)
            
            if os.path.exists(dest_path):
                base_name, extension = os.path.splitext(filename)
                counter = 1
                
                while os.path.exists(dest_path):
                    new_filename = f"{base_name}_{counter}{extension}"
                    dest_path = os.path.join(TARGET_DIR, category, new_filename)
                    counter += 1
                print(f"File already exists. Renaming to: {new_filename}")
            
            shutil.move(filepath, dest_path)
            print(f"Moved '{filename}' to '{category}'")
        else:
            print(f"Unknown file type: '{filename}' — leaving in place for now.")

if __name__ == "__main__":
    print("Starting file organization. This might take a moment...")
    organize_files()
    print("Organization complete. 🎉")
