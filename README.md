# Python Automation for Platform

This script is used to quickly make local platform workspaces through automation. Only manual requirement is the insertion of Confirmation Code that platform generates during the creation of a workspace.

## Getting Started with Python in VS Code

Source: [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

### Prerequisites

- VS Code
- VS Code Python extension
- Python 3

### Install Visual Studio Code and the Python Extension

1. If you have not already done so, install  [VS Code](https://code.visualstudio.com/).
2. Next, install the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the Visual Studio Marketplace. For additional details on installing extensions, see [Extension Marketplace](https://code.visualstudio.com/docs/editor/extension-marketplace). The Python extension is named **Python** and it's published by Microsoft.

### Install a Python interpreter
##### macOS
The system install of Python on macOS is not supported. Instead, an installation through  [Homebrew](https://brew.sh/)  is recommended. To install Python using Homebrew on macOS use  `brew install python3`  at the Terminal prompt.

### Verify the Python installation
To verify that you've installed Python successfully on your machine, run one of the following commands (depending on your operating system):

-   Linux/macOS: open a Terminal Window and type the following command
    ```
    python3 --version
    ```

-   Windows: open a command prompt and run the following command:

    ```
    py -3 --version
    ```

If the installation was successful, the output window should show the version of Python that you installed.

> **Note**  You can use the  `py -0`  command in the VS Code integrated terminal to view the versions of python installed on your machine. The default interpreter is identified by an asterisk (*).

### Select a Python interpreter
Python is an interpreted language, and in order to run Python code and get Python IntelliSense, you must tell VS Code which interpreter to use.

From within VS Code, select a Python 3 interpreter by opening the  **Command Palette**  (⇧⌘P), start typing the  **Python: Select Interpreter**  command to search, then select the command. You can also use the  **Select Python Environment**  option on the Status Bar if available (it may already show a selected interpreter, too):

![No interpreter selected](https://code.visualstudio.com/assets/docs/python/environments/no-interpreter-selected-statusbar.png)

The command presents a list of available interpreters that VS Code can find automatically, including virtual environments. If you don't see the desired interpreter, see  [Configuring Python environments](https://code.visualstudio.com/docs/python/environments).

### Install Dependencies
Use Command Palette to run **Terminal: Create New Terminal** (⌃⇧`). This command opens a command prompt for your selected interpreter.

A best practice among Python developers is to avoid installing packages into a global interpreter environment. You instead use a project-specific  `virtual environment`  that contains a copy of a global interpreter. Once you activate that environment, any packages you then install are isolated from other environments. Such isolation reduces many complications that can arise from conflicting package versions. To create a  _virtual environment_  and install the required packages, enter the following commands as appropriate for your operating system:

> **Note**: For additional information about virtual environments, see  [Environments](https://code.visualstudio.com/docs/python/environments#_global-virtual-and-conda-environments).

1.  Create and activate the virtual environment

    > **Note**: When you create a new virtual environment, you should be prompted by VS Code to set it as the default for your workspace folder. If selected, the environment will automatically be activated when you open a new terminal.

    ![Virtual environment dialog](https://code.visualstudio.com/assets/docs/python/tutorial/virtual-env-dialog.png)



    **For macOS/Linux**
    
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2.  Select your new environment by using the  **Python: Select Interpreter**  command from the  **Command Palette**.

3.  Install the packages

    ```
    # Don't use with Anaconda distributions because they include matplotlib already.
    
    # macOS
    pip install -r requirements.txt 
    or
    python3 pip install -r requirements.txt
    ```

