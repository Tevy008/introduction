import requests
import os
import shutil


def download_picture(folder, filename, url):
    file_path = os.path.join(folder,filename)
    img_response = requests.get(url)
    img_response.raise_for_status()
    with open(file_path, 'wb') as f:
        f.write(img_response.content)


def main():
    folder = "dog_images"
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

    for number in range(1,51):
        url = "https://random.dog/woof.json"
        params = {'filter': 'mp4,webm'}
        response = requests.get(url,params=params)
        data = response.json()
        picture_link = data["url"]
        filename,picture_extension = os.path.splitext(picture_link)
        filename = f"dog_{number}{picture_extension}"
        download_picture(folder, filename, picture_link)


if __name__ == '__main__':
    main()