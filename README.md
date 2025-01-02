# Smart Commit Message Generator

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


An AI-powered tool that automatically generates meaningful commit messages from your staged git changes using GPT-2.


## Features

- 🤖 Automatically analyzes staged git changes
- ✨ Generates concise and descriptive commit messages
- 📏 Configurable message length
- 🖥️ Easy to use command-line interface
- 🧠 Uses GPT-2 for intelligent message generation

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd smart-commit-generator
```

2. Create and activate virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Unix/macOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development
```

4. Install the `scommit` command:
```bash
chmod +x setup.sh
./setup.sh
```

## Usage

Simply stage your changes with git and run:

```bash
scommit
```

Options:
- `--max_length`: Maximum length for the generated commit message (default: 50)
- `--dry-run`: Preview the generated message without committing

## Useful Tips

🧪 **Dry Run**: 
- Add `--dry-run` flag to preview the generated message without committing
- Useful for testing and adjusting message generation settings
- Example: `scommit --dry-run`

🤖 **Custom Models**: 
- Configure different models in `src/ai/model_config.py`
- Supports any Hugging Face text generation model
- Adjust model parameters for different output styles

## ⚠️ Limitations

- Requires Python 3.8+
- Only works with git repositories
- May generate generic messages for complex changes
- Limited to staged changes only
- CPU-only by default (GPU support requires additional setup)
- English language only

## 🔮 Future Improvements

- [ ] GPU acceleration support
- [ ] Multiple language support
- [ ] Custom prompt templates
- [ ] Integration with popular Git GUIs
- [ ] Support for commit message conventions (conventional commits)
- [ ] Pre-commit hook integration
- [ ] Branch-specific message styles
- [ ] Message quality scoring

## Development

### Running Tests

```bash
pytest tests/ -v
```

### Project Structure

```
├── src/
│   ├── ai/                    # AI-related modules
│   │   ├── message_generator.py
│   │   ├── model_config.py
│   │   └── text_cleaner.py
│   ├── cli/                   # CLI-related modules
│   │   └── argument_parser.py
│   ├── git/                   # Git operations
│   │   └── git_operations.py
│   └── main.py               # Main entry point
├── tests/                     # Test suite
├── requirements.txt           # Production dependencies
├── requirements-dev.txt       # Development dependencies
└── setup.sh                  # Installation script
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch
3. Write tests for your changes
4. Ensure all tests pass
5. Submit a pull request
