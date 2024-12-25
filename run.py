import requests

def load_config(file_path):
    """Load the user ID and proxy from a .txt file."""
    config = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split('=')
            config[key] = value
    return config

def setup_proxy(proxy_url):
    """Setup the proxy settings for the requests."""
    proxies = {
        'http': proxy_url,
        'https': proxy_url,
    }
    return proxies

def run_grass_lite_node(user_id, proxy_url):
    """Function to run the Grass Lite Node using the provided user ID and proxy."""
    url = "https://r.clarity.ms/collect"  # Contoh URL (ganti dengan URL yang benar)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Authorization': f'Bearer {user_id}'  # Ganti jika diperlukan format lain
    }

    proxies = setup_proxy(proxy_url)

    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            print("Grass Lite Node is running successfully.")
            print("Response:", response.json())
        else:
            print("Failed to run Grass Lite Node. Status code:", response.status_code)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    config = load_config("data.txt")  # Ganti dengan nama file .txt yang sesuai
    user_id = config.get("user_id")
    proxy_url = config.get("proxy")

    if user_id and proxy_url:
        run_grass_lite_node(user_id, proxy_url)
    else:
        print("Error: user_id or proxy not found in the configuration file.")
