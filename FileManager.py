import json

class FileManager:
    def load_data(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def save_data(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)

    def read_json(self, json_file_path):
        with open(json_file_path, 'r') as file:
            return json.load(file)
        
    def write_json(self, list_of_dicts, json_file_path):
        with open(json_file_path, 'w') as file:
            json.dump(list_of_dicts, file)
    
    def add_to_json(self, data, json_file_path):
        current_data = self.read_json(json_file_path)
        current_data.append(data)
        self.write_json(current_data, json_file_path)


            