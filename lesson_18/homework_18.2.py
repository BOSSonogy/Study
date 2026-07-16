import os
from urllib.parse import quote
import requests

BASE_URL = "http://127.0.0.1:8080"

def upload_image(file_path):
    upload_url = f"{BASE_URL}/upload"
    with open(file_path, "rb") as image:
        response = requests.post(
            upload_url,
            files={"image": image}
        )

    response.raise_for_status()
    return response.json()["image_url"]

def get_image_url(filename):
    encoded_filename = quote(filename)
    image_url = f"{BASE_URL}/image/{encoded_filename}"
    response = requests.get(
        image_url,
        headers={"Content-Type": "text"}
    )

    response.raise_for_status()
    return response.json()["image_url"]

def delete_image(filename):
    encoded_filename = quote(filename)
    delete_url = f"{BASE_URL}/delete/{encoded_filename}"
    response = requests.delete(delete_url)
    response.raise_for_status()

    return response.json()["message"]


def main():
    file_path = "mars_photo1.jpg"
    print("Uploading image...")

    uploaded_url = upload_image(file_path)
    print(f"Uploaded URL: {uploaded_url}")

    filename = os.path.basename(file_path)
    print("\nGetting image URL...")

    image_url = get_image_url(filename)
    print(f"Image URL: {image_url}")

    print("\nDeleting image...")
    message = delete_image(filename)
    print(message)

main()