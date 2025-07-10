import os
from tkinter import filedialog

FOLDER_MAPPING = {
    ".jpg": "Bilder",
    ".jpeg": "Bilder",
    ".png": "Bilder",
    ".bmp": "Bilder",
    ".gif": "Bilder",
    ".tiff": "Bilder",
    ".svg": "Bilder",
    ".zip": "Archive",
    ".rar": "Archive",
    ".7z": "Archive",
    ".tar": "Archive",
    ".iso": "Archive",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".mp4": "Video",
    ".avi": "Video",
    ".mkv": "Video",
    ".mov": "Video",
    ".pdf": "Dokumente",
    ".docx": "Dokumente",
    ".xlsx": "Dokumente",
    ".txt": "Dokumente",
    ".log": "Dokumente",
    ".one": "Dokumente",
    ".csv": "Dokumente",
    ".ppt": "Dokumente",
    ".pptx": "Dokumente",
    ".yaml": "Skripts",
    ".json": "Skripts",
    ".xml": "Skripts",
    ".py": "Skripts",
    ".java": "Skripts",
    ".js": "Skripts",
    ".html": "Links",
    ".msg": "Mails",
    ".exe": "Anwendungen"
}

# Alle unbekannten Dateiendungen werden in "Sonstiges" einsortiert
DEFAULT_FOLDER = "Sonstiges"

