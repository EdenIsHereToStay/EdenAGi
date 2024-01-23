# Installation Guide for Project EdenAGI

## Introduction
This guide provides step-by-step instructions for setting up Project EdenAGI on your system. The repository is set up with placeholder folders and files to demonstrate the file structure. This guide will also explain the organizational structure, file layout, and the reasoning behind it to help users understand the infrastructure and setup.

## Initial Repository Setup
- Clone the EdenAGI repository: `git clone https://github.com/EdenIsHereToStay/EdenAGi.git`
- Navigate to the cloned directory: `cd EdenAGi`

# File System Overview

## File Structure Explanation

The file structure of Project EdenAGI is designed to provide clarity, ease of use, and a logical organization of all components involved in the project. This structure is pivotal for understanding how different parts of the system interact, as well as for guiding users and developers in navigating and contributing to the project effectively.

### Key Components of the File Structure:

- **`/docs`**: This directory is the heart of documentation for Project EdenAGI. It includes detailed system design documents, update specifications for components like AutoGPT, introductory guides, and comprehensive analysis of each system component. This section is essential for anyone looking to understand the project in-depth or contribute to its development.

- **`/src`**: The source directory contains the core code and AI models that drive Project EdenAGI. Each sub-directory within `src` is dedicated to a specific component of the system, such as LeonAI, AutoGPT, and PrivateGPT. This organization ensures a modular and maintainable codebase.

- **`/tests`**: Housing test cases and scenarios, this directory is crucial for ensuring the reliability and stability of Project EdenAGI. It includes tests for each major component, providing a way to validate changes and updates systematically.

- **`/plugins`**: This directory is reserved for plugins or extensions that enhance the functionality of Project EdenAGI. It embodies the project's commitment to extensibility and customization.

### Organizational Philosophy:

- **Modularity**: Each component of Project EdenAGI is contained within its own sub-directory, promoting a modular approach. This facilitates easier updates, maintenance, and scalability of the system.

- **Clarity and Accessibility**: The clear naming conventions and logical grouping of files and directories are designed to make the system user-friendly and navigable, aiding both new users and seasoned contributors.

- **Comprehensive Documentation**: The extensive documentation provided in the `/docs` directory serves as a guide and reference, ensuring users and developers have a deep understanding of the system's functionality and architecture.

- **Testing and Reliability**: The emphasis on testing, reflected in the `/tests` directory, underscores the project's commitment to quality and reliability, an essential aspect of any sophisticated AI system.

By understanding this file structure, users and contributors can effectively navigate, utilize, and enhance Project EdenAGI, ensuring its ongoing development and success.


Project_Eden/
├── dev/                                           # Development environment.
│
├── docs/                                          # Project documentation.
│   ├── guides/                                    # Instructional guides.
│   ├── knowledgeBases/                            # Knowledge Bases for various components.
│   │   ├── agentSpecificKnowledgeBase/            # Knowledge Base specific to each AI agent.
│   │   ├── memoryFiles/                           # Storage of system restore files and summaries.
│   │   ├── projectInsights/                       # Insights and findings related to the project.
│   │   ├── promptTemplateLibrary/                 # Collection of prompt templates for system engineering.
│   │   ├── researchPapers/                        # Repository of research papers.
│   │   ├── systemWideKnowledgeBase/               # General Knowledge Base for the entire system.
│   │   │   └── AgentSOPs/                         # Standard Operating Procedures for AI Agents.
│   │   └── technicalReferences/                   # Technical references and documentation.
│   ├── SystemInstructions/                        # Instructions for system setup and usage.
│   │   ├── CoreComponentConfigurationSetupInstructions/ # Setup instructions for core components.
│   │   └── CoreComponentConfigurationUsageInstructions/ # Usage instructions for core components.
│   ├── technicalDocs/                             # Technical documentation for advanced users.
│   └── userManuals/                               # User manuals for general audience.
│
├── plugins/                                       # Plugins for extending functionality.
│   ├── dataManagement/                            # Plugins for data management.
│   └── textProcessing/                            # Plugins for text processing.
│
├── src/                                           # Source code for the entire project.
│   ├── aiModels/                                  # All AI models (LLM, LAM, etc.).
│   │   ├── AutoGPT/                               # AutoGPT components.
│   │   ├── leonAi/                                # Leon.AI components.
│   │   ├── LocalLAM-Storage/                      # Storage for Large Associative Memories (LAM).
│   │   ├── LocalLLM-Storage/                      # Storage for Large Language Models (LLM).
│   │   ├── privateGPT/                            # PrivateGPT for secure document processing.
│   │   └── selfOperatingComputer/                 # Self-Operating Computer components.
│   └── codeGeneration/                            # Code generation components (EngineerGPT).
│
├── staging/                                       # Staging environment for pre-production testing.
│
├── tests/                                         # Test cases for the project.
│   ├── autoGPTTests/                              # Tests for AutoGPT components.
│   ├── leonAITests/                               # Tests for Leon.AI components.
│   ├── privateGPTTests/                           # Tests for PrivateGPT.
│   └── selfOperatingComputerTests/                # Tests for Self-Operating Computer.
│
├── .gitignore                                     # Specifies intentionally untracked files to ignore.
└── README.md                                      # Overview and general information about the project.


## Setting Up Core Systems
- Navigate to `/src`.
- Install dependencies: `./install_dependencies.sh` (Linux/Mac) or `install_dependencies.bat` (Windows).

### AutoGPT Setup
- Configure AutoGPT as a REPLACEMENT for the `/src/AutoGPT` directory.
- Detailed instructions can be found in the [AutoGPT Comprehensive User Guide](EdenAGi\docs\SetupInstructions\CoreComponentConfigurationSetupInstructions\AutoGPTSetup.md).

### EngineerGPT Integration
- Install and configure as a REPLACEMENT for the `/src/EngineerGPT` directory.
- Integration guide with EngineerGPT available [here](EdenAGi\docs\SetupInstructions\CoreComponentConfigurationSetupInstructions\EngineerGPTSetup.md).

### PrivateGPT Configuration
- Set up adn configure as a REPLACEMENT for the `/src/PrivateGPT` directory.
- Follow the [PrivateGPT User Guide](EdenAGi\docs\SetupInstructions\CoreComponentConfigurationSetupInstructions\PrivateGPTSetup.md) for detailed instructions.

### Leon AI Integration
- Set up as a REPLACEMENT for the `/src/LeonAI` directory.
- Configure as per the [Leon AI Documentation](EdenAGi\docs\SetupInstructions\CoreComponentConfigurationSetupInstructions\LeonAiSetup.md).

## Integrating Language Models
- Refer to the [Comprehensive Guide to Large Language Models](https://link-to-language-models-guide) for integration details of models like BERT, GPT, T5, etc.
- LocalLLM stored: [ EdenAGi\src\aiModels\LocalLLM-Storage ]

## Falcon 180B Integration
- Technical integration steps for Falcon 180B are detailed in the [Falcon 180B Technical Deep Dive]( https://www.projecteden.online/infrastructure/falcon-180b-integration ).
- LocalLLM stored: [ EdenAGi\src\aiModels\LocalLLM-Storage ]

## Setting Up the Self-Operating-Computer Framework
- Set up as a REPLACEMENT for the `/src/SelfOperatingComputer` directory.
- Follow the setup instructions as REPLACMENT fo the [Self-Operating Computer Framework Guide](EdenAGi\docs\SystemInstructions\CoreComponentConfigurationSetupInstructions\SelfOperatingComputerSetup.md).

## Final Configuration
- Ensure all systems in `/src` are correctly set up and configured.
- Test each component individually and then the entire system.

## Troubleshooting and Support
- For issues, refer to the individual guides or visit [Project EdenAGI Support](https://www.projecteden.online/support).

## Additional Resources
- Visit [Project EdenAGI](https://www.projecteden.online/) for more information and updates.

---

_This guide is a part of the Project EdenAGI documentation. For more details and updates, please refer to the official [Project EdenAGI Repository](https://github.com/EdenIsHereToStay/EdenAGi)._ 
