#!/usr/bin/env python3
import os
import sys

TEMPLATES_DIR = "/usr/local/share/plotonix/templates"

# Template mapping
TEMPLATE_MAP = {
    "classic": "classic-repo.py",
    "images": "images.py",
    "python": "python.py",
    "tool": "tool-repo.py"
}

def create_repo(template_key="classic"):
    template_file = TEMPLATE_MAP.get(template_key, "classic-repo.py")
    template_path = os.path.join(TEMPLATES_DIR, template_file)

    if not os.path.exists(template_path):
        print("All roads lead to Rome! Template '{}' not found in {}".format(template_file, TEMPLATES_DIR))
        return

    target_dir = os.getcwd()
    namespace = {}
    with open(template_path, "r") as f:
        exec(f.read(), namespace)

    if "create_structure" in namespace:
        namespace["create_structure"](target_dir)
        print(f"Repository created using '{template_key}' template.")
    else:
        print(f"Template '{template_file}' does not define create_structure().")

def main():
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
