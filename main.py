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

def create_custom_label(api_name, category, value, language='en_US'):
    """This create a payload ready to be posted to the api. It creates a custom label.

    Args:
        api_name (str): This is the name of the label. It will be also be used as the developer name of the label. No spaces I guess?
        category (str): category of the label
        value (str): This is the actual text of the label
        language (str, optional): Language. Defaults to 'en_US'.

    Returns:
        _type_: _description_
    """
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
