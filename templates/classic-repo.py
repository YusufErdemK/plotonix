# classic-repo.py
"""
Classic repository template for Plotonix.

This file is used as a reference to generate the initial files
for a standard GitHub repository.
"""

# Example: default files and folders for a classic repo
DEFAULT_FILES = [
    "README.md",
    "LICENSE",
    "requirements.txt",
    ".gitignore",
]

DEFAULT_FOLDERS = [
    "src",
    "docs",
    "tests",
]

def generate_classic_repo():
    import os

    # Create folders
    for folder in DEFAULT_FOLDERS:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Create files
    for file in DEFAULT_FILES:
        if not os.path.exists(file):
            with open(file, "w") as f:
                if file == "README.md":
                    f.write(f"# {os.path.basename(os.getcwd())}\n\nGenerated using Plotonix classic template.\n")
                elif file == "LICENSE":
                    f.write("MIT License\n")
                elif file == "requirements.txt":
                    f.write("# Add your Python dependencies here\n")
                elif file == ".gitignore":
                    f.write("__pycache__/\n*.pyc\n")

    print("Classic repository template generated successfully.")

if __name__ == "__main__":
    generate_classic_repo()
