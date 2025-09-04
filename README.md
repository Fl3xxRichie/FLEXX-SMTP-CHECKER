# FLEXX-SMTP-CHECKER

**FLEXX-SMTP-CHECKER** is a powerful and efficient tool for validating a large list of SMTP credentials. It concurrently checks each SMTP server's connectivity and authentication, helping you quickly identify which servers are active and accessible.

## Features

- **Bulk SMTP Checking**: Validate a large number of SMTP credentials from a file.
- **Concurrent Processing**: Utilizes multithreading to check multiple SMTP servers simultaneously, significantly speeding up the process.
- **Configuration File**: Easily configure the recipient email address and the default number of threads using a `config.json` file.
- **Detailed Logging**: Saves detailed logs of valid and invalid SMTP credentials in the `Result` directory.
- **Cross-Platform**: Works on both Windows and Linux.

## Prerequisites

- Python 3.x

## Installation

1.  Clone the repository or download the source code.
2.  Install the required Python packages using pip:

    ```bash
    pip install -r requirement.txt
    ```

## How to Use

1.  **Configure the application**:
    -   Open the `config.json` file.
    -   Set the `recipient_email` to the email address where you want to receive the test emails.
    -   Adjust the `default_threads` to set the default number of concurrent threads.

2.  **Prepare your SMTP list**:
    -   Create a text file (e.g., `smtp.txt`).
    -   Add your SMTP credentials in the following format, with each entry on a new line:
        ```
        HOST|PORT|USER|PASS
        ```
        **Example:**
        ```
        smtp.example.com|587|user@example.com|password123
        mail.anotherdomain.net|465|contact@anotherdomain.net|securepass
        ```

3.  **Run the script**:
    -   Open your terminal or command prompt.
    -   Execute the script with the path to your SMTP list file.

    **Basic usage:**
    ```bash
    python main.py smtp.txt
    ```

    **Specify the number of threads:**
    ```bash
    python main.py smtp.txt -t 50
    ```

## Output

The script will print the status of each SMTP server to the console. The results will also be saved in the `Result` directory:

-   `Result/valid.txt`: Contains the list of all valid SMTP credentials.
-   `Result/invalid.txt`: Contains the list of all invalid SMTP credentials.
-   `Result/logs.txt`: Contains detailed logs of the entire checking process.

## Disclaimer

This tool is provided for educational and personal use only. The author assumes no responsibility for any misuse or malicious activities conducted with it. As an open-source project, users are solely accountable for how they utilize this tool.
