#!/bin/bash
set -e

# Mevcut klasör
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Global kurulum klasörü
INSTALL_DIR="/usr/local/share/plotonix"
LAUNCHER="/usr/local/bin/plotonix"

if [[ "$1" == "-u" ]] || [[ "$1" == "--uninstall" ]]; then
    echo "Uninstalling Plotonix..."

    # Launcher'ı sil
    if [[ -f "$LAUNCHER" ]]; then
        sudo rm "$LAUNCHER"
        echo "Removed: $LAUNCHER"
    else
        echo "Launcher not found, skipping."
    fi

    # Global klasörü sil
    if [[ -d "$INSTALL_DIR" ]]; then
        sudo rm -rf "$INSTALL_DIR"
        echo "Removed: $INSTALL_DIR"
    else
        echo "Install dir not found, skipping."
    fi

    echo "Plotonix completely removed from system."
    exit 0
fi

echo "Installing Plotonix..."

# Önce eski klasörü sil
sudo rm -rf "$INSTALL_DIR"
sudo mkdir -p "$INSTALL_DIR"

# Tüm projeyi (py + templates + diğer dosyalar) kopyala
sudo cp -r "$DIR/"* "$INSTALL_DIR/"
sudo chmod -R 755 "$INSTALL_DIR"

# Launcher script
echo "#!/bin/bash
python3 \"$INSTALL_DIR/plotonix.py\" \"\$@\"" | sudo tee "$LAUNCHER" > /dev/null

sudo chmod +x "$LAUNCHER"

echo "Plotonix installed successfully!"
echo "You can run it from anywhere using: plotonix"
