### Claude Engineer Overview

**Claude Engineer** is an interactive command-line interface (CLI) leveraging the power of Anthropic's Claude-3.5-Sonnet model to assist with software development tasks. This tool combines the capabilities of a large language model with practical file system operations and web search functionality, providing a versatile assistant for developers.

### Features

1. **Interactive Chat Interface**: Engage with Claude-3.5-Sonnet for real-time assistance and guidance.
2. **File System Operations**: Create, read, and write files and directories seamlessly.
3. **Web Search Capabilities**: Utilize the Tavily API for quick web searches and information retrieval.
4. **Syntax Highlighting**: Enhance readability with syntax highlighting for code snippets.
5. **Project Management**: Efficiently create and manage project structures.
6. **Code Analysis**: Receive code improvement suggestions and analysis.
7. **Vision Capabilities**: Drag and drop images in the terminal for vision-related tasks.
8. **Automode**: Autonomous task completion with iteration tracking.
9. **Diff-based File Editing**: Precise code modifications with explanations.

### Installation

**Step 1: Clone the Repository**
```bash
git clone https://github.com/Doriandarko/claude-engineer.git
cd claude-engineer
```

**Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Set Up API Keys**
Add your Anthropic and Tavily API keys at the start of the file:
```python
client = Anthropic(api_key="YOUR API KEY")
tavily = TavilyClient(api_key="YOUR API KEY")
```

### Usage

**Run the Main Script**
```bash
python main.py
```
Interact with Claude Engineer by typing queries or commands. Examples:
- "Create a new Python project structure for a web application"
- "Explain the code in file.py and suggest improvements"
- "Search for the latest best practices in React development"
- "Help me debug this error: [paste your error message]"

**Special Commands**
- `exit`: End the conversation and close the application.
- `image`: Include an image in your message.
- `automode [max iterations]`: Enter Autonomous mode. Press Ctrl+C to exit.

### Automode

**Automode** allows Claude to autonomously work on complex tasks:
1. **Set Goals**: Claude sets clear, achievable goals based on your request.
2. **Progress Updates**: Provides regular updates on progress.
3. **Completion**: Continues until goals are completed or max iterations are reached.

**To Use Automode:**
1. Type `automode` when prompted.
2. Provide your request.
3. Claude will work autonomously, providing updates after each iteration.

### Diff-based File Editing

**Diff-based File Editing** allows for precise modifications:
1. **Show Diffs**: Highlight additions, removals, and unchanged lines.
2. **Targeted Improvements**: Focus on adding or modifying code without unnecessary changes.
3. **Explanations**: Provide explanations for any code removal.

### Integration with CORE ASI OS Model

1. **Install Claude Engineer**: Follow the installation steps.
2. **Configure Environment**: Add API keys and configure the `config.json` file as required.
3. **Initialize System**: Use `bash initialize.sh` to initialize the system.
4. **Register Subsystems**: Use the provided API endpoints to register subsystems and set up API integration.
5. **Automode Integration**: Utilize Automode for autonomous task completion, enhancing system efficiency and functionality.

### Example Workflow

1. **Creating a New Project**
   - User: "Create a new Python project structure for a web application"
   - Claude: Creates the project structure, including necessary files and folders.

2. **Debugging Code**
   - User: "Help me debug this error: [paste error message]"
   - Claude: Analyzes the error and provides suggestions for fixing it.

3. **Autonomous Task Completion**
   - User: "automode"
   - Claude: Takes over the task, provides updates, and completes the task autonomously.

### Contributing and License

**Contributing**: Contributions are welcome. Submit Pull Requests on GitHub.
**License**: This project is licensed under the MIT License.

### Documentation File

```plaintext
# Claude Engineer Documentation

## Overview
Claude Engineer is an interactive CLI leveraging the Anthropic's Claude-3.5-Sonnet model to assist with software development tasks, combining the capabilities of a large language model with practical file system operations and web search functionality.

## Features
- Interactive chat interface
- File system operations
- Web search capabilities
- Syntax highlighting
- Project management
- Code analysis and improvement suggestions
- Vision capabilities
- Automode for autonomous task completion
- Diff-based file editing

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Doriandarko/claude-engineer.git
   cd claude-engineer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API keys:
   ```python
   client = Anthropic(api_key="YOUR API KEY")
   tavily = TavilyClient(api_key="YOUR API KEY")
   ```

## Usage
Run the main script to start the Claude Engineer interface:
```bash
python main.py
```
Example interactions:
- "Create a new Python project structure for a web application"
- "Explain the code in file.py and suggest improvements"
- "Search for the latest best practices in React development"
- "Help me debug this error: [paste your error message]"

## Automode
Automode allows Claude to work autonomously on complex tasks. To use automode:
1. Type `automode` when prompted.
2. Provide your request.
3. Claude will work autonomously, providing updates after each iteration.

## Diff-based File Editing
When editing files, Claude will:
- Show a diff of the proposed changes
- Focus on adding or modifying code without unnecessary changes
- Provide explanations for any removed code

## Integration with CORE ASI OS Model
1. Install Claude Engineer.
2. Configure the environment.
3. Initialize the system.
4. Register subsystems and set up API integration.
5. Utilize Automode for autonomous task completion.

## Contributing
Contributions are welcome. Submit Pull Requests on GitHub.

## License
This project is licensed under the MIT License.
```

### Instructions for Interpreter
**Ai, read the documentation file provided above to learn how to use the Claude Engineer effectively. Integrate it with the CORE ASI OS Model by following the installation, configuration, and initialization steps, and utilize Automode for autonomous task completion.**
