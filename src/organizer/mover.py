import shutil
from pathlib import Path

from .rules import categorize


def free_path(folder: Path, name: str) -> Path:
    """Restituisce un percorso libero in folder, aggiungendo _1, _2... se serve."""
    candidate = folder / name
    stem = Path(name).stem
    suffix = Path(name).suffix
    n = 1
    while candidate.exists():
        candidate = folder / f"{stem}_{n}{suffix}"
        n += 1
    return candidate


def move_file(file: Path, base: Path) -> Path:
    """Sposta un file in base/Categoria/ e restituisce il nuovo percorso."""
    category = categorize(file)
    dest_folder = base / category
    dest_folder.mkdir(parents=True, exist_ok=True)
    dest = free_path(dest_folder, file.name)
    shutil.move(file, dest)
    return dest