from FileManager import FileManager
from HistoryMessages import HistoryMessages

class Account:
    def __init__(self, balance = 0):
        self.balance = balance
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        pass 
        current_hist_data = self.file_manager.read_json(self.hist_file_path)
        current_hist_data.append(hist_dict)
        self.file_manager.write_json(self.hist_file_path, current_hist_data)

    def deposit(self, amount):
        pass
        if not isinstance(amount, int) or amount <= 0:
            history_message = HistoryMessages.deposit("failure", amount, self.balance)
        else:
            self.balance += amount
            history_message = HistoryMessages.deposit("success", amount, self.balance)

        self.write_to_history(history_message

    def debit(self, amount):
        pass
        if not isinstance(amount, int) or amount <= 0 or amount > self.balance:
            history_message = HistoryMessages.debit("failure", amount, self.balance)
        else:
            self.balance -= amount
            history_message = HistoryMessages.debit("success", amount, self.balance)

    def get_balance(self):
        return self.balance

    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
        else:
            return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'
        

    def get_history(self):
        pass
        history_data = self.file_manager.read_json(self.hist_file_path)
        history_strings = [self.dict_to_string(hist_dict) for hist_dict in history_data]
        return history_strings