import requests



base_url = "https://yougile.com"

# Получить список компаний
def test_auth():
    creds = {
        'login': 'yellowratty@rustyload.com',
        'password': '2335108'
    }
    resp = requests.post(base_url + '/api-v2/auth/companies', json=creds)
    response_body = resp.json()["content"][0]
    first_company = response_body["id"]
    assert resp.status_code == 200
    assert len(response_body) > 0
    return first_company


# Создать ключ
def test_key():
     creds = {
        'login': 'yellowratty@rustyload.com',
        'password': '2335108',
        'companyId': test_auth()
     }
     resp = requests.post(base_url + '/api-v2/auth/keys', json=creds)
     response_body = resp.json()["key"]
     assert resp.status_code == 201
     return response_body


# получить токен 

def test_token():
    my_token = {
        'Authorization': ("Bearer " + test_key())
    }
    return my_token

# Получить список проектов (надо исп полученный ключ в запросе)

def test_get_project():
    resp = requests.get(base_url+'/api-v2/projects', headers=test_token())
    assert resp.status_code == 200

# Получить ИД сотрудника
def test_ID_worker():
     resp = requests.get(base_url+'/api-v2/users', headers=test_token())
     response_body = resp.json()["content"][0]
     worker = response_body["id"]
     #assert worker == "b4c03f3c-badf-44f6-8206-cd7b2f236bea"
     assert resp.status_code == 200
     return worker


# создать проект (надо получить ид сотрудника) 
def test_new_project():
    project = {
        "title": "Новый проект",
        "users": {
             test_ID_worker(): "admin"
        }
    }
    resp = requests.post(base_url+'/api-v2/projects', json=project, headers=test_token())
    response_body = resp.json()["id"]
    assert resp.status_code == 201
    assert resp.status_code == 401 
    return response_body


# Получить по ID проект
def test_id_project():
    id_project = test_new_project()
    resp = requests.get(base_url+'/api-v2/projects/'+id_project, headers=test_token())
    response_body = resp.json()["id"]
    assert id_project == response_body
    assert resp.status_code == 200


# изменить проект 
def test_change_project():
    id_project = test_new_project()
    change = {
        "title": "Очень новый проект"
        }
    resp = requests.put(base_url+'/api-v2/projects/'+id_project, json=change, headers=test_token())
    assert resp.status_code == 200

