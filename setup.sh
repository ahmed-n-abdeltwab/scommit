#!/bin/bash

# Create bin directory in home if it doesn't exist
mkdir -p ~/bin

# Create the scommit script
cat > ~/bin/scommit << 'EOF'
#!/bin/bash

# Get the current directory
CURRENT_DIR=$(pwd)

# Activate virtual environment
source "${CURRENT_DIR}/myenv/bin/activate"

# Run the script with the current directory as project path
python3 "${CURRENT_DIR}/src/main.py" "${CURRENT_DIR}" "$@"

# Deactivate virtual environment
deactivate
EOF

# Make the script executable
chmod +x ~/bin/scommit

# Add ~/bin to PATH if not already there
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
fi

echo "scommit command has been installed. Please restart your terminal or run 'source ~/.bashrc' (or 'source ~/.zshrc' if using zsh) to use it."
