import os 
import shutil 
 
FILE_TYPES = { 
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"], 
    "Videos": [".mp4", ".mov", ".avi", ".mkv"], 
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"], 
    "Audio": [".mp3", ".wav", ".aac"], 
} 
 
def organize_files(folder_path): 
    if not os.path.exists(folder_path): 
        print("The folder does not exist!") 
        return 
 
    for filename in os.listdir(folder_path): 
        file_path = os.path.join(folder_path, filename) 
 
        if os.path.isdir(file_path): 
            continue 
 
        ext = os.path.splitext(filename)[1].lower() 
        moved = False 
 
        for category, extensions in FILE_TYPES.items(): 
            if ext in extensions: 
                category_folder = os.path.join(folder_path, category) 
                os.makedirs(category_folder, exist_ok=True) 
 
                ext_folder = os.path.join(category_folder, ext[1:]) 
                os.makedirs(ext_folder, exist_ok=True) 
 
                shutil.move(file_path, os.path.join(ext_folder, filename)) 
                print(f"Moved: {filename} -^> {category}/{ext[1:]}") 
 
                moved = True 
                break 
 
        if not moved: 
            others_folder = os.path.join(folder_path, "Others") 
            os.makedirs(others_folder, exist_ok=True) 
 
            ext_folder = os.path.join(others_folder, ext[1:] if ext else "Others") 
            os.makedirs(ext_folder, exist_ok=True) 
 
            shutil.move(file_path, os.path.join(ext_folder, filename)) 
            print(f"Moved: {filename} -^> Others") 
 
    print("\nThe files have been successfully sorted!") 
 
folder_path = input("Enter folder path: ") 
organize_files(folder_path) 
