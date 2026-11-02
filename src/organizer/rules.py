from pathlib import Path

CATEGORIES = {
    "Immagini": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documenti": {".pdf", ".doc", ".docx", ".odt", ".txt", ".md"},
    "Archivi": {".zip", ".tar", ".gz", ".xz", ".7z", ".rar"},
    "Video": {".mp4", ".mkv", ".avi", ".webm"},
    "Audio": {".mp3", ".flac", ".ogg", ".wav"},
    "Installer": {".rpm", ".deb", ".appimage"},
}


def categorize(path: Path) -> str:
    ext = path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Altro"