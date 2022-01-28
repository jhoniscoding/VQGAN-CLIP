import requests


def main():
    url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20&collection=boredapeyachtclub"
    headers = {
        "Accept": "application/json",
        "X-API-KEY": "2f6f419a083c46de9d83ce3dbe7db601"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    for asset in data["assets"]:
        img_url = asset["image_url"]
        img_resp = requests.get(img_url)
        with open(f"outputs/{asset['id']}.png", "wb") as f:
            f.write(img_resp.content)


if __name__ == '__main__':
    main()
