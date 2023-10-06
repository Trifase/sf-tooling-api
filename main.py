from sfdclib import SfdcSession
from sfdclib import SfdcToolingApi
import json
import config

s = SfdcSession(username=config.username,
                password=config.password,
                token=config.token,
                is_sandbox=False,
                api_version=config.api_ver)
s.login()

tooling = SfdcToolingApi(s)


def create_label_payload(dict):
    data = {
        'Name' : dict['api_name'],
        'MasterLabel' : dict['api_name'],
        'Value' : dict['value'],
        'IsProtected' : 'true',
        'Category' : dict['cat'],
        'Language' : 'en_US'
    }
    data = json.dumps(data)
    return data


def create_custom_label(api_name, category, value, language='en_US'):
    data = {
        'Name' : api_name,
        'MasterLabel' : api_name,
        'Value' : value,
        'IsProtected' : 'true',
        'Category' : category,
        'Language' : language
    }
    data = json.dumps(data)
    return data



for n in range(50, 100):
    api_name = f'Automatic_label_creation_{n}'
    value = f'Test Label {n}'
    category = 'Automatic label'
    data = create_custom_label(api_name, category, value)
    
    r = tooling.post('/sobjects/ExternalString', data)
    print(f'Carico la label {api_name}...', end='')

    if r['success']:
        print('✔️')
    else:
        print('❌')
