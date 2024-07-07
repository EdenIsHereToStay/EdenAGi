## Self-Operating Computer Framework Overview Document

### Introduction
The Self-Operating Computer Framework is an innovative open-source project that leverages multimodal models to autonomously control a computer. By using advanced AI models such as GPT-4 Vision, Gemini Pro Vision, Claude 3, and LLaVa, the framework can interpret visual inputs and perform actions like a human operator, enhancing productivity and enabling complex automation tasks.

### Key Features
- **Compatibility**: Supports various multimodal models, including GPT-4 Vision, Gemini Pro Vision, Claude 3, and LLaVa.
- **Integration**: Seamlessly integrates with multiple AI models for diverse applications.
- **Future Plans**: Ongoing development aims to support additional models and improve accuracy.

### Technical Specifications
#### Requirements
- **Operating Systems**: Compatible with macOS, Windows, and Linux (with X server installed).
- **Python**: Python 3 is required.
- **Dependencies**: Various Python libraries and API keys from OpenAI and other providers.

#### Installation and Setup
1. **Clone the Repository**: 
   ```sh
   git clone https://github.com/OthersideAI/self-operating-computer.git
   cd self-operating-computer
   ```

2. **Set Up Python Environment**:
   ```sh
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Rename `example.env` to `.env`:
     ```sh
     mv example.env .env
     ```
   - Add your API keys to the `.env` file.

4. **Run the Framework**:
   ```sh
   operate
   ```

### Usage Modes
- **Default Mode**: Operates using GPT-4 with OCR.
  ```sh
  operate
  ```
- **Gemini Pro Vision Mode**:
  ```sh
  operate -m gemini-pro-vision
  ```
- **Claude 3 Mode**:
  ```sh
  operate -m claude-3
  ```
- **LLaVa Mode**:
  ```sh
  operate -m llava
  ```
- **Voice Mode**:
  ```sh
  operate --voice
  ```

### How It Works
The framework captures screenshots of your desktop and sends them to the multimodal models, which then interpret the visual data and decide on actions to perform. These actions can include mouse movements, keyboard inputs, and other interactions to achieve the specified objectives.

### Example Usage
1. **Lookup Information**:
   - Prompt: "Look up the most recent Langchain release on Google."
   - The framework will open the browser, navigate to Google, and search for the specified term autonomously.

2. **Voice Commands**:
   - Enable voice mode to give spoken commands.
   - Example: "Open Visual Studio Code and create a new Python file."

### Contribution and Feedback
- Contributions are welcomed. See [CONTRIBUTING.md](https://github.com/OthersideAI/self-operating-computer/blob/main/CONTRIBUTING.md) for guidelines.
- For feedback and discussions, join the [Discord server](https://discord.gg/self-operating-computer).

### Future Development
- **Agent-1-Vision**: HyperwriteAI is developing a multimodal model with improved click location accuracy.
- **API Access**: Soon, API access to Agent-1-Vision will be available.

### Documentation and Resources
- **GitHub Repository**: [Self-Operating Computer Framework](https://github.com/OthersideAI/self-operating-computer)
- **Video Tutorial**: [Self-Operating Computer Framework in 4 Minutes](https://www.youtube.com/watch?v=nQor7Weu4LQ)

### Conclusion
The Self-Operating Computer Framework represents a significant step forward in AI automation, enabling computers to be controlled through sophisticated multimodal models. As the project evolves, it promises to become even more powerful and versatile, opening up new possibilities for automation and productivity.

### References
1. [GitHub Repository](https://github.com/OthersideAI/self-operating-computer)
2. [Self-Operating Computer Framework in 4 Minutes](https://www.youtube.com/watch?v=nQor7Weu4LQ)
