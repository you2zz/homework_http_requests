# Задача №2 (с ООП)

import requests

from ya_disk import YandexDisk

TOKEN = ''
if __name__ == '__main__':
    yd = YandexDisk(token=TOKEN)
    yd.upload_file_to_disk("test12052023.txt", "test12052023.txt")




# # Задача №2 (без ООП)

# import requests

# def get_upload_link(disk_file_path, token):
#         upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
#         headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
#         params = {"path": disk_file_path, "overwrite": "true"}
#         response = requests.get(upload_url, headers=headers, params=params)
#         return response.json()

# def upload_file_to_disk(disk_file_path, filename, token):
#         href = get_upload_link(disk_file_path=disk_file_path, token=token).get("href", "")
#         response = requests.put(href, data=open(filename, 'rb'))
#         response.raise_for_status()
#         if response.status_code == 201:
#             print("Success")

# token = ''
# upload_file_to_disk("test12052023.txt", "test12052023.txt", token)