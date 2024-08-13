import requests


def registration_ref(username, firstName, lastName, id, code):
    if code == "None":
        url = f"https://waterwa1ker-nuts-95d6.twc1.net/api/v1/auth/init"
    else:
        url = f"https://waterwa1ker-nuts-95d6.twc1.net/api/v1/auth/init?ref={code}"
    params = {
        "username": username,
        "firstName": firstName,
        "lastName": lastName,
        "id": id
    }

    # Заголовки
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=params, headers=headers)
    # Проверка
    if response.status_code == 200:
        try:
            # Обработка данных ответа
            data = response.json()
            return data
        except requests.exceptions.JSONDecodeError:
            print("Ошибка декодирования JSON. Тело ответа:")
            print(response.text)
            return None
    else:
        print(f"Ошибка: {response.status_code}")
        print(response.text)
        return None


