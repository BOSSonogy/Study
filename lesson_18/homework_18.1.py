import requests

BASE_URL = "https://images-api.nasa.gov"

def search_photos():
    search_url = f"{BASE_URL}/search"
    search_params = {
        "q": "Curiosity rover Mars",
        "media_type": "image",
        "page_size": 20
    }

    response = requests.get(search_url, params=search_params)
    response.raise_for_status()
    response_json = response.json()
    nasa_ids = []

    for item in response_json["collection"]["items"]:
        nasa_data = item.get("data")

        if nasa_data:
            nasa_id = nasa_data[0].get("nasa_id")

            if nasa_id:
                nasa_ids.append(nasa_id)

    return nasa_ids

def get_jpg_url(nasa_id):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    response = requests.get(asset_url)
    response.raise_for_status()
    response_json = response.json()

    for item in response_json["collection"]["items"]:
        href = item.get("href", "")

        if href.lower().endswith(".jpg"):
            return href

    return None


def download_image(image_url, filename):
    response = requests.get(image_url)
    response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(response.content)

    print(f"{filename} saved.")


def main():
    nasa_ids = search_photos()
    photos_saved = 0

    for nasa_id in nasa_ids[2:]:
    # for nasa_id in nasa_ids:
        
        jpg_url = get_jpg_url(nasa_id)

        if jpg_url is None:
            continue

        filename = f"mars_photo{photos_saved + 1}.jpg"
        download_image(jpg_url, filename)
        photos_saved += 1
        if photos_saved == 2:
            break

    if photos_saved < 2:
        print("Couldn't download two images.")
    else:
        print("Done.")


main()