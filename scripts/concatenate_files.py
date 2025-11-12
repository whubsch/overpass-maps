#!/usr/bin/env python3
"""
Concatenate YAML and TXT files into .ultra files.

This script replicates the functionality of the GitHub Actions workflow
that combines YAML and TXT files from each directory into a single .ultra file.
"""

from pathlib import Path


def main():
    """
    Find all directories in data/ and concatenate matching YAML and TXT files.

    For each directory in data/, this script:
    1. Looks for a YAML file named {dirname}.yaml
    2. Looks for a TXT file named {dirname}.txt
    3. If both exist, creates {dirname}.ultra in the output directory
    4. The .ultra file contains the YAML wrapped in --- delimiters, followed by the TXT content
    """
    # Get the script's parent directory (project root)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Define data directory
    data_dir = project_root / "data"

    # Check if data directory exists
    if not data_dir.exists():
        print(f"Error: data directory not found at {data_dir}")
        return

    # Create output directory if it doesn't exist
    output_dir = project_root / "output"
    output_dir.mkdir(exist_ok=True)

    with open(data_dir / "common.yaml", "r", encoding="utf-8") as f:
        common_content = f.read()

    # Find all directories in the data folder
    for item in data_dir.iterdir():
        if not item.is_dir():
            continue

        dir_name = item.name

        # Skip hidden directories
        if dir_name.startswith("."):
            continue

        # Check for matching YAML and TXT files
        yaml_file = item / f"{dir_name}.yaml"
        txt_file = item / f"{dir_name}.txt"
        output_file = output_dir / f"{dir_name}.ultra"

        if yaml_file.exists() and txt_file.exists():
            print(f"Processing {dir_name}...")

            try:
                # Read the YAML file
                with open(yaml_file, "r", encoding="utf-8") as f:
                    yaml_content = f.read()

                # Read the TXT file
                with open(txt_file, "r", encoding="utf-8") as f:
                    txt_content = f.read()

                # Write combined content to .ultra file
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write("---\n")
                    f.write(common_content)
                    if not common_content.endswith("\n"):
                        f.write("\n")
                    f.write(yaml_content)
                    if not yaml_content.endswith("\n"):
                        f.write("\n")
                    f.write("---\n")
                    f.write(txt_content)

                print(f"Created {output_file.relative_to(project_root)}")

            except Exception as e:
                print(f"Error processing {dir_name}: {e}")
        else:
            missing = []
            if not yaml_file.exists():
                missing.append("yaml")
            if not txt_file.exists():
                missing.append("txt")
            print(f"Skipping {dir_name} (missing {' and '.join(missing)} file)")


if __name__ == "__main__":
    main()
