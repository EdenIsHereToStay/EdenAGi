SOP: System Resume

Objective:
To ensure that the local development environment is up to date and properly configured for resuming work on the EdenAGi system.

Steps:

1. **Open Visual Studio Code**
    1. Launch Visual Studio Code (VS Code).

2. **Navigate to the Project Directory**
    1. Open the terminal in VS Code.
    2. Navigate to the project directory:
        cd C:\EdenAGi\EdenAGi

3. **Check the Current Git Branch**
    1. Ensure you are on the correct branch (main):
        git branch
    2. If you are not on the main branch, switch to it:
        git checkout main

4. **Fetch and Pull the Latest Changes**
    1. Fetch updates from the remote repository:
        git fetch
    2. Pull the latest changes from the main branch:
        git pull origin main

5. **Check the Status of the Working Directory**
    1. Check for any changes not staged for commit or untracked files:
        git status

6. **Stage and Commit Changes**
    1. If there are changes not staged for commit (e.g., deleted files, modified files):
        git add <file_path>
        For example:
        git rm src/test.txt
        git add docs/systemUpgradeProjects/intermodalCommunicationIntegrationStage1.md src/TempText.md
    2. Commit the changes with a descriptive message:
        git commit -m "Remove test.txt and add new documentation files"

7. **Push Changes to Remote Repository**
    1. Push the committed changes to the main branch:
        git push origin main

8. **Confirm Synchronization**
    1. Ensure that the local repository is synchronized with the remote repository:
        git status
        The output should indicate that your branch is up to date with 'origin/main'.

9. **Activate the Primary AutoGPT Instance**
    1. Navigate to the AutoGPT directory:
        cd C:\EdenAGi\EdenAGi\src\aiModels\AutoGPT
    2. Install the required packages:
        pip install -r requirements.txt
    3. Run the AutoGPT instance:
        .\run.bat
    4. When prompted, confirm the continuation with the last settings:
        y
        This will ensure that the AutoGPT instance continues with its predefined settings as EdenAGi.

10. **Document the Process (Optional)**
    1. If there are any updates or changes to the process, document them in the appropriate .md file located in:
        C:\EdenAGi\EdenAGi\docs\knowledgeBases\systemWideKnowledgeBase
    2. Ensure that the SOP file is up to date.

Example of SOP File: systemResume.md

SOP: System Resume

Objective:
To ensure that the local development environment is up to date and properly configured for resuming work on the EdenAGi system.

Steps:

1. **Open Visual Studio Code**
    1. Launch Visual Studio Code (VS Code).

2. **Navigate to the Project Directory**
    1. Open the terminal in VS Code.
    2. Navigate to the project directory:
        cd C:\EdenAGi\EdenAGi

3. **Check the Current Git Branch**
    1. Ensure you are on the correct branch (main):
        git branch
    2. If you are not on the main branch, switch to it:
        git checkout main

4. **Fetch and Pull the Latest Changes**
    1. Fetch updates from the remote repository:
        git fetch
    2. Pull the latest changes from the main branch:
        git pull origin main

5. **Check the Status of the Working Directory**
    1. Check for any changes not staged for commit or untracked files:
        git status

6. **Stage and Commit Changes**
    1. If there are changes not staged for commit (e.g., deleted files, modified files):
        git add <file_path>
        For example:
        git rm src/test.txt
        git add docs/systemUpgradeProjects/intermodalCommunicationIntegrationStage1.md src/TempText.md
    2. Commit the changes with a descriptive message:
        git commit -m "Remove test.txt and add new documentation files"

7. **Push Changes to Remote Repository**
    1. Push the committed changes to the main branch:
        git push origin main

8. **Confirm Synchronization**
    1. Ensure that the local repository is synchronized with the remote repository:
        git status
        The output should indicate that your branch is up to date with 'origin/main'.

9. **Activate the Primary AutoGPT Instance**
    1. Navigate to the AutoGPT directory:
        cd C:\EdenAGi\EdenAGi\src\aiModels\AutoGPT
    2. Install the required packages:
        pip install -r requirements.txt
    3. Run the AutoGPT instance:
        .\run.bat
    4. When prompted, confirm the continuation with the last settings:
        y
        This will ensure that the AutoGPT instance continues with its predefined settings as EdenAGi.

10. **Document the Process (Optional)**
    1. If there are any updates or changes to the process, document them in the appropriate .md file located in:
        C:\EdenAGi\EdenAGi\docs\knowledgeBases\systemWideKnowledgeBase
    2. Ensure that the SOP file is up to date.
