import os
from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_valid_user(email = valid_email, password = valid_password):
    # Получаем ключ
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter = ''):
    # Получаем ключ и список всех питомцев. Доступное значение параметра filter - 'my_pets' либо ''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key=auth_key, filter=filter)

    # Смотрим что список не пустой
    assert status == 200
    assert len(result['pets'])>0

def test_post_add_pets_no_foto(name="Джек", animal_type="кот", age=3):
    # Получаем ключ и добавляем питомца без фото
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pets_no_foto(auth_key, name, animal_type, age)

    # Сравниваем что в списке есть даные питомца которого добавляли
    assert status == 200
    assert result['name']==name and result['age']==str(age) and result['animal_type']==animal_type

def test_post_add_new_pets(name="Mia", animal_type="wolf", age='1', pet_photo = r'images/kotik.jpg'):
    # Сохраняем в переменную pet_photo полный путь к файлу
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ и добавляем питомца
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сравниваем что в списке есть даные питомца которого добавляли
    assert status == 200
    assert result['name']==name and result['age']==age and result['animal_type']==animal_type

def test_delete_pets():
    # получаем ключ и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    #  Если список пустой, то создаем питомца
    if len(my_pets['pets']) == 0:
        pf.post_add_new_pet(auth_key, "oland", "wol", '22', r'images/kotik.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    #  Берем id первого питомца и пробуем его удалить
    pet_id = my_pets["pets"][0]["id"]
    status, _ = pf.delete_pets(auth_key, pet_id)

    # Получаем список питомцев и сравниваем что в списке нет id удаленного питомца
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    assert status == 200
    assert pet_id not in my_pets.values()

#-------------------------------- 10 тест кейсов ---------------------------------------------------------

def test_update_pets( name='Mark', animal_type='beer', age='33'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)   #получаем ключ
    _,  my_pets = pf.get_list_of_pets(auth_key, 'my_pets')       #получаем список своих питомцев
    print("my_pets['pets'][0][id]=", my_pets["pets"][0]["id"])
# Если список питомцев не пустой меняем данные
    if len(my_pets['pets']) > 0:
        status, result = pf.put_update_pets(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
# Иначе вызываем исключение с сообщением
    else:
        raise Exception ("There is no my pets")

def test_add_photo(pet_photo = r'images/kotik.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    print("\npet_photo", pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)   #получаем ключ
    _, add_pets = pf.post_add_pets_no_foto(auth_key, 2, "wiku", '2')
    print("add_pets", add_pets)

    print("add_pets['[id]=", add_pets["id"])

    status, result = pf.post_add_photo(auth_key, add_pets['id'], pet_photo)
    print("result['pet_photo']", result['pet_photo'])
    assert status == 200
    assert result['pet_photo'] != ''

def test_get_api_key_invalid_password(email = valid_email, password = ""):
    # Пытаемся получить ключ с пустым паролем
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_get_all_pets_with_invalid_key(filter = ''):
    # Получаем ключ. Доступное значение параметра filter - 'my_pets' либо ''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем к ключу лишний символ
    auth_key['key']+="q"
    # Пробуем получить список питомцев с невалидным ключом
    status, result = pf.get_list_of_pets(auth_key=auth_key, filter=filter)
    # Смотрим что приходит статус ошибки
    assert status == 403

def test_post_add_pets_no_foto_invalid_data(name="Bars", animal_type="кот", age="^*^&"):
    # Получаем ключ и добавляем питомца без фото, значение возраста указали спецсимволами
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pets_no_foto(auth_key, name, animal_type, age)

    # Ожидаем ошибку некорректных данных
    assert status == 400

def test_post_add_pets_no_foto_invalid_data_2(name="Bars", animal_type="кот", age=None):
    # Получаем ключ и добавляем питомца без фото, значение возраста не указываем
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pets_no_foto(auth_key, name, animal_type, age)

    # Ожидаем ошибку некорректных данных
    assert status == 400

def test_post_add_new_pets(name="Mia-nana", animal_type="wolfen", age='1', pet_photo = r'images/file.txt'):
    # Сохраняем в переменную pet_photo полный путь к файлу
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ и добавляем питомца
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сравниваем что в ответ пришла ошибка данных
    assert status == 400

def test_delete_pets_invalid_id():
    # получаем ключ и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    #  Если список пустой, то создаем питомца
    if len(my_pets['pets']) == 0:
        pf.post_add_new_pet(auth_key, "oland", "wol", '22', r'images/kotik.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    #  Берем id первого питомца и меняем его, пробуем удалить питомца с несуществующим id

    pet_id = my_pets["pets"][0]["id"]
    print("do", pet_id)
    pet_id_2 = pet_id +"12"
    print("posle", pet_id_2)
    status, _ = pf.delete_pets(auth_key, pet_id_2)


    # Получаем список питомцев и  ожидаем что первый питомец не удалился
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    print("values",my_pets['pets'])
    assert status == 400
    assert pet_id in my_pets['pets'][0]['id']

def test_delete_all_pets():
    # получаем ключ и список своих питомцев. Тест удаляет чужого питомца.
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем список питомцев всех пользователей
    _, pets = pf.get_list_of_pets(auth_key, '')

    #  Берем id первого питомца, пробуем удалить
    pet_id = pets["pets"][0]["id"]
    status, _ = pf.delete_pets(auth_key, pet_id)

    # Получаем список питомцев и  ожидаем что первый питомец не удалился
    _, pets = pf.get_list_of_pets(auth_key, '')
    assert status == 400

def test_duble_delete():
    # получаем ключ и список своих питомцев. Тест дважды удаляет питомца.
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем список питомцев
    _, pets = pf.get_list_of_pets(auth_key, 'my_pets')
    #  Берем id первого питомца, пробуем удалить
    pet_id = pets["pets"][0]["id"]
    # Пробуем два раза удалить один и тот же id
    status, _ = pf.delete_pets(auth_key, pet_id)
    status, _ = pf.delete_pets(auth_key, pet_id)

    # Получаем список питомцев и  ожидаем сообщение об ошибке
    _, pets = pf.get_list_of_pets(auth_key, 'my_pets')

    assert status == 400
    assert pet_id not in pets.values()


