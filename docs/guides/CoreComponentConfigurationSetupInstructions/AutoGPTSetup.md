# AutoGPT Setup Guide

## Overview of AutoGPT
AutoGPT is an experimental, open-source AI agent leveraging OpenAI's GPT-4 or GPT-3.5 APIs to autonomously perform tasks. It is a pioneering example of applications using GPT-4 technology. See: [ https://www.projecteden.online/infrastructure/autogpt ]

### Features:
- **Autonomous Operation**: AutoGPT independently generates prompts and executes tasks, differing from Agent GPT which relies on user inputs.
- **Task Breakdown**: Given a goal in natural language, AutoGPT divides it into sub-tasks, utilizing the internet and various tools for completion.
- **Enhanced Capabilities**: It extends beyond traditional chatbot functionalities, capable of web access, running searches, file creation, and utilizing plugins.

### Project Eden Utilization:
- In Project Eden, AutoGPT acts as an extension of the localized system for complex tasks.
- Features 'Autogpt Stacking' for performance optimization, enabling AutoGPT systems to edit, communicate, and distribute tasks across AutoGPT clusters.

## AutoGPT Comprehensive User Guide

### Key Benefits:
- **Versatility**: Thanks to its plugin system, AutoGPT can handle diverse tasks.
- **Efficiency**: Automates tasks, thereby boosting productivity.
- **Flexibility**: Compatible plugins allow for a seamless workflow.

### Plugins Overview:
- Text Generation, Summarization, and Translation Plugins are among the notable additions enhancing the AutoGPT's capabilities.

### Setting Up AutoGPT:
1. Download AutoGPT from the [official GitHub repository](https://github.com/link-to-auto-gpt-repository).
2. Launch the application and create a new project via File > New > Project.

### Configuration:
- Access configuration options under Tools > Options.
- Set preferences like default language and text generation parameters.

### Testing and Deployment:
- Test the setup via Run > Test Run and deploy using Build > Deploy.

### Working with Plugins:
- Plugins have dedicated root folders within projects.
- Add a plugin via Project > Add Existing Plugin, then navigate to its root folder.

### Best Practices and Troubleshooting:
- Keep plugins updated.
- Refer to [AutoGPT's GitHub page](https://github.com/link-to-auto-gpt-repository) for troubleshooting.

### AutoGPT Installation and Usage:
- Install plugins using the curl command (Linux/MacOS) or PowerShell (Windows).
- Configure `ALLOWLISTED_PLUGINS` in `.env` for specific plugin usage.

## Integration with Leon.ai:
- Install AutoGPT in a folder named 'Auto-GPT' within Leon's working directory.
- Use Visual Studio Plus for direct file access and operations.

### Command-Line Interaction:
- Access various functionalities like Speak Mode, Continuous Mode, and Self-Feedback Mode through specific command-line arguments.
- Refer to the AutoGPT guide for details on each mode and their usage.

## AutoGPT Configuration for Eden Project:
- The Primary AutoGPT acts as a controller for the Secondary AutoGPT, handling tasks, interpreting outputs, and ensuring communication.
- The Secondary AutoGPT focuses on executing tasks based on the Primary's instructions.

### Important Note on Installation:
- Do not install the primary/parent AutoGPT inside the existing AutoGPT folder.
- It is recommended to replace the existing AutoGPT folder with the one obtained from the repository installation.

