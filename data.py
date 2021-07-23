import requests

question_settings = {
    'amount': 10,
    'type': 'boolean'
}

question_data = requests.get(url='https://opentdb.com/api.php', params=question_settings)
question_data.raise_for_status()
data = question_data.json()
question_data = (data['results'])


