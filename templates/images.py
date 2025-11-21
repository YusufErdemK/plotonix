# images.py
"""
Images repository template for Plotonix.

This template sets up a GitHub repository suitable for projects
with image or media content.
"""

# Default files and folders for image repo
DEFAULT_FILES = [
    "README.md",
    "LICENSE",
    ".gitignore",
]

DEFAULT_FOLDERS = [
    "images",
    "assets",
    "docs",
]

def generate_images_repo():
    import os

    # Create folders
    for folder in DEFAULT_FOLDERS:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Create placeholder files
    for file in DEFAULT_FILES:
        if not os.path.exists(file):
            with open(file, "w") as f:
                if file == "README.md":
                    f.write(f"# {os.path.basename(os.getcwd())}\n\nGenerated using Plotonix images template.\n")
                elif file == "LICENSE":
                    f.write("MIT License\n")
                elif file == ".gitignore":
                    f.write("*.DS_Store\n*.thumbs\n")

    print("Images repository template generated successfully.")

if __name__ == "__main__":
    generate_images_repo()
