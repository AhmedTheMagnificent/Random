import os 
import re
import shutil

directory = r"C:\Users\ahmed\Downloads"
files = os.listdir(directory)
file_extensions = {
    ".txt": "text_files",
    ".md": "text_files",
    ".rtf": "text_files",
    ".doc": "document_files",
    ".docx": "document_files",
    ".pdf": "document_files",
    ".odt": "document_files",
    ".tex": "document_files",
    ".wps": "document_files",
    ".xls": "spreadsheet_files",
    ".xlsx": "spreadsheet_files",
    ".ods": "spreadsheet_files",
    ".csv": "spreadsheet_files",
    ".ppt": "presentation_files",
    ".pptx": "presentation_files",
    ".odp": "presentation_files",
    ".jpg": "image_files",
    ".jpeg": "image_files",
    ".png": "image_files",
    ".gif": "image_files",
    ".bmp": "image_files",
    ".tiff": "image_files",
    ".svg": "image_files",
    ".webp": "image_files",
    ".mp3": "audio_files",
    ".wav": "audio_files",
    ".aac": "audio_files",
    ".flac": "audio_files",
    ".m4a": "audio_files",
    ".wma": "audio_files",
    ".mp4": "video_files",
    ".avi": "video_files",
    ".mov": "video_files",
    ".wmv": "video_files",
    ".flv": "video_files",
    ".mkv": "video_files",
    ".webm": "video_files",
    ".zip": "compressed_files",
    ".rar": "compressed_files",
    ".7z": "compressed_files",
    ".tar": "compressed_files",
    ".gz": "compressed_files",
    ".bz2": "compressed_files",
    ".exe": "executable_files",
    ".msi": "executable_files",
    ".bat": "executable_files",
    ".sh": "executable_files",
    ".apk": "executable_files",
    ".jar": "executable_files",
    ".html": "web_files",
    ".htm": "web_files",
    ".css": "web_files",
    ".js": "web_files",
    ".php": "web_files",
    ".asp": "web_files",
    ".aspx": "web_files",
    ".xml": "data_files",
    ".json": "data_files",
    ".yaml": "data_files",
    ".yml": "data_files",
    ".sql": "data_files",
    ".db": "data_files",
    ".mdb": "data_files",
    ".sqlite": "data_files",
    ".sys": "system_files",
    ".dll": "system_files",
    ".ini": "system_files",
    ".log": "system_files",
    ".py": "programming_files",
    ".java": "programming_files",
    ".c": "programming_files",
    ".cpp": "programming_files",
    ".cs": "programming_files",
    ".rb": "programming_files",
    ".php": "programming_files",
    ".go": "programming_files",
    ".rs": "programming_files",
    ".iso": "other_files",
    ".dmg": "other_files",
    ".torrent": "other_files",
    ".ics": "other_files",
    ".bin": "other_files"
}

directory_names = [
    "text_files",
    "document_files",
    "spreadsheet_files",
    "presentation_files",
    "image_files",
    "audio_files",
    "video_files",
    "compressed_files",
    "executable_files",
    "web_files",
    "data_files",
    "system_files",
    "programming_files",
    "other_files"
]
for folder in directory_names:
    os.makedirs(os.path.join(directory, folder), exist_ok=True)

for fil in files:
    match = re.search(r"\.\w+$", fil)
    if match:
        endingPart = match.group()
        if endingPart in file_extensions:
            folder = file_extensions[endingPart]
            source_file = os.path.join(directory, fil)  
            destination_folder = os.path.join(directory, folder)
            shutil.move(source_file, os.path.join(destination_folder, fil)) 
