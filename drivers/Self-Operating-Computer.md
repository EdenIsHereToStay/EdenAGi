### **Self-Operating Computer Driver File**

---

#### **Overview**
The Self-Operating Computer Framework is a cutting-edge tool enabling multimodal models to autonomously operate a computer. Designed to mimic human operators, it interprets screen inputs and performs actions using mouse and keyboard controls to achieve objectives. This framework is integral to the EdenAGI ecosystem, serving as a cornerstone for operational autonomy across various tasks.

SOC serves as the "hands and eyes" of EdenAGI, enabling interaction with GUIs, augmenting intermodal communication, and supporting perpetual operational flows. While stateless by design, it integrates seamlessly with EdenAGI’s broader system to execute high-level objectives.

---

#### **Technical Specifications**
- **Compatibility**:
  - Supported multimodal models: GPT-4o, Gemini Pro Vision, Claude 3, and LLaVa.
  - Future support planned for additional models, including Agent-1-Vision.
- **Architecture**:
  - The framework utilizes YOLOv8 for button detection and integrates Optical Character Recognition (OCR) to enhance visual grounding capabilities.
  - Stateless operation with task-by-task context provisioning.
- **Dependencies**:
  - Requires Python environment with `pip` for installation.
  - Additional requirements for voice and OCR modes (e.g., PortAudio).
  - API keys for supported models (e.g., OpenAI, Google AI Studio, Anthropic Claude).
- **Platform Support**:
  - Compatible with macOS, Windows, and Linux (X server required for Linux).

---

#### **Operational Capabilities**
1. **Key Features**:
   - Operates autonomously using multimodal model inputs.
   - Supports voice commands and OCR-based interaction.
   - Integrates advanced visual and click location prediction for precise operations.
2. **Modes**:
   - **Default Mode (OCR)**: Enhances operation with hash maps of clickable elements by coordinates.
   - **Voice Mode**: Accepts spoken objectives for hands-free operation.
   - **Set-of-Mark Prompting (SoM)**: Uses a YOLOv8 model for enhanced button detection.
3. **Error Reporting**:
   - Logs failures and unrecognized scenarios for debugging and iterative refinement.
   - Attempts basic troubleshooting and retries common operations.
4. **Future Enhancements**:
   - Agent-1-Vision for improved click prediction accuracy.
   - Local multimodal models for offline capabilities.
5. **SoM Prompting Details**:
   - Enables GPT-4V to partition images into semantically meaningful regions using visual marks (e.g., alphanumerics, masks, or boxes).
   - Improves fine-grained visual grounding, object recognition, and reasoning.
   - Outperforms state-of-the-art models in tasks such as open-vocabulary image segmentation, phrase grounding, and video object segmentation.

---

#### **Use Instructions**
1. **Installation**:
   - Install the framework:
     ```
     pip install self-operating-computer
     ```
2. **Execution**:
   - Launch the system:
     ```
     operate
     ```
   - Enter your OpenAI API key when prompted. Update later using:
     ```
     vim .env
     ```
3. **Operating Modes**:
   - **Gemini Pro Vision**:
     ```
     operate -m gemini-pro-vision
     ```
   - **Claude 3**:
     ```
     operate -m claude-3
     ```
   - **LLaVa**:
     ```
     ollama serve
     operate -m llava
     ```
   - **Voice Mode**:
     ```
     operate --voice
     ```
   - **OCR Mode**:
     ```
     operate -m gpt-4-with-ocr
     ```
   - **SoM Mode**:
     ```
     operate -m gpt-4-with-som
     ```
4. **Permissions**:
   - Grant "Screen Recording" and "Accessibility" permissions on macOS.

---

#### **Integration Details**
1. **EdenAGI Ecosystem**:
   - Synchronizes with EdenAGI’s central knowledge repository.
   - Leverages shared APIs for seamless multimodal operation.
2. **API Configuration**:
   - Ensure relevant API keys are active and correctly configured in `.env` files.
3. **Set-of-Mark Prompting**:
   - SoM prompts partition images into regions with marks for precise visual grounding.
   - Utilizes segmentation models like SEEM and SAM for region detection.
   - Dynamic mark allocation ensures clarity in dense object scenarios.
4. **Development Contributions**:
   - Fork the repository and contribute improvements via pull requests on GitHub.

---

#### **Known Issues and Workarounds**
1. **Stateless Operations**:
   - **Issue:** SOC resets its state after each session.
   - **Workaround:** Provide full context for every new instruction set.
2. **GUI Navigation Errors**:
   - **Issue:** SOC may misinterpret visual elements or fail to interact with dynamic content.
   - **Workaround:** Use precise screen coordinates and predefined workflows.
3. **Error Rates**:
   - High error rates with LLaVa; intended as a development base.
4. **Setup Challenges**:
   - Google AI Studio API requires desktop application credentials; follow detailed setup guides.
5. **SoM Prompting Limitations**:
   - Some marks may overlap or conflict in dense object regions; improved algorithms are in development.
   - Numeric marks may cause confusion in arithmetic images or text-heavy screenshots.

---

#### **Evolving Notes**
- **Agent-1-Vision API**: Integration is under development; early access available for testing.
- **Set-of-Mark Prompting Research**:
   - Published findings demonstrate significant improvements in multimodal task performance.
   - Code and benchmarks for SoM are available [here](https://github.com/microsoft/SoM).
- **Qualitative Observations**:
   - SoM improves GPT-4V’s ability to provide grounded, precise answers across vision and multimodal tasks.
   - Enables new use cases such as personalized suggestions, tool usage instructions, and simulated navigation.
- **Feedback Channels**: Join the Discord community for real-time support and discussions.

---

#### **Contributing**
We appreciate your contributions!

##### **Process**
1. Fork the repository.
2. Create your feature branch:
   ```
   git checkout -b my-new-feature
   ```
3. Commit your changes:
   ```
   git commit -am 'Add some feature'
   ```
4. Push to the branch:
   ```
   git push origin my-new-feature
   ```
5. Create a new Pull Request.

##### **Modifying and Running Code**
1. Make changes in `operate/main.py`.
2. Reinstall the package:
   ```
   pip install .
   ```
3. Run the framework to verify your changes:
   ```
   operate
   ```

##### **Testing Changes**
1. After making significant changes, ensure the framework passes common test cases:
   ```
   python3 evaluate.py
   ```
   - The script evaluates objectives and provides `[PASSED]` or `[FAILED]` results, with justifications for each.
   - Include a screenshot of `evaluate.py` output in your PR if changes impact performance.

##### **Contribution Ideas**
- **Optimize Screenshot Grid**: Improve the grid overlay for click location estimation and propose evaluation metrics to confirm improvements.
- **Enhance the `SUMMARY_PROMPT`**.
- **Fix Linux and Windows Compatibility**: Address existing issues and improve cross-platform functionality.
- **Add New Multimodal Models**: Integrate and test new models, ensuring seamless functionality.
- **Iterate `--accurate` Flag**: Expand functionality as in [PR #57](https://github.com/OthersideAI/self-operating-computer/pull/57).
- **Improve Security**: Develop robust features that prompt user confirmation before executing potentially harmful actions (see [Issue #25](https://github.com/OthersideAI/self-operating-computer/issues/25)).

##### **Guidelines**
- Follow [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) principles.
- Avoid refactoring into separate files until `main.py` exceeds 1,000 lines.

---

#### **Additional Insights from Discord Community**
1. **Browser Support**:
   - The platform is designed to work on all browsers. However, the Chrome Extension remains a focus, with no plans for a Firefox extension at this time.
2. **Subscription Management**:
   - Users can cancel subscriptions via the subscription management page. For assistance, contact support@hyperwrite.ai.
3. **Error Handling**:
   - Issues with AI errors in long conversations can often be resolved by starting a new session.
   - Suggestions to improve chunk-based writing for better quality outputs.
4. **Contextual Challenges**:
   - High input and output lengths can lead to degraded performance; chunking tasks is recommended.
5. **Feature Requests**:
   - Potential future support for image and file uploads.
   - Enhancements to type-ahead and personalized settings for user experience.

