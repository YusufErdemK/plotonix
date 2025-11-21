#!/usr/bin/env python3
import os
import sys
import json
import shutil

# Paths
CONFIG_PATH = "json/config.json"
GITHUB_PATH = "json/github.json"
TEMPLATES_DIR = "templates"

# Default template mapping
TEMPLATE_MAP = {
    "classic": "classic-repo.py",
    "images": "images.py",
    "python": "python.py",
    "tool": "tool-repo.py"
}

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def init_user_data():
    github_data = load_json(GITHUB_PATH)
    if not github_data.get("username"):
        username = input("Enter your GitHub username: ").strip()
        github_data["username"] = username
        save_json(GITHUB_PATH, github_data)

    config_data = load_json(CONFIG_PATH)
    if not config_data.get("default_license"):
        license_type = input("Enter default license (e.g., MIT, Apache-2.0): ").strip()
        config_data["default_license"] = license_type
        save_json(CONFIG_PATH, config_data)

def create_repo(template_key="classic"):
    template_file = TEMPLATE_MAP.get(template_key)
    if not template_file:
        print(f"Template '{template_key}' not found. Using classic template.")
        template_file = TEMPLATE_MAP["classic"]

    template_path = os.path.join(TEMPLATES_DIR, template_file)
    if not os.path.exists(template_path):
        print(f"Template file {template_path} does not exist.")
        return

    # Copy template content to main repo files
    repo_files = ["README.md", "LICENSE"]
    for file_name in repo_files:
        with open(file_name, "w") as f:
            f.write(f"# {os.path.basename(os.getcwd())}\n\n")
            f.write(f"Generated using Plotonix\n")

    # Fill LICENSE with selected license
    config_data = load_json(CONFIG_PATH)
    license_type = config_data.get("default_license", "MIT")
    with open("LICENSE", "a") as f:
        f.write(f"{license_type} License\n")

    print(f"Repository initialized using {template_key} template.")

def main():
    init_user_data()

    # parse command line
    args = sys.argv[1:]
    template = "classic"
    if args:
        if args[0] in ["-img", "--images"]:
            template = "images"
        elif args[0] in ["-py", "--python"]:
            template = "python"
        elif args[0] in ["-tool"]:
            template = "tool"

    create_repo(template)

if __name__ == "__main__":
    main()
