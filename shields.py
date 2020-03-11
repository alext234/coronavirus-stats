import json
def write_shields_json(filename, label='', message=''):    
    json_payload = {'schemaVersion': 1, 
              'label': label, 
              'message': message}
    with open(filename, 'w') as fo:
        fo.write(json.dumps(json_payload))
