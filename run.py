import requests
import json

# Fungsi untuk membaca user_id dari file
def read_user_ids(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Fungsi untuk membaca proxy dari file
def read_proxies(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Fungsi untuk membuat node di Grass
def create_grass_node(user_id, proxy):
    url = "https://api.grass.com/create-node"  # Ganti dengan URL API yang sesuai
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {user_id}",  # Jika perlu otentikasi dengan token
    }
    data = {
        "node_name": "MyNode",  # Sesuaikan parameter lainnya jika diperlukan
        "node_description": "Automatically created node."
    }

    proxies = {
        "http": proxy,
        "https": proxy,
    }

    try:
        response = requests.post(url, headers=headers, json=data, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(f"Success for user_id {user_id}: {response.json()}")
        else:
            print(f"Failed for user_id {user_id}: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error for user_id {user_id} with proxy {proxy}: {e}")

if __name__ == "__main__":
    user_ids_file = "user_ids.txt"  # File dengan daftar user_id
    proxies_file = "proxies.txt"    # File dengan daftar proxy

    user_ids = read_user_ids(user_ids_file)
    proxies = read_proxies(proxies_file)

    if not user_ids:
        print("User ID file is empty.")
    if not proxies:
        print("Proxy file is empty.")

    for user_id, proxy in zip(user_ids, proxies):  # Iterasi dengan menggabungkan user_id dan proxy
        create_grass_node(user_id, proxy)
