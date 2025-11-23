# Plotonix

Plotonix is a command-line tool designed to quickly initialize GitHub repositories
with standard files and folder structures. It supports multiple project types
such as classic repos, Python projects, image/media projects, and CLI/tool repos.

## Features

- Quickly generate standard GitHub repo files and folders
- Supports multiple templates:
    - Classic repo
    - Python projects
    - Image/media projects
    - Tool/CLI projects
- Automatically fills user information from JSON configuration
- Easy to extend with custom templates

## Installation

```bash
git clone https://github.com/YusufErdemK/plotonix.git
cd plotonix
chmod +x install.sh
./install.sh
```
## Unistalling
```bash
cd plotonix
./install.sh -u
```
## Usage
Navigate to your project folder and run:

```bash
mkdir my_project    #your repo name
cd my_project
plotonix           # Initialize a classic repository
plotonix -py       # Initialize a Python repository
plotonix -img      # Initialize an image/media repository
plotonix -tool     # Initialize a CLI/tool repository
```

Plotonix will prompt for any missing information when first run.

> Templates

- All templates are located in the templates/ folder:

    - classic-repo.py

    - python.py

    - images.py

    - tool-repo.py

These templates define the folder structure and starter files for each repo type.

# License
 MIT License

 > by erdamn
