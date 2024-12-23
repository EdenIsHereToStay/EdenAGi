### **pyenv Integration Knowledgebase Article**

#### **Overview**

`pyenv` is a powerful tool for managing multiple Python versions on a single system. It enables developers to install, switch, and manage different Python versions without interfering with the system Python or other projects. This is particularly useful in environments requiring multiple Python versions for compatibility with diverse tools and dependencies.

For EdenAGI systems, `pyenv` provides a robust framework for maintaining Python version control, allowing seamless integration of Open-Interpreter, FastAPI-based APIs, and other Python-driven components.

---

### **Key Features**

1. **Python Version Management**:

   - Install and manage multiple versions of Python.
   - Use pre-release versions of Python for testing.
   - Isolate project dependencies by specifying Python versions per project.

2. **Compatibility**:

   - Supports Python 2.x, Python 3.x, and alternative interpreters like PyPy and Jython.
   - Compatible with Linux, macOS, and Windows (via `pyenv-win`).

3. **Virtual Environment Integration**:

   - Create and manage virtual environments with the `pyenv-virtualenv` plugin.
   - Automatically activate virtual environments based on project directories.

4. **Seamless Switching**:
   - Switch between global, local, and shell-specific Python versions effortlessly.

---

### **Installation Instructions**

#### **For Linux/macOS**

1. **Install Dependencies**:

   ```bash
   sudo apt update
   sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
   libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev
   ```

2. **Install pyenv**:

   ```bash
   curl https://pyenv.run | bash
   ```

3. **Add pyenv to PATH**:
   Add the following lines to `~/.bashrc` or `~/.zshrc`:

   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)"
   ```

4. **Reload the Shell**:
   ```bash
   exec "$SHELL"
   ```

#### **For Windows**

1. **Install pyenv-win**:

   ```powershell
   Invoke-WebRequest -Uri https://pyenv.run -UseBasicParsing | Invoke-Expression
   ```

2. **Add pyenv to PATH**:

   ```powershell
   [System.Environment]::SetEnvironmentVariable("PYENV", "$HOME\.pyenv", "User")
   [System.Environment]::SetEnvironmentVariable("PATH", "$HOME\.pyenv\bin;$HOME\.pyenv\shims;$env:PATH", "User")
   ```

3. **Restart the Terminal**.

---

### **Usage Instructions**

#### **Install Python Versions**

1. List available versions:
   ```bash
   pyenv install --list
   ```
2. Install specific versions:
   ```bash
   pyenv install 3.10.12
   pyenv install 3.12.0
   ```

#### **Switch Between Versions**

1. Set a global default version:
   ```bash
   pyenv global 3.10.12
   ```
2. Set a local version for a project:
   ```bash
   pyenv local 3.12.0
   ```
3. Temporarily set a shell-specific version:
   ```bash
   pyenv shell 3.11.6
   ```

#### **Create Virtual Environments**

1. Install the `pyenv-virtualenv` plugin (if not already installed):
   ```bash
   pyenv virtualenv <python_version> <environment_name>
   ```
2. Activate a virtual environment:
   ```bash
   pyenv activate <environment_name>
   ```
3. Deactivate the environment:
   ```bash
   pyenv deactivate
   ```

---

### **Integration with EdenAGI Systems**

1. **Python Version Management**:

   - Use `pyenv` to install Python versions required by Open-Interpreter, FastAPI, or any other Python-based component.
   - Maintain compatibility with legacy Python tools while experimenting with the latest versions.

2. **Virtual Environments**:

   - Assign virtual environments to EdenAGI submodules (e.g., `eden-core`, `eden-api`).
   - Use `.python-version` files in project directories to automate environment activation.

3. **Continuous Integration (CI)**:

   - Integrate `pyenv` into CI pipelines to test EdenAGI components across multiple Python versions.

4. **Conflict Resolution**:
   - Isolate dependencies for submodules by combining `pyenv` with `pip` or `poetry` for package management.
   - Avoid global dependency conflicts by leveraging local and virtual environments.

---

### **Testing pyenv Integration**

1. Verify installed versions:
   ```bash
   pyenv versions
   ```
2. Test Python version switching:
   ```bash
   pyenv global 3.10.12
   python --version
   pyenv global 3.12.0
   python --version
   ```
3. Validate virtual environments:
   ```bash
   pyenv virtualenv 3.10.12 test-env
   pyenv activate test-env
   python --version
   pyenv deactivate
   ```
4. Test EdenAGI components under specific Python versions and virtual environments.

---

### **Benefits for EdenAGI**

- Simplifies Python version management across agents and subsystems.
- Enhances compatibility testing for legacy and cutting-edge Python versions.
- Reduces dependency conflicts by isolating environments for different projects.
- Improves maintainability and scalability of Python-based components.

---

### **Conclusion**

`pyenv` is a critical tool for managing Python versions and dependencies within the EdenAGI ecosystem. Its flexibility and ease of use ensure compatibility across diverse components while minimizing the risk of conflicts. By integrating `pyenv` into EdenAGI workflows, the system can achieve greater stability, scalability, and developer efficiency.
