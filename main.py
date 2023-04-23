import requests
import json

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)

hero = ''
intelligence = 0
data = response.json()
for d in data:
    name = d['name']
    intell = d['powerstats']['intelligence']
    if name == 'Hulk' or name == 'Captain America' or name == 'Thanos':
       if intell > intelligence:
           hero = name
           intelligence = intell

print(hero)
# ------------------------------
class YaUploader:
    def __init__(self, token: str):
        self.token = token
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get('href')
        return href
    def upload(self, file_path: str):
        href = self._get_upload_link(disk_file_path=file_path)
        response = requests.put(href, data=open(file_path, 'rb'))

if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = 'y0_AgAAAAABbe-7AADLWwAAAADhpYBPvqgp78YvQ-Sd96Nhadiq_6-DZoc'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)