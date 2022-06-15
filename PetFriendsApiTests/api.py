import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url="https://petfriends.skillfactory.ru"

    def post_add_pets_no_foto(self, auth_key: json, name: str, animal_type: str, age: int) -> json:
        """Метод делает запрос к API сервера и добавляет информацию о новом питомце"""

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.post(self.base_url + '/api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_api_key(self, email:str, password: str) -> json:
        """Метод делает запрос к API сервера и вщзвращает статус запроса и результат в формате JSON
        с уникальным ключом пользователя, найденным по указанным email и паролем """
        headers = {'email':email, 'password':password}
        res = requests.get(self.base_url+'/api/key', headers = headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text

        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и резульат со списком найденных
        питомцев, совпадающих с фильтром. На данный момент фильтр пустое значение - получить список всех
        питомцев"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url+'/api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return  status, result

    def post_add_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        """ Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url+'/api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_add_photo(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """ Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url+'/api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_pets(self, auth_key: json,  pet_id: str) -> json:
        """ Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления о успешном удалении."""

        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url+'/api/pets/'+ pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return  status, result

    def put_update_pets(self, auth_key: json,  pet_id: str,
                        name: str, animal_type: str, age: str) -> json:
        """ Метод отправляет запрос на сервер о обновлении данных питомуа по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""

        data = {
                'name': name,
                'animal_type': animal_type,
                'age': age
            }
        headers = {'auth_key': auth_key['key']}
        res = requests.put(self.base_url+'/api/pets/'+ pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return  status, result