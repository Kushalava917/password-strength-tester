# Password Strength Tester

A Flask-based web application to test the strength of passwords and generate strong passwords.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Step 1: Download the Code](#step-1-download-the-code)
  - [Step 2: Set Up a Virtual Environment](#step-2-set-up-a-virtual-environment)
  - [Step 3: Install Dependencies](#step-3-install-dependencies)
- [Usage](#usage)
  - [Step 1: Run the Flask Application](#step-1-run-the-flask-application)
  - [Step 2: Access the Application](#step-2-access-the-application)
  - [Step 3: Test Passwords](#step-3-test-passwords)
  - [Step 4: Generate Strong Passwords](#step-4-generate-strong-passwords)
- [Troubleshooting](#troubleshooting)
- [Additional Notes](#additional-notes)
- [License](#license)

## Features
- Check the strength of a password based on multiple criteria:
  - Minimum length (8 characters).
  - Presence of uppercase, lowercase, digits, and special characters.
  - Avoidance of common passwords.
  - Prevention of repetitive characters.
- Generate strong random passwords.
- User-friendly interface with real-time feedback.

## Prerequisites
Before running the application, ensure you have the following installed:

- **Python 3.6 or higher**: [Download Python](https://www.python.org/downloads/).
- **Pip**: Python's package manager (usually included with Python).
- **Git (optional)**: To clone the repository. [Download Git](https://git-scm.com/downloads).

## Installation

### Step 1: Download the Code
You can either clone the repository using Git or download the ZIP file:

#### Option 1: Clone the Repository (Using Git)
1. Open your terminal or command prompt.
2. Run the following command to clone the repository:
    ```bash
    git clone https://github.com/Kushalava917/password-strength-tester.git
    ```
3. Navigate to the project directory:
    ```bash
    cd password-strength-tester
    ```

#### Option 2: Download the ZIP File
1. Go to the [GitHub repository page](https://github.com/Kushalava917/password-strength-tester).
2. Click the "Code" button and select "Download ZIP".
3. Extract the ZIP file to your desired location.
4. Open your terminal or command prompt and navigate to the extracted folder:
    ```bash
    cd path/to/extracted/folder
    ```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)
It's a good practice to use a virtual environment to isolate dependencies.

#### On Windows:
1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment:
    ```bash
    venv\Scripts\activate
    ```

#### On macOS/Linux:
1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

### Step 3: Install Dependencies
Install the required Python packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt

