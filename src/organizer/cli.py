import argparse
from pathlib import Path

from .mover import move_file
from .rules import categorize


def main():
    parser = argparse.ArgumentParser(
        prog="organizer",
        description="Organizza i file di una cartella in sottocartelle per categoria.",
    )
    parser.add_argument("cartella", type=Path, help="cartella da organizzare")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="mostra cosa farebbe, senza spostare nulla",
    )

    args = parser.parse_args()
    if not args.cartella.is_dir():
        parser.error("non è una cartella valida.")

    for f in sorted(args.cartella.iterdir()):
        if not f.is_file() or f.name.startswith("."):
            continue

        if args.dry_run:
            print(f"{f.name} -> {categorize(f)}/{f.name}")
        else:
            dest = move_file(f, args.cartella)
            print(f"{f.name} -> {dest.relative_to(args.cartella)}")


if __name__ == "__main__":
    main()