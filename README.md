# Project EdenAGI: Comprehensive Guide to Autonomous General Intelligence System

Welcome to the repository of Project EdenAGI, an ambitious and groundbreaking open-source initiative aimed at creating a fully autonomous, self-evolving Artificial General Intelligence (AGI) system. Project EdenAGI epitomizes the fusion of human ingenuity and AI autonomy, crafted to operate on advanced hardware systems independently of external control. Also see: www.ProjectEden.Online

Project_Eden/
│
├── docs/                                        # Project documentation.
│   ├── SystemDesign.md                          # Detailed system design documentation.
│   ├── AutoGPT_Update_Specifications.md         # AutoGPT enhancement specifics.
│   ├── Introduction.md                          # Introduction to Project Eden.
│   ├── SystemOverview.md                        # Overview of the entire system.
│   ├── DetailedComponentsAnalysis.md            # In-depth analysis of each component.
│   ├── EngineeringRoundsExplained.md            # Explanation of the engineering rounds.
│   ├── InstallationGuide.md                     # Step-by-step installation instructions.
│   ├── UsageProtocols.md                        # Guide on how to use the system.
│   ├── Contributing.md                          # Guidelines for contributing to EdenAGI.
│   ├── SupportAndContact.md                     # Information for support and contact.
│   ├── knowledgeBases/                          # Knowledge Bases for LLM, LAM, etc.
│   │   ├── localizedKnowledgeBase/              # Localized Knowledge Bases.
│   │   ├── memoryFiles/                         # Storage of system restore files and engineering round summaries.
│   │   ├── promptTemplateLibrary/               # Storage of prompt templates to be used for system engineering.
│   │   └── systemWideKnowledgeBase/             # System-wide Knowledge Bases.
│   └── ...                                      # Other documentation files.
│
├── aiTools/                                     # Source code for the entire project.
│   ├── leonAI/                                  # Central Hub: Leon.AI (Parent Component)
│   │   ├── ui/                                  # User Interface components.
│   │   ├── taskManager/                         # Task management logic.
│   │   └── feedbackMechanism/                   # Feedback mechanism implementation.
│   │
│   ├── autoGPT/                                 # AutoGPT (Parent and Child Components)
│   │   ├── parentAutoGPT/                       # Parent AutoGPT (AI Dispatcher)
│   │   │   ├── inputParser/                     # Input parsing components.
│   │   │   ├── childAutoGPT/                    # Child AutoGPTs (Worker Allocators)
│   │   │       └── ...                          # Other components.
│   │   └── ...                                  # Other AutoGPT related components.
│   │
│   ├── privateGPT/                              # PrivateGPT for secure document processing.
│   │   ├── documentReader/                      # Document reading components.
│   │   ├── dataProcessor/                       # Data processing logic.
│   │   └── securityLayer/                       # Security layers for data.
│   │
│   ├── selfOperatingComputer/                   # SelfOperatingComputer components.
│   │   ├── operationManager/                    # Operation management logic.
│   │   └── ...                                  # Other components.
│   │
│   ├── codeGeneration/                          # Code Generation (EngineerGPT)
│   │   ├── codeGenerator/                       # Code generation logic.
│   │   ├── codeAuditor/                         # Code auditing components.
│   │   └── deploymentManager/                   # Code deployment mechanisms.
│   │
│   │
│   └── aiModels/                                # All AI models (LLM, LAM, etc.).
│       ├── llm/                                 # Large Language Models.
│       ├── lam/                                 # Large Associative Memories.
│       └── ...                                  # Other AI models.
│
├── tests/                                       # Test cases for the project.
│   ├── leonAITests/                             # Tests for Leon.AI components.
│   ├── autoGPTTests/                            # Tests for AutoGPT components.
│   ├── privateGPTTests/                         # Tests for PrivateGPT.
│   ├── selfOperatingComputerTests/              # Tests for SelfOperatingComputer.
│   └── ...                                      # Other test suites.
│
├── plugins/                                     # Plugins for extending functionality.
│   └── ...                                      # Plugin files and directories.
│
├── .gitignore                                   # Specifies intentionally untracked files to ignore.
└── README.md                                    # Overview and general information about the project.


## Introduction
Project EdenAGI is a revolutionary blueprint for an AI system that transcends traditional limitations. It's a personal, private, and sovereign AI, built to empower users while ensuring data integrity and ethical AI use.

## System Overview
EdenAGI is a modular, multi-component AI ecosystem. Its architecture is designed to be self-sustaining, capable of autonomously performing complex tasks, and making decisions based on available resources and predefined directives.

### Detailed Components Analysis
- **AutoGPT**: The core intelligence of EdenAGI, responsible for generating autonomous prompts and overseeing task execution within the system.
- **Leon.AI**: The central hub and interface for user interaction, managing task distribution across the AI network.
- **First-Level AutoGPT**: Acts as an AI dispatcher, intelligently delegating tasks to the appropriate second-tier AutoGPT agents.
- **Second-Tier AutoGPTs**: Specialized AI workers dedicated to processing tasks and reporting outcomes.
- **EngineerGPT**: Integrated within Leon.AI, this component is responsible for dynamic, real-time code generation and system updates.
- **PrivateGPT**: Focused on secure document processing, ensuring data privacy and security within the system.
- **Communication Protocol**: A robust JSON file system integration is employed for efficient and coherent inter-component communication.

### Engineering Rounds Explained
Engineering Rounds are the operational heart of EdenAGI, where AI agents communicate via meticulously crafted prompt templates. This iterative process involves initiation, data handling, synthesis by EdenAGI's core, and concludes with a system memory checkpoint, ensuring continuous learning and system evolution.

## Installation Guide
For installation, please refer to [INSTALLATION.md](/docs/INSTALLATION.md). This document provides step-by-step instructions on setting up EdenAGI, configuring the environment, and ensuring successful deployment.

## Usage Protocols
Utilizing EdenAGI involves interacting with its various components and engaging in the Engineering Rounds. Detailed usage instructions are available in [USAGE.md](/docs/USAGE.md), offering guidelines for operating within the EdenAGI ecosystem.

## Contributing to EdenAGI
We invite developers, AI enthusiasts, and forward-thinkers to contribute to the evolution of EdenAGI. For guidelines on contributing, please consult [CONTRIBUTING.md](/docs/CONTRIBUTING.md).

## License Information
EdenAGI is licensed under the MIT License, promoting open and flexible use of the software. See [LICENSE.md](/docs/LICENSE.md) for more details.

## Support and Contact
For support or further inquiries, visit [www.eddieboscan.com](http://www.eddieboscan.com) or reach out to the EdenAGI community for collaborative assistance and guidance.

