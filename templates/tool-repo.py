# tool-repo.py
"""
Tool repository template for Plotonix.

This template sets up a GitHub repository suitable for CLI tools or
small utility projects.
"""

# Default files and folders for tool repo
DEFAULT_FILES = [
    "README.md",
    "LICENSE",
    "requirements.txt",
    ".gitignore",
    "main.py",  # starter script
]

DEFAULT_FOLDERS = [
    "bin",
    "src",
    "docs",
    "tests",
]

def generate_tool_repo():
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
                    f.write(f"# {os.path.basename(os.getcwd())}\n\nGenerated using Plotonix tool template.\n")
                elif file == "LICENSE":
                    f.write("MIT License\n")
                elif file == "requirements.txt":
                    f.write("# Add your Python dependencies here\n")
                elif file == ".gitignore":
                    f.write("__pycache__/\n*.pyc\n")
                elif file == "main.py":
                    f.write("# Starter script for your tool\n")
                    f.write("def main():\n")
                    f.write("    print('Hello from Plotonix tool repo!')\n\n")
                    f.write("if __name__ == '__main__':\n")
                    f.write("    main()\n")

    print("Tool repository template generated successfully.")

if __name__ == "__main__":
    generate_tool_repo()
