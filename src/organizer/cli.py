import argparse
from pathlib import Path
from .rules import categorize


def main():
    parser = argparse.ArgumentParser(
        prog='organizer'
    )

    parser.add_argument('cartella', type=Path)
    parser.add_argument('--dry-run', action='store_true')

    args = parser.parse_args()
    if not args.cartella.is_dir():
        parser.error("non è una cartella valida.")

    folder = args.cartella

    for f in sorted(folder.iterdir()):
        if f.is_file():
            print(f"{categorize(f)}/{f.name}")
if __name__ == "__main__":
    main()