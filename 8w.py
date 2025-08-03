import base64, json, random

locales = ["en-US", "en-GB", "de-DE", "fr-FR", "es-ES", "tr-TR", "ja-JP"]
os_versions = ["10", "11", "10.0.22621", "10.0.19045"]
chrome_versions = ["114.0.0.0", "115.0.0.0", "116.0.5845.110", "117.0.5938.92", "118.0.5993.117"]

def _8w():
    locale = random.choice(locales)
    os_version = random.choice(os_versions)
    chrome_version = random.choice(chrome_versions)
    build_number = random.randint(20000, 30000)

    user_agent = f"Mozilla/5.0 (Windows NT {os_version}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"

    properties = {
        "os": "Windows",
        "browser": "Chrome",
        "device": "",
        "system_locale": locale,
        "browser_user_agent": user_agent,
        "browser_version": chrome_version,
        "os_version": os_version,
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": build_number,
        "client_event_source": None
    }
    return base64.b64encode(json.dumps(properties).encode()).decode()

count = int(input("[-] Enter how many Super Properties you want to generate: "))

super_props = [_8w() for _ in range(count)]

with open("list.json", "w", encoding="utf-8") as f:
    json.dump(super_props, f, indent=2)

print(f"[+] Successfully generated {count} X-Super-Properties in list.json")
