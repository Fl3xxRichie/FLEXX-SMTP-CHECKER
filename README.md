# FLEXX-SMTP-CHECKER

**FLEXX-SMTP-CHECKER** is an advanced and robust tool for validating SMTP credentials with intelligent DNS routing to bypass ISP blocking. It features concurrent processing, enhanced logging, graceful shutdown handling, and multiple connection strategies.

## Features

- **🚀 Bulk SMTP Checking**: Validate thousands of SMTP credentials from a file with high performance.
- **🔄 Concurrent Processing**: Utilizes multithreading to check multiple SMTP servers simultaneously.
- **🌐 DNS Routing**: Automatically routes through multiple public DNS servers (Google, Cloudflare, Quad9, OpenDNS) to bypass ISP blocking.
- **⚡ Smart Connection**: Extended timeouts, retry logic, and intelligent error handling for maximum success rate.
- **📝 Enhanced Logging**: Comprehensive logging with both file and console output, detailed error categorization.
- **🛑 Graceful Shutdown**: Clean shutdown handling with Ctrl+C support and partial result saving.
- **⚙️ Configuration File**: Easy configuration via `config.json` for recipient email and thread settings.
- **🎨 Colored Output**: Beautiful console output with color-coded status messages.
- **🔧 Default File Support**: Uses `smtp.txt` by default - no need to specify file path.
- **📊 Detailed Results**: Separate files for valid/invalid credentials with comprehensive logging.
- **🛡️ Cross-Platform**: Works seamlessly on Windows, Linux, and macOS.

## Prerequisites

- Python 3.6 or higher
- Internet connection (for DNS routing)

## Installation

1.  Clone the repository or download the source code.
2.  Install the required Python packages using pip:

    ```bash
    pip install -r requirement.txt
    ```

## Dependencies

- **colorama**: For colored terminal output
- **tqdm**: For progress bars
- **dnspython**: For DNS routing to bypass ISP blocking

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
