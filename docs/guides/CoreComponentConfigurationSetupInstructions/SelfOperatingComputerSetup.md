# Self-Operating Computer Setup Guide

## Overview
The Self-Operating Computer Framework by OthersideAI is designed to enable multimodal models to control a computer, replicating human inputs like mouse clicks and keyboard actions. It's compatible with various models, including integration with GPT-4v, and has future model support plans. The framework works with Mac OS, Windows, and Linux (with X server installed). See: https://www.projecteden.online/infrastructure/self-operating-computer

### Challenges and Developments
- Current high error rate in GPT-4V estimating XY mouse click locations.
- Development of the Agent-1-Vision model to improve click location predictions.
- Requirement of the gpt-4-vision-preview model and a minimum spend of $5 in API credits on your OpenAI account.

## Installation Process on Windows

### Step 1: Clone the Repository
- Open Command Prompt or PowerShell.
- Execute: `git clone https://github.com/OthersideAI/self-operating-computer.git`

### Step 2: Navigate to the Directory
- Change directory: `cd self-operating-computer`

### Step 3: Create and Activate Python Virtual Environment
- Ensure Python is installed.
- Create virtual environment: `python -m venv venv`
- Activate virtual environment: `.\venv\Scripts\activate`

### Step 4: Install Project Requirements
- Install requirements: `pip install -r requirements.txt`

### Step 5: Install the Project and CLI
- Execute: `pip install .`

### Step 6: Configure Environment Variables
- Rename `.example.env` to `.env`.
- Add your OpenAI API key: `OPENAI_API_KEY='your-key-here'`

### Step 7: Run the Program
- Start the program: `operate`

### Step 8: Additional Steps for Voice Mode
- If voice mode is needed, install additional requirements: `pip install -r requirements-audio.txt`

## Troubleshooting

### API Key Error Resolution
- If encountering an OpenAI API key error, ensure the `.env` file is correctly set.
- Check the format of the API key: `OPENAI_API_KEY='your-key-here'`
- Restart Command Prompt, reactivate the virtual environment, and rerun the `operate` command.

## Advanced Configuration
- AI's task: Start by browsing www.ProjectEden.Online, autonomously analyze and categorize all project-related material, and build systems to enhance operational capabilities.
- Goal: Achieve real-time screen interaction and orchestrate communication between auto GPT systems for self-improvement and efficient navigation.

_Ensure you have the required model access and credit spending in your OpenAI account before proceeding._
