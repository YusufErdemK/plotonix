#!/usr/bin/env python3
import os
import sys
from flask import json

TEMPLATES_DIR = "/usr/local/share/plotonix/templates"
BASE_DIR = "/usr/local/share/plotonix"
GITHUBCRED_PATH = os.path.join(BASE_DIR, "json", "github.json")

TEMPLATE_MAP = {
    "classic": "classic-repo.py",
    "images": "images.py",
    "python": "python.py",
    "tool": "tool-repo.py"
}

def registerGitHub():
    username = input("Enter your GitHub username: ")
    token = input("Enter your GitHub personal access token: ")
    
    with open(GITHUBCRED_PATH, "w") as f:
        json.dump({"username": username, "token": token}, f)
    
    print("GitHub credentials registered successfully.")
    print(f"Username: {username}")
    

def create_repo(template_key="classic"):
    template_file = TEMPLATE_MAP.get(template_key, "classic-repo.py")
    template_path = os.path.join(TEMPLATES_DIR, template_file)

    if not os.path.exists(template_path):
        print("Template '{}' not found in {}".format(template_file, TEMPLATES_DIR))
        return

    target_dir = os.getcwd()
    namespace = {}
    with open(template_path, "r") as f:
        exec(f.read(), namespace)

    # file/folder creator
    if "create_structure" in namespace:
        namespace["create_structure"](target_dir)
        print(f"Repository created using '{template_key}' template.")
    else:
        print(f"Template '{template_file}' does not define create_structure().")
        
    # github repo creator
    if "create_github_repo" in namespace:
        namespace["create_github_repo"]()
        print("GitHub repository created in your account successfully.")
    else:
        print(f"Template '{template_file}' does not define create_github_repo().")

def main():
    try:
        with open(GITHUBCRED_PATH, "r") as neckhurt:
            content = neckhurt.read()
            if content:
                pass
            else:
                registerGitHub()
    except FileNotFoundError:
        print(f"Error: {GITHUBCRED_PATH} not found.")
    
    # repo name
    repoName = input("Enter the name of your new repository: ")
    if repoName:
        print(f"Creating repository '{repoName}'...")
    else:
        print("Repository name cannot be empty.")
    
    # repo templates
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
