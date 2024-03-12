import requests
exchange_rate_api_url = 'https://open.er-api.com/v6/latest'
valid_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD']

from FileManager import FileManager
from HistoryMessages import HistoryMessages

class CurrencyExchange:
    def __init__(self, balance=0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"

    def write_to_history(self, hist_dict):
        current_hist_data = self.file_manager.read_json(self.hist_file_path)
        current_hist_data.append(hist_dict)
        self.file_manager.write_json(self.hist_file_path, current_hist_data)

    def get_exchange_rates(self):
        try:
            response = requests.get(exchange_rate_api_url)
            response.raise_for_status()
            return response.json().get('rates')  
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return None
        
    def exchange_currency(self, currency_from, currency_to, amount):
        exchange_rates = self.get_exchange_rates()
        if exchange_rates:
            if not isinstance(amount, (int, float)) or currency_from not in valid_currencies or currency_to not in valid_currencies:
                history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
                self.write_to_history(history_message)
                return None

            converted_amount = amount * exchange_rates[currency_to] / exchange_rates[currency_from]

            if converted_amount > 0:
                history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
                self.write_to_history(history_message)
                return converted_amount
            else:
                history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
                self.write_to_history(history_message)
                return None
        else:
            return None