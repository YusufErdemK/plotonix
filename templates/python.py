# python.py
"""
Python repository template for Plotonix.

This template sets up a GitHub repository suitable for Python projects,
with standard folder structure and files.
"""

# Default files and folders for Python repo
DEFAULT_FILES = [
    "README.md",
    "LICENSE",
    "requirements.txt",
    ".gitignore",
    "main.py",  # starter Python file
]

DEFAULT_FOLDERS = [
    "src",
    "tests",
    "docs",
]

def generate_python_repo():
    import os

    # Create folders
    for folder in DEFAULT_FOLDERS:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Create files with starter content
    for file in DEFAULT_FILES:
        if not os.path.exists(file):
            with open(file, "w") as f:
                if file == "README.md":
                    f.write(f"# {os.path.basename(os.getcwd())}\n\nGenerated using Plotonix Python template.\n")
                elif file == "LICENSE":
                    f.write("MIT License\n")
                elif file == "requirements.txt":
                    f.write("# Add your Python dependencies here\n")
                elif file == ".gitignore":
                    f.write("__pycache__/\n*.pyc\n")
                elif file == "main.py":
                    f.write("# Starter Python file\n")
                    f.write("def main():\n")
                    f.write("    print('Hello from Plotonix Python repo!')\n\n")
                    f.write("if __name__ == '__main__':\n")
                    f.write("    main()\n")

    print("Python repository template generated successfully.")

if __name__ == "__main__":
    generate_python_repo()
