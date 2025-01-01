# 🧑‍💻 Git Diff Commit Message Generator 📝

## 🌟 Project Overview
This 🛠️ is a 🐍 script 🧑‍💻 to simplify the 🛣️ of generating 🎯 Git commit messages. It 🏗️ a local text-generation 🤖 (GPT-2) to 🧐 staged changes in a Git 📁 and generate a short 📝. The 📝 can then be directly used to commit the changes.

### ❓ Why This Project?
Writing ✍️ meaningful and consistent commit 📝 is an essential practice in 🔧 🖥️. However, it can be 🕒-consuming and 🛑-prone. This 🛠️ automates the 🛣️, ensuring that commit 📝 are:

- **🔍 Descriptive**: Reflecting the staged changes.
- **🎯 Consistent**: Maintaining a uniform style.
- **⏱️ Efficient**: Saving developer 🕒.

The use of a local 🤖 ensures that no 🔒 code or data is sent to 🌐 services, making it suitable for projects with strict 🔐 requirements.

## 🔥 Features
- 🧐 staged Git changes (`git diff --staged`).
- Generates commit 📝 using a local GPT-2 🤖.
- 📜 commits changes with the generated 📝.
- ⚙️ customization of 📝 length using the `--max_length` parameter.

## 🧭 How to Use

### 📋 Prerequisites
Ensure the following are installed:
- 🐍 3.7+
- `transformers` and `torch` 🐍 libraries
- Git

### 🔧 Installation
1. 🌀 this repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd your-repo-url
   ```
2. Install the required 🐍 📦:
   ```bash
   pip install transformers torch
   ```

### 🚀 Usage
1. 📥 your changes in the target project:
   ```bash
   git add <file>
   ```
2. Run the 🛠️:
   ```bash
   python generate_commit_message.py /path/to/target/project --max_length 100
   ```
   Replace `/path/to/target/project` with the 📁 to your project and adjust `--max_length` as needed.

3. The 🛠️ will 🏗️ a commit 📝 and use it to commit the changes.

### 📝 Example
```bash
python scommit.py /my/project --max_length 80
```
Output:
```
Changes committed ✅.
Commit Output: [main abc1234] 🛠️ function for better error 🛡️.
```

## 💡 Useful Tips
- **🧪 Dry Run**: If you want to 🔍 the commit 📝 before committing, 🛠️ the script to 🖨️ the 📝 without executing `git commit`.
- **🤖 Custom Models**: You can replace GPT-2 with a fine-tuned 🤖 for 🏗️-specific commit 📝.

## ⚠️ Limitations
- Requires staged changes to 🏗️ a 📝.
- The ✨ of the 🏗️ 📝 depends on the 📊 of the GPT-2 🤖.

## 🔮 Future Improvements
- 🧑‍🤝‍🧑 for 🗂️ file changes in a single commit.
- 🛠️ to preview and 🖊️ the 🏗️ 📝 before committing.
- Integration with popular Git 🖼️ for seamless usage.

## 🙌 Contributing
Contributions are welcome! 🤝 Feel free to open an 🐞 or submit a 📤 request.

## ⚖️ License
This 🛠️ is 🏷️ under the MIT 📜. See the `LICENSE` 📄 for more details.

