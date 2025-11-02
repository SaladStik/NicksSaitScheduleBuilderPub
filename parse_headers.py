"""
HTTP Header Parser for Banner API Authentication
Extracts cookies and synchronizer token from copied browser request headers
"""

import re


def parse_request_headers(headers_text):
    """
    Parse HTTP request headers to extract Banner API authentication tokens

    Args:
        headers_text (str): Raw HTTP request headers copied from browser dev tools

    Returns:
        dict: Dictionary containing parsed authentication data
    """
    result = {
        "cookies": {},
        "sync_token": None,
        "unique_session_id": None,
        "host": None,
        "base_url": None,
        "success": False,
        "errors": [],
    }

    try:
        # Extract uniqueSessionId from URL if present
        session_id_match = re.search(r"uniqueSessionId=([^&\s]+)", headers_text)
        if session_id_match:
            result["unique_session_id"] = session_id_match.group(1).strip()

        # Extract Cookie header
        cookie_match = re.search(r"Cookie:\s*([^\n\r]+)", headers_text, re.IGNORECASE)
        if cookie_match:
            cookie_string = cookie_match.group(1).strip()
            # Parse individual cookies
            for cookie in cookie_string.split(";"):
                cookie = cookie.strip()
                if "=" in cookie:
                    name, value = cookie.split("=", 1)
                    result["cookies"][name.strip()] = value.strip()
        else:
            result["errors"].append("No Cookie header found")

        # Extract X-Synchronizer-Token
        sync_token_match = re.search(
            r"X-Synchronizer-Token:\s*([^\n\r]+)", headers_text, re.IGNORECASE
        )
        if sync_token_match:
            result["sync_token"] = sync_token_match.group(1).strip()
        else:
            result["errors"].append("No X-Synchronizer-Token header found")

        # Extract Host
        host_match = re.search(r"Host:\s*([^\n\r]+)", headers_text, re.IGNORECASE)
        if host_match:
            result["host"] = host_match.group(1).strip()
            result["base_url"] = f"https://{result['host']}"
        else:
            result["errors"].append("No Host header found")

        # Check if we got the minimum required info
        if result["cookies"] and result["sync_token"]:
            result["success"] = True

    except Exception as e:
        result["errors"].append(f"Parsing error: {str(e)}")

    return result


def format_for_banner_api(parsed_data):
    """
    Format parsed data for use with Banner API functions

    Args:
        parsed_data (dict): Output from parse_request_headers()

    Returns:
        dict: Formatted credentials ready for API calls
    """
    if not parsed_data["success"]:
        return None

    # Build cookie string for requests
    cookie_string = "; ".join(
        [f"{name}={value}" for name, value in parsed_data["cookies"].items()]
    )

    return {
        "cookies": cookie_string,
        "sync_token": parsed_data["sync_token"],
        "unique_session_id": parsed_data.get("unique_session_id", ""),
        "base_url": parsed_data["base_url"],
        "headers": {
            "Cookie": cookie_string,
            "X-Synchronizer-Token": parsed_data["sync_token"],
        },
    }


def display_results(parsed_data):
    """
    Display parsed results in a readable format
    """
    print("=" * 80)
    print("BANNER API AUTHENTICATION PARSER")
    print("=" * 80)

    if parsed_data["success"]:
        print("\n✓ Successfully parsed authentication tokens!\n")

        print(f"Host: {parsed_data['host']}")
        print(f"Base URL: {parsed_data['base_url']}")
        print(f"\nSynchronizer Token: {parsed_data['sync_token']}")

        print("\nCookies:")
        for name, value in parsed_data["cookies"].items():
            # Truncate long cookie values for display
            display_value = value if len(value) < 50 else value[:47] + "..."
            print(f"  {name}: {display_value}")

        print("\n" + "-" * 80)
        print("READY TO USE IN CODE:")
        print("-" * 80)

        formatted = format_for_banner_api(parsed_data)
        print("\n# Add this to your Streamlit app or fetch_classes.py:\n")
        print("credentials = {")
        print(f"    'cookies': '{formatted['cookies']}',")
        print(f"    'sync_token': '{formatted['sync_token']}'")
        print("}")

    else:
        print("\n✗ Failed to parse headers\n")
        print("Errors:")
        for error in parsed_data["errors"]:
            print(f"  - {error}")

    print("\n" + "=" * 80)


def main():
    """
    Interactive CLI for parsing headers
    """
    print("=" * 80)
    print("Banner API Header Parser")
    print("=" * 80)
    print("\nInstructions:")
    print("1. Open your browser DevTools (F12)")
    print("2. Go to Network tab")
    print("3. Navigate to SAIT Banner (Class Registration)")
    print("4. Find any request to 'classSearch' or similar")
    print("5. Right-click → Copy → Copy as cURL or Copy Request Headers")
    print("6. Paste below (press Enter, then Ctrl+D or Ctrl+Z+Enter when done)")
    print("\n" + "=" * 80)
    print("\nPaste your headers here:\n")

    # Read multi-line input
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    headers_text = "\n".join(lines)

    if not headers_text.strip():
        print("\nNo input received. Exiting.")
        return

    # Parse the headers
    result = parse_request_headers(headers_text)
    display_results(result)


# Example usage with the provided headers
EXAMPLE_HEADERS = """GET /StudentRegistrationSsb/ssb/classSearch/get_subjectcoursecombo?searchTerm=&term=202530&offset=1&max=10&uniqueSessionId=54ktv1761859042020&_=1761868113369 HTTP/1.1
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: en-US,en;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Cookie: JSESSIONID=3CB2F72D0B8566B63FE6EED5CE220199; NLB=1116a3db1128e77d45e3b4da77c98636fc907ab682b8e93c20244d08950e30009377a334; NSC_ESNS=14ca2989-05d6-1904-9678-005056baaca9_0874326293_0928480473_00000000004643198069
Host: sait-sust-prd-prd1-ban-ss-ssag6.sait.ca
Pragma: no-cache
Referer: https://sait-sust-prd-prd1-ban-ss-ssag6.sait.ca/StudentRegistrationSsb/ssb/classRegistration/classRegistration
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
X-Requested-With: XMLHttpRequest
X-Synchronizer-Token: 36392fea-6d6b-41d3-a4d3-f46333133e9a
sec-ch-ua: "Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
"""


if __name__ == "__main__":
    # Uncomment to test with example headers
    # print("Testing with example headers...\n")
    # result = parse_request_headers(EXAMPLE_HEADERS)
    # display_results(result)

    # Run interactive mode
    main()
