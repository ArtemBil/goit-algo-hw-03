import shutil
import sys
from pathlib import Path


def copy_files_recursively(source_dir, dest_dir):
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)

    if not source_path.exists():
        print(f"Source directory {source_path} does not exist.")
        return

    for item in source_path.rglob('*'):
        if item.is_file():
            try:
                file_ext = item.suffix[1:] if item.suffix else 'no_extension'
                target_dir = dest_path / file_ext
                target_dir.mkdir(parents=True, exist_ok=True)

                shutil.copy2(item, target_dir)
                print(f"Copied {item} to {target_dir}")
            except Exception as e:
                print(f"Error copying file {item}: {e}")


def main():
    if len(sys.argv) < 2:
        print("Error: Source directory is required.")
        return

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    source_path = Path(source_dir)
    if not source_path.exists():
        print(f"Error: Output dir {source_path} does not exist")
        return

    try:
        copy_files_recursively(source_dir, dest_dir)
        print("Copying is finished.")
    except Exception as e:
        print(f"Error during copying: {e}")


if __name__ == "__main__":
    main()
