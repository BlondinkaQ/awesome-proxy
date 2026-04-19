import requests


def proxy():

    proxy_creds = 'username:password@proxyserver:port'

    proxies = {
        'http': f'http://{proxy_creds}',
        'https': f'http://{proxy_creds}'
    }

    return proxies


def main():
    url = "https://www.example.com/"
    payload = ""

    headers = {
        # 1. User-Agent: Identifies the client.
        # The default Python User-Agent is often blocked by site protection
        # (e.g., Cloudflare). This string simulates a real modern browser
        # on Windows.
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),

        # 2. Accept: Tells the server what data formats we expect in response.
        # Prioritizes JSON, then HTML and XML (useful for both APIs and
        # web scraping).
        "Accept": "application/json, text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8",

        # 3. Content-Type: Specifies the format of the data you are sending
        # (request body). Most modern APIs work with JSON.
        "Content-Type": "application/json; charset=utf-8",

        # 4. Accept-Encoding: Allows the server to compress the response
        # (using gzip, deflate, br algorithms). Reduces bandwidth usage
        # and speeds up loading.
        "Accept-Encoding": "gzip, deflate, br",

        # 5. Accept-Language: Indicates the preferred language for the content.
        "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",

        # 6. Cache-Control: Cache management.
        # 'no-cache' is useful for scripts to always get the freshest data
        # from the server.
        "Cache-Control": "no-cache",

        # --- Headers added as needed ---

        # 7. Authorization: Used to access protected API resources.
        # "Authorization": "Bearer YOUR_TOKEN_HERE",

        # 8. Referer: Indicates the URL from which the transition supposedly
        # occurred (useful for scraping).
        "Referer": "https://www.example.com/"
    }

    prx = proxy()
    response = requests.request("GET", url, data=payload, headers=headers, proxies=prx, timeout=10)

    return response.status_code


if __name__ == '__main__':
    main()
