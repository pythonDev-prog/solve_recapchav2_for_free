"""
ReCAPTCHA v2 Solver using Playwright and NopeCHA Extension

This script automates the solving of ReCAPTCHA v2 challenges using the NopeCHA
browser extension with Playwright. It launches a Chromium browser with the extension
loaded and navigates to a specified URL.

Author: Mohammed Anaam
"""

import argparse
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, Error as PlaywrightError


def get_extension_path():

    # Use relative path from script location
    script_dir = Path(__file__).parent
    extension_path = script_dir / "extension" / "nopecha-extensionC"
    
    if not extension_path.exists():
        raise FileNotFoundError(
            f"Extension directory not found at: {extension_path}\n"
            f"Please ensure the NopeCHA extension is placed in the 'extension' folder."
        )
    
    return extension_path


def solve_recaptcha(url, wait_time=360, headless=False, timeout=90000):
   
    try:
        extension_path = get_extension_path()
        print(f"[INFO] Using extension from: {extension_path}")
        
        with sync_playwright() as p:
            print("[INFO] Launching browser...")
            
            # Launch browser with NopeCHA extension
            browser = p.chromium.launch_persistent_context(
                user_data_dir="",
                headless=headless,
                args=[
                    '--disable-blink-features=AutomationControlled',
                    '--disable-dev-shm-usage',
                    f"--disable-extensions-except={extension_path.resolve()}",
                    f"--load-extension={extension_path.resolve()}",
                ]
            )
            
            print(f"[INFO] Navigating to: {url}")
            page = browser.new_page()
            page.goto(url, timeout=timeout)
            
            print(f"[SUCCESS] Page loaded: {page.title()}")
            print(f"[INFO] Waiting {wait_time} seconds for ReCAPTCHA solving...")
            print("[INFO] The NopeCHA extension will handle the ReCAPTCHA automatically.")
            
            time.sleep(wait_time)
            
            print("[INFO] Closing browser...")
            browser.close()
            
            return True
            
    except FileNotFoundError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return False
        
    except PlaywrightError as e:
        print(f"[ERROR] Playwright error: {e}", file=sys.stderr)
        return False
        
    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user. Closing browser...")
        try:
            browser.close()
        except:
            pass
        return False
        
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}", file=sys.stderr)
        return False


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Solve ReCAPTCHA v2 using NopeCHA extension with Playwright",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python solve_recaptchav2.py
  python solve_recaptchav2.py --url "https://example.com/form"
  python solve_recaptchav2.py --wait-time 300 --headless
        """
    )
    
    parser.add_argument(
        "--url",
        type=str,
        default="https://www.google.com/recaptcha/api2/demo",
        help="URL to visit (default: Google ReCAPTCHA demo)"
    )
    
    parser.add_argument(
        "--wait-time",
        type=int,
        default=360,
        help="Time to wait in seconds (default: 360)"
    )
    
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run browser in headless mode (not recommended for ReCAPTCHA)"
    )
    
    parser.add_argument(
        "--timeout",
        type=int,
        default=90000,
        help="Page navigation timeout in milliseconds (default: 90000)"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("ReCAPTCHA v2 Solver with NopeCHA Extension")
    print("=" * 60)
    
    success = solve_recaptcha(
        url=args.url,
        wait_time=args.wait_time,
        headless=args.headless,
        timeout=args.timeout
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
