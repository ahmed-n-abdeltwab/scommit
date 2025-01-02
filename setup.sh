#!/bin/bash

# Create bin directory in home if it doesn't exist
mkdir -p ~/bin

# Create the scommit script
cat > ~/bin/scommit << 'EOF'
#!/bin/bash
python3 "$(pwd)/src/main.py" "$(pwd)" "$@"
EOF

# Make the script executable
chmod +x ~/bin/scommit

# Add ~/bin to PATH if not already there
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
fi

echo "scommit command has been installed. Please restart your terminal or run 'source ~/.bashrc' (or 'source ~/.zshrc' if using zsh) to use it."
