import requests

class WolfBetAPI:
    def __init__(self, api_key):
        self.base_url = 'https://wolfbet.com/api/v1'
        self.api_key = api_key

    def request(self, endpoint, method='GET', data=None):
        url = f'{self.base_url}/{endpoint}'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError('Invalid HTTP method')
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # e.g. 404, 501, etc.
        except Exception as err:
            print(f'Other error occurred: {err}')  # Handle other requests exceptions

    def get_live_bets(self):
        return self.request('live-bets')

    def place_bet(self, bet_data):
        return self.request('place-bet', method='POST', data=bet_data)

# Usage example:
# Initialize the API client with your API key
# api = WolfBetAPI('your_api_key_here')
# live_bets = api.get_live_bets()
# print(live_bets)