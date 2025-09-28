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

### 1. Configuration
- Open `config.json` and set your `recipient_email` (where test emails will be sent)
- Adjust `default_threads` (default: 10) for concurrent processing

### 2. SMTP List Format
Create `smtp.txt` with credentials in this format (one per line):
```
HOST|PORT|USER|PASS
```
**Examples:**
```
smtp.gmail.com|587|user@gmail.com|password123
mail.example.com|465|contact@example.com|securepass
smtp.office365.com|587|user@outlook.com|password
```

### 3. Usage Examples

**🚀 Basic Usage (uses smtp.txt by default):**
```bash
python main.py
```

**📄 Custom SMTP File:**
```bash
python main.py my_smtp_list.txt
```

**⚡ Custom Thread Count:**
```bash
python main.py -t 20
```

**📋 Combined Options:**
```bash
python main.py custom_smtp.txt -t 50
```

### 5. Example Output
```
[*] Loaded 1,250 SMTP credentials from smtp.txt
Starting SMTP check with 15 threads for 1,250 credentials
[*] Trying smtp.gmail.com:587 with DNS routing...
[*] Resolved smtp.gmail.com -> 66.102.1.109 using DNS 8.8.8.8
[+] VALID SMTP: smtp.gmail.com:587 | user@gmail.com
[*] Trying mail.example.com:465 with DNS routing...
[*] Resolved mail.example.com -> 192.168.1.100 using DNS 1.1.1.1
[!] Connection attempt 1 to 192.168.1.100 failed: TimeoutError
[!] Connection attempt 2 to 192.168.1.100 failed: TimeoutError
[-] Failed to connect to mail.example.com:465 with all DNS servers

[+] DONE! VALIDS: 847, INVALIDS: 403
```

### 4. DNS Routing (Automatic)
The script automatically routes through multiple DNS servers to bypass ISP blocking:
- **Google DNS** (8.8.8.8, 8.8.4.4)
- **Cloudflare DNS** (1.1.1.1)
- **Quad9 DNS** (9.9.9.9)
- **OpenDNS** (208.67.222.222, 208.67.220.220)

This significantly improves success rates when ISPs block SMTP domains.

## Output

### Console Output
The script provides real-time colored output:
- **🟢 Green**: Valid SMTP credentials
- **🔴 Red**: Invalid/failed credentials
- **🟡 Yellow**: Connection attempts and warnings
- **🟠 Cyan**: DNS routing and progress information

**Example Output:**
```
[*] Trying smtp.gmail.com:587 with DNS routing...
[*] Resolved smtp.gmail.com -> 66.102.1.109 using DNS 8.8.8.8
[+] VALID SMTP: smtp.gmail.com:587 | user@gmail.com
```

### Result Files
All results are saved in the `Result/` directory:

- **✅ `Result/valid.txt`**: Working SMTP credentials
- **❌ `Result/invalid.txt`**: Failed SMTP credentials with error details
- **📋 `Result/logs.txt`**: Comprehensive execution logs with timestamps

### Graceful Shutdown
- **Ctrl+C Support**: Press Ctrl+C for clean shutdown
- **Partial Results**: Saves progress even if interrupted
- **Resource Cleanup**: Properly closes connections and files

## Troubleshooting

### Common Issues

**🔒 ISP Blocking SMTP Ports:**
- The script automatically uses DNS routing to bypass blocking
- If still blocked, consider using a VPN for complete bypass
- Gmail SMTP usually works better as it's less commonly blocked

**⏱️ Timeout Errors:**
- Script uses 30-second timeout with 3 retry attempts
- Some servers may be slow to respond
- Check your internet connection stability

**🔐 Authentication Failures:**
- Verify username/password combinations
- Some providers require app-specific passwords
- Check if accounts are locked or require verification

**🌐 DNS Resolution Issues:**
- Script tries multiple public DNS servers automatically
- If all fail, check your internet connection
- Consider using a different network (mobile hotspot)

### Performance Tips

- **Start with 10 threads** and increase gradually
- **Gmail SMTPs** typically have higher success rates
- **Use stable internet connection** for best results
- **Monitor RAM usage** with large SMTP lists

## Changelog

### Version 2.0 - Enhanced Edition
- ✅ **DNS Routing**: Bypass ISP blocking with multiple DNS servers
- ✅ **Default File Support**: Use smtp.txt without specifying path
- ✅ **Enhanced Logging**: Comprehensive file and console logging
- ✅ **Graceful Shutdown**: Clean Ctrl+C handling with partial result saving
- ✅ **Better Error Handling**: Detailed error categorization and reporting
- ✅ **Extended Timeouts**: 30-second timeout with retry logic
- ✅ **Colored Output**: Beautiful console interface with status colors

## Disclaimer

This tool is provided for educational and personal use only. The author assumes no responsibility for any misuse or malicious activities conducted with it. As an open-source project, users are solely accountable for how they utilize this tool.

**Note**: Always respect the terms of service of email providers and use this tool responsibly. Some email providers may flag or block automated connection attempts.
