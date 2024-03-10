# The vision

To develop a simple, yet powerful tool that processes user-input text to generate flashcards for study purposes, with an option to export these in a format compatible with Anki, a popular flashcard application.

# Installation Guidelines

### Step 1: Setting up the Environment Variable

Before installing the application, you need to set up an environment variable for the OpenAI API key. This key allows our tool to communicate with OpenAI's services.

-   **For Windows Users:**

    1. Open the Start Search, type in "env", and choose "Edit the system environment variables".
    2. In the System Properties window, click on the "Environment Variables..." button.
    3. Under "User variables," click on "New..." to create a new environment variable.
    4. For "Variable name," enter `OPENAI_API_KEY`.
    5. For "Variable value," paste your OpenAI API key.
    6. Click "OK" and apply the changes.

-   **For macOS/Linux Users:**
    1. Open your terminal.
    2. Edit your shell profile file (e.g., `~/.bash_profile`, `~/.zshrc`, etc.) by typing `nano ~/.bash_profile` (replace `.bash_profile` with your specific file).
    3. Add the following line at the end of the file: `export OPENAI_API_KEY='your_api_key_here'`
    4. Press CTRL + X to close, then Y to save changes, and Enter to confirm.
    5. To apply the changes, type `source ~/.bash_profile` (replace `.bash_profile` with your specific file).

Please replace `'your_api_key_here'` with your actual OpenAI API key.

### Step 2: Installing the Tool

With your environment variable set, the next steps involve setting up the tool itself, which is built on Flask, a lightweight WSGI web application framework in Python.

1. **Clone the Repository**
   Start by cloning the repository to your local machine.

    ```bash
    git clone https://github.com/Endlessflow/flashcard-generator.git
    ```

2. **Install Python Requirements**
   Ensure you have Python installed on your system. This tool requires Python 3.6 or newer. You can check your Python version by running `python --version` in your terminal or command prompt.

    Next, install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Running the Flask Application**
   Finally, to run the Flask application, use the following command from the terminal or command prompt:

    ```bash
    flask run
    ```

    This command starts the Flask web server. You should see output indicating the server is running and listening on a local port (usually `127.0.0.1:5000`). You can now open a web browser and navigate to this address to interact with the tool.

### Step 3: Enjoy

This should be all you need. Happy studying!
